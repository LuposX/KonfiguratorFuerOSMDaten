from __future__ import annotations

import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_state_enum

import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum as calculation_method_of_area_enum_i
import src.osm_configurator.model.parser.tag_parser as tag_parser_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i

import geopandas as gpd

from pathlib import Path

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, List, Dict
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
    from src.osm_configurator.model.parser.tag_parser import TagParser
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute

class ReductionPhase(ICalculationPhase):
    """
    This calculation phase is responsible for reducing bigger OSM-elements on single coordinates and for generating
    the values of the attributes for alle OSM-elements.
    For details see the method calculate().
    """
    def calculate(self, configuration_manager_o: ConfigurationManager) -> Tuple[CalculationState, str]:
        """
        Reduces OSM-elements on single points and calculates their attributes.
        The calculation phase reads the data of the previous calculation phase. OSM-elements that are not just a single
        node, must be reduced on one coordinate. For that the centre of the given shape is calculated and set as the
        new coordinate. This calculation phase does also calculate the attributes of every OSM-element. There is no
        generic form for calculation attributes, every attribute has an individual calculation. If a method of
        calculation is not possible or if the user turned it off, the value of the attributes is defined by the
        default value list of the category. The value is given by the highest priority entry of the default value
        list, that matches the osm-element. After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the configuration required for an execution.

        Returns:
              Tuple[CalculationState, str]: The state of the calculation after this phase finished its execution or failed trying so and a string which describes what happened e.g. an error.
        """

        # Get path to the results of the last Phase
        checkpoint_folder_path_last_phase: Path = calculation_phase_utility_i.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.TAG_FILTER_PHASE)

        # Get path to the results of the current Phase
        checkpoint_folder_path_current_phase: Path = calculation_phase_utility_i.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.REDUCTION_PHASE)

        # Prepare result folder
        deleter: FileDeletion = file_deletion_i.FileDeletion()
        deleter.reset_folder(checkpoint_folder_path_current_phase)

        # get the category manager
        category_manager_o: CategoryManager = ConfigurationManager.get_category_manager()

        # check if the folder exist
        if checkpoint_folder_path_last_phase.exists() and checkpoint_folder_path_current_phase.exists():
            list_of_traffic_cell_checkpoints: List = list(checkpoint_folder_path_last_phase.iterdir())
        else:
            return calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY, ""

        return self._parse_the_data_file(list_of_traffic_cell_checkpoints, category_manager_o, checkpoint_folder_path_current_phase)

    def _parse_the_data_file(self,
                             list_of_traffic_cell_checkpoints: List[Path],
                             category_manager_o: CategoryManager,
                             checkpoint_folder_path_current_phase: Path):

        for file_path in list_of_traffic_cell_checkpoints:
            try:
                # Read out dataframe from disk into memory
                df = gpd.read_file(file_path)
            except FileNotFoundError as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, str(err.args)

            except Exception as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, str(err.args)

            # calculated data data
            # should be in the format: model_constants_i.DF_CL_REDUCTION_PHASE
            # which should be: CL_OSM_TYPE, CL_OSM_ELEMENT_NAME, CL_GEOMETRY, CL_TAGS, CL_CATEGORY, CL_AREA_PROPERTY, CL_BUILDING_PROPERTY
            reduction_phase_data = []

            # This for-loop is for the calculation
            # iterate over the dataframe
            # TODI: I  think the data entries are in different order depending on which attributes are activated
            for idx, row in df.iterrows():
                curr_category: Category = category_manager_o.get_category(row[model_constants_i.CL_CATEGORY])
                curr_calculated_method_of_area: CalculationMethodOfArea = curr_category.get_calculation_method_of_area()

                curr_default_value_list: List[DefaultValueEntry] = curr_category.get_default_value_list()
                curr_default_value: DefaultValueEntry = self._find_default_value_entry_which_applies(curr_default_value_list, row[model_constants_i.CL_TAGS])  # maybe need a val()

                # This means we don't need to calculate anything
                if curr_category.get_strictly_use_default_values():
                    # create the data entry
                    data_entry: List = []

                    for DF_CL_NAME in model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES:
                        # Do point reduction
                        if DF_CL_NAME == model_constants_i.CL_GEOMETRY:
                            # Returns a representation of the object’s geometric centroid (point).
                            data_entry.append(row[model_constants_i.CL_GEOMETRY].centroid)

                        else:
                            data_entry.append(row[data_entry])

                    # Get the default values for teh attributes
                    for attribute in attribute_enum_i.Attribute:
                        data_entry.append(curr_default_value.get_attribute_default(attribute))

                    # Now add the osm element data row to the global data
                    reduction_phase_data.append(data_entry)

                # If strictly-use-default-values isn't activated, we need to calculate the data
                else:
                    # If our current osm element is a Node
                    # we can't calculate area for nodes.
                    # TODO: should we tread them the same or give them for area the default values?
                    if row[model_constants_i.CL_OSM_TYPE] == model_constants_i.NODE_NAME:
                        pass

                    # create the data entry
                    data_entry: List = []

                    # These are the attributes we need to calculate
                    activated_attributes: List[Attribute] = curr_category.get_activated_attribute()
                    # get the not activated
                    not_activated_attributes: List[Attribute] = curr_category.get_not_activated_attribute()

                    # transform list into a dictionary
                    activated_attributes_dict: Dict
                    for attribute_entry in activated_attributes:
                        activated_attributes_dict.update({attribute_entry.get_name(): attribute_entry})

                    # Insert the data which isn't calculated from the attributes
                    for DF_CL_NAME in model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES:
                        # Do point reduction
                        if DF_CL_NAME == model_constants_i.CL_GEOMETRY:
                            # Returns a representation of the object’s geometric centroid (point).
                            data_entry.append(row[model_constants_i.CL_GEOMETRY].centroid)

                        else:
                            data_entry.append(row[data_entry])

                    # Add the attributes to the list that are not activated(which means that don't get caclulated)
                    for act_attribute in activated_attributes_dict.keys():
                        data_entry.append(curr_default_value.get_attribute_default(act_attribute))

                    # calculate the not activated attributes
                    for not_act_attribute in not_activated_attributes:
                        data_entry.append(not_act_attribute.calculate_attribute_value(curr_category, idk))

                    # Now add the osm element data row to the global data
                    reduction_phase_data.append(data_entry)

            # We now need to construct our dataframe from the data
            column_name = []
            column_name.extend(model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES)
            column_name.extend([e.get_name() for e in attribute_enum_i.Attribute])
            traffic_cell_data_frame = gpd.GeoDataFrame(data=reduction_phase_data, columns=column_name)

            # save the parsed osm data
            # name of the file
            file_name = file_path.stem

            try:
                traffic_cell_data_frame. \
                    to_csv(checkpoint_folder_path_current_phase.
                           joinpath(file_name + osm_file_format_enum_i.OSMFileFormat.CSV.get_file_extension()))

            # If there's an error while encoding the file.
            except ValueError as err:
                return calculation_state_enum_i.CalculationState.ERROR_ENCODING_THE_FILE, ''.join(str(err))

            # If the file cannot be opened.
            except OSError as err:
                return calculation_state_enum_i.CalculationState.ERROR_COULDNT_OPEN_FILE, ''.join(str(err))

            return calculation_state_enum_i.CalculationState.RUNNING, ""

    def _find_default_value_entry_which_applies(self, default_value_list: List[DefaultValueEntry],
                                                osm_element_tags: List[str]):
        """
        This method figures out the first default value entry in the List which applies to the osm element.
        Where applies means that the osm element hast the same key-value pair then the default-value-entry.
        The Default-value-list has a priority the lowest index is the most important, if that element doesnt apply
        we iterate further along the list until we find a default-value-entry which applies.

        Args:
            default_value_list (List): A list of default-value entries
            osm_element_tags (List[str]): A list of unparsed tags of the osm element.
        """
        # Create a new Tag parser
        tag_parser_o: TagParser = tag_parser_i.TagParser()

        # These are the parsed tags from the osm element
        parsed_osm_element_tag_list = tag_parser_o.parse_tags(osm_element_tags)

        _default_value_entry: DefaultValueEntry
        for _default_value_entry in default_value_list:
            # This will return a dictionary with a single entry which is our tag
            parsed_default_value_tag = tag_parser_o.parse_tags(
                [_default_value_entry.get_default_value_entry_tag()])

            # Since teh dictionary has only one entry we can get the key this way
            key_tag_default_value_entry = parsed_default_value_tag.keys()[0]
            value_tag_default_value_entry = parsed_default_value_tag.get(key_tag_default_value_entry)

            # gets set to true when osm element applies to default_value_list entry
            is_osm_element_in_default_value: bool = False

            # get the first value of every tuple entry, which is the key of the tag
            # if this true this means the key value of the default value is also in the osm tag list.
            if key_tag_default_value_entry in parsed_osm_element_tag_list.keys():
                # The don't care symbol is "*" if thats set the value of the osm element for this tag
                # doesn't interest us.
                if value_tag_default_value_entry == model_constants_i.DONT_CARE_SYMBOL:
                    is_osm_element_in_default_value = True

                elif value_tag_default_value_entry == parsed_osm_element_tag_list.get(key_tag_default_value_entry):
                    is_osm_element_in_default_value = True

            if is_osm_element_in_default_value:
                return _default_value_entry

        return None

