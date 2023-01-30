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

import geopandas as gpd

from pathlib import Path

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, List
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
    from src.osm_configurator.model.parser.tag_parser import TagParser

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

        return self._parse_the_data_file(list_of_traffic_cell_checkpoints, category_manager_o)

    def _parse_the_data_file(self, list_of_traffic_cell_checkpoints: List[Path], category_manager_o: CategoryManager):
        for file in list_of_traffic_cell_checkpoints:
            try:
                # Read out dataframe from disk into memory
                df = gpd.read_file(file)
            except FileNotFoundError as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, str(err.args)

            except Exception as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, str(err.args)

            # calculated data data
            # should be in the same format as last one

            # This for-loop is for the calculation
            # iterate over the dataframe
            for idx, row in df.iterrows():
                curr_category: Category = category_manager_o.get_category(row[model_constants_i.CL_CATEGORY])
                curr_calculated_method_of_area: CalculationMethodOfArea = curr_category.get_calculation_method_of_area()

                # If our current osm element is a Node
                if row[model_constants_i.CL_OSM_TYPE] == model_constants_i.NODE_NAME:

                else:
                    if curr_calculated_method_of_area == calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_SITE_AREA
                        # What we get here are shapely object, which are either a polygon(maybe multipolygon) or a point
                        row[model_constants_i.CL_GEOMETRY].area
                    else:
                        # TODO: Iam not sure how to go about this?
                        pass


            # This for loop is to get the default_value_data_list, which tells us for each osm element which  default entry applies to it
            # ----------------------------------------------------------------------------------------------------------
            # Create a list where we save which default value applies to which osm element.
            # idx is the osm element entry is the default value.
            default_value_data_list = []

            # iterate over the dataframe
            for idx, row in df.iterrows():
                curr_category: Category = category_manager_o.get_category(row[model_constants_i.CL_CATEGORY])

                # Get everything we need for point reduction
                curr_default_value_list: List[DefaultValueEntry] = curr_category.get_default_value_list()
                curr_calculated_method_of_area: CalculationMethodOfArea = curr_category.get_calculation_method_of_area()

                default_value_data_list.append(
                    self._find_default_value_entry_which_applies(curr_default_value_list, row["tags"])) # maybe need a val()

                # If our current osm element is a Node
                if row[model_constants_i.CL_OSM_TYPE] == model_constants_i.NODE_NAME:

                else:
                    if curr_calculated_method_of_area == calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_SITE_AREA
                        # What we get here are shapely object, which are either a polygon(maybe multipolygon) or a point
                        row[model_constants_i.CL_GEOMETRY].area
                    else:
                        # TODO: Iam not sure how to go about this?
                        pass

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






