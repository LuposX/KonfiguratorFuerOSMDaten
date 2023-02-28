from __future__ import annotations

import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i
import src.osm_configurator.model.project.calculation.default_value_finder as default_value_finder_i
import src.osm_configurator.model.parser.tag_parser as tag_parser_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.prepare_calculation_phase as prepare_calculation_phase_i
import src.osm_configurator.model.project.calculation.paralellization.work_manager as work_manager_i
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum
import src.osm_configurator.model.project.calculation.paralellization.work as work_i

import geopandas as gpd
from fiona.errors import DriverError

from pathlib import Path

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, List, Dict, Any
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from geopandas import GeoDataFrame, GeoSeries
    from src.osm_configurator.model.parser.tag_parser import TagParser
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from src.osm_configurator.model.project.calculation.paralellization.work_manager import WorkManager
    from src.osm_configurator.model.project.calculation.paralellization.work import Work
    from src.osm_configurator.model.project.calculation.prepare_calculation_information import \
        PrepareCalculationInformation


class ReductionPhase(ICalculationPhase):
    """
    This calculation phase is responsible for reducing bigger OSM-elements on single coordinates and for generating
    the values of the attributes for alle OSM-elements.
    For details see the method calculate().
    """

    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.REDUCTION_PHASE

    def calculate(self, configuration_manager_o: ConfigurationManager,
                  application_manager: ApplicationSettings) -> Tuple[CalculationState, str]:
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
            application_manager (ApplicationSettings): The settings of the application

        Returns:
              Tuple[CalculationState, str]: The state of the calculation after this phase finished its execution or failed trying so and a string which describes what happened e.g. an error.
        """
        prepare_calc_obj: PrepareCalculationInformation = prepare_calculation_phase_i.PrepareCalculationPhase \
            .prepare_phase(configuration_manager_o=configuration_manager_o,
                           current_calculation_phase=calculation_phase_enum.CalculationPhase.REDUCTION_PHASE,
                           last_calculation_phase=calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE)

        # Return if we got an error
        if prepare_calc_obj.get_calculation_state() is not None:
            return prepare_calc_obj.get_calculation_state(), prepare_calc_obj.get_error_message()

        # get the category manager
        category_manager_o: CategoryManager = configuration_manager_o.get_category_manager()

        # Iterate over all traffic cells and generate the attractiveness (using multiprocessing)
        work_manager: WorkManager = work_manager_i.WorkManager(
            application_manager.get_setting(application_settings_enum.ApplicationSettingsDefault.NUMBER_OF_PROCESSES))

        for traffic_cell_file_path in prepare_calc_obj.get_list_of_traffic_cell_checkpoints():
            execute_traffic_cell: Work = work_i.Work(
                target=self._parse_the_data_file,
                args=(traffic_cell_file_path,
                      category_manager_o,
                      prepare_calc_obj.get_checkpoint_folder_path_current_phase(),
                      )
            )
            work_manager.append_work(execute_traffic_cell)

            try:
                work_manager.do_all_work()

            except (FileNotFoundError, DriverError) as err:
                return calculation_state_enum_i.CalculationState.ERROR_FILE_NOT_FOUND, str(err.args)

            # If there's an error while encoding the file.
            except (ValueError, DriverError, UnicodeDecodeError) as err:
                return calculation_state_enum_i.CalculationState.ERROR_ENCODING_THE_FILE, ''.join(str(err))

            # If the file cannot be opened.
            except OSError as err:
                return calculation_state_enum_i.CalculationState.ERROR_COULDNT_OPEN_FILE, ''.join(str(err))

            except Exception as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, str(err.args)

        return calculation_state_enum_i.CalculationState.RUNNING, ""

    def _parse_the_data_file(self,
                             traffic_cell_file_path: Path,
                             category_manager_o: CategoryManager,
                             checkpoint_folder_path_current_phase: Path):

        tag_parser_o: TagParser = tag_parser_i.TagParser()

        # Read out dataframe from disk into memory
        df = gpd.read_file(traffic_cell_file_path,
                           GEOM_POSSIBLE_NAMES=model_constants_i.CL_GEOMETRY,
                           KEEP_GEOM_COLUMNS="NO"
                           )

        # Remove unwanted nodes
        # ---------------------
        # We remove all nodes which are in an area and have the same category as them
        # Why? Because they are most likely doubled elements.
        self._remove_nodes_in_areas_with_same_category(df)

        # Initialize Data
        # --------------.
        # Initialize a dictionary in which we will save our calculated data
        reduction_phase_data = self._initialize_data_save()

        default_value_finder_o = default_value_finder_i.DefaultValueFinder()

        # Calculate data
        # --------------
        # This for-loop is for the calculation
        # iterate over the dataframe
        idx: int
        row: GeoSeries
        for idx, row in df.iterrows():
            # Initialize a temporal data save location
            # just used for a single osm element
            # we do this, so we can compare at the end if we have an entry for each key.
            data_entry: Dict = self._initialize_data_save()

            curr_category: Category = category_manager_o.get_category(row[model_constants_i.CL_CATEGORY])

            curr_default_value_list: List[DefaultValueEntry] = curr_category.get_default_value_list()

            # make the string to a list of string
            osm_elements_list_tags: List[Tuple[str, str]] = tag_parser_o.dataframe_tag_parser(
                row[model_constants_i.CL_TAGS])
            osm_elements_list_tags: Dict[str, str] = tag_parser_o.list_to_dict(osm_elements_list_tags)

            curr_default_value: DefaultValueEntry = default_value_finder_o.find_default_value_entry_which_applies(
                curr_default_value_list, osm_elements_list_tags)

            # This means we don't need to calculate anything
            if curr_category.get_strictly_use_default_values():
                self._set_data_entry_from_default_value(curr_default_value, reduction_phase_data, row, data_entry)

            # If strictly-use-default-values isn't activated, we need to calculate the data
            else:
                # These are the attributes we need to calculate
                activated_attributes: List[Attribute] = curr_category.get_activated_attribute()
                # get the not activated
                not_activated_attributes: List[Attribute] = curr_category.get_not_activated_attribute()

                # previously calculated attributes temp data saver
                already_calculated_attributes: Dict[str, float] = {}

                # Add the attributes to the list that are not activated(which means that don't get calculated)
                # The data saver is from which we later built our geodataframe
                self._add_attributes_to_data_saver(already_calculated_attributes, curr_default_value, data_entry,
                                                   not_activated_attributes)

                # transform list into a dictionary
                activated_attributes_dict: Dict = {}
                for attribute_entry in activated_attributes:
                    activated_attributes_dict.update({attribute_entry.get_name(): attribute_entry})

                # Insert the data which isn't calculated from the attributes
                # This is data such as the name of the traffic cell
                self._save_non_calculated_non_attribute_data(data_entry, row)

                # calculate the activated attributes
                self._calculate_activated_attributes(activated_attributes_dict, already_calculated_attributes,
                                                     curr_category, curr_default_value, data_entry, df, row)

                # Add the calculated data for a single osm element to the main saving point
                self._add_calculated_data_to_data_saver(data_entry, reduction_phase_data)

        # We now need to construct our dataframe from the data
        column_name = []
        column_name.extend(model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES)
        column_name.extend([e.get_name() for e in attribute_enum_i.Attribute])
        traffic_cell_data_frame = gpd.GeoDataFrame(data=reduction_phase_data, columns=column_name)

        # save the parsed osm data
        # name of the file
        file_name = traffic_cell_file_path.stem

        traffic_cell_data_frame. \
            to_csv(checkpoint_folder_path_current_phase.
                   joinpath(file_name + osm_file_format_enum_i.OSMFileFormat.CSV.get_file_extension()))

    def _add_attributes_to_data_saver(self, already_calculated_attributes, curr_default_value, data_entry,
                                      not_activated_attributes):
        not_act_attribute: Attribute
        for not_act_attribute in not_activated_attributes:
            tmp_default_value: float = curr_default_value.get_attribute_default(
                not_act_attribute)
            data_entry[not_act_attribute.get_name()].append(tmp_default_value)

            # we save already calculated attributes in this list if we have attributes
            # which are dependent on other attributes which need to be calculated first.
            already_calculated_attributes.update({not_act_attribute.get_name(): tmp_default_value})

    def _add_calculated_data_to_data_saver(self, data_entry, reduction_phase_data):
        for key_data_entry, value_data_entry in data_entry.items():
            if len(value_data_entry) == 1:
                # since we only save one value per entry we can do [0]
                reduction_phase_data[key_data_entry].append(value_data_entry[0])

    def _calculate_activated_attributes(self, activated_attributes_dict, already_calculated_attributes,
                                        curr_category, curr_default_value, data_entry, df, row):
        key_act_attribute: str
        value_act_attribute: Attribute
        for key_act_attribute, value_act_attribute in activated_attributes_dict.items():
            if value_act_attribute == attribute_enum_i.Attribute.PROPERTY_AREA:
                # property needs to be treated special, because it depends on special data
                # i.e. all osm element which lie in its border.

                curr_category.get_calculation_method_of_area()

                calculated_value: float = value_act_attribute.calculate_attribute_value(curr_category,
                                                                                        row,
                                                                                        already_calculated_attributes,
                                                                                        curr_default_value,
                                                                                        df)

            else:
                # Calculate the value of the osm element for the given attribute
                calculated_value: float = value_act_attribute.calculate_attribute_value(curr_category,
                                                                                        row,
                                                                                        already_calculated_attributes,
                                                                                        curr_default_value,
                                                                                        None)
            # we save already calculated attributes in this list if we have attributes
            # which are dependent on other attributes which need to be calculated first.
            already_calculated_attributes.update({key_act_attribute: calculated_value})

            # The data entry will later be saved to our main memory for all osm elements
            data_entry[key_act_attribute].append(calculated_value)

    def _save_non_calculated_non_attribute_data(self, data_entry, row):
        DF_CL_NAME: str
        for DF_CL_NAME in model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES:
            # Do point reduction
            if DF_CL_NAME == model_constants_i.CL_GEOMETRY:
                # Returns a representation of the object’s geometric centroid (point).
                data_entry[model_constants_i.CL_GEOMETRY].append(
                    row[model_constants_i.CL_GEOMETRY].centroid)

            else:
                data_entry[DF_CL_NAME].append(row[DF_CL_NAME])

    def _initialize_data_save(self):
        """
        This method is used to create a dictionary with the correct keys which are the
        attributes which we want to save and other information about the osm element such as the name.
        The Dictionary has as key one type of information for the osm element which will later be transformed
        in a column in the dataframe and each key has a  list of values.
        """
        reduction_phase_data: Dict = {}

        # First we add all columns which are not attributes such as "name", "geometry".
        column_name: str
        for column_name in model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES:
            reduction_phase_data.update({column_name: []})

        # Next we add all column which are created from attributes
        tmp_attribute: Attribute
        for tmp_attribute in attribute_enum_i.Attribute:
            reduction_phase_data.update({tmp_attribute.get_name(): []})

        return reduction_phase_data

    def _set_data_entry_from_default_value(self, curr_default_value: DefaultValueEntry,
                                           reduction_phase_data: Dict,
                                           osm_element: GeoSeries,
                                           data_entry: Dict):
        """
        This method uses DefaultValueEntry to calculate the default value for the osm element
        """
        DF_CL_NAME: str
        for DF_CL_NAME in model_constants_i.DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES:
            # Do point reduction
            if DF_CL_NAME == model_constants_i.CL_GEOMETRY:
                # Returns a representation of the object’s geometric centroid (point).
                reduction_phase_data[DF_CL_NAME] += osm_element[model_constants_i.CL_GEOMETRY].centroid

            else:
                data_entry[DF_CL_NAME] += osm_element[DF_CL_NAME]

        # Get the default values for the attributes
        attribute: Attribute
        for attribute in attribute_enum_i.Attribute:
            data_entry[Attribute.get_name()] += curr_default_value.get_attribute_default(attribute)

    def _remove_nodes_in_areas_with_same_category(self, df: GeoDataFrame):
        # If we have nodes in a area(relations or way) and the nodes have the same category as the area in which
        # it lies we delete the node.
        # So we iterate over all osm_elements which are area and check if there are nodes in it
        # if yes we check if they have the same category and if yes we delete them, otherwise they can stay.
        # TODO: the index of new geodatframe should have the same index as the old ones, if not here is the issue.
        area_df: GeoDataFrame = df.loc[(df[model_constants_i.CL_OSM_TYPE] == model_constants_i.AREA_WAY_NAME) | (
                df[model_constants_i.CL_OSM_TYPE] == model_constants_i.AREA_RELATION_NAME)]
        node_df: GeoDataFrame = df.loc[(df[model_constants_i.CL_OSM_TYPE] == model_constants_i.NODE_NAME)]
        idx: int
        node_row: GeoSeries
        for idx_node, node_row in node_df.iterrows():
            # This should return a GeoSeries which consists of bool values, true when the matching up row
            # in the dataframe contains the node otherwise false.
            found_areas_bool: GeoSeries = area_df[model_constants_i.CL_GEOMETRY].within(
                node_row[model_constants_i.CL_GEOMETRY])  # TODO: This could be wrong if yes use contains() instead

            # iterate over them and check their categories
            i: int
            found_series: GeoSeries
            # The iloc takes in our geo-series which consists of boolean values and returns all entries
            # in the dataframe which row number is true.
            for i, found_series in area_df.loc[found_areas_bool].iterrows():
                # This checks if the category name of the found_area is the same as the node ones
                # If it has the same category we delete it.
                if found_series[model_constants_i.CL_CATEGORY].item() == node_row[model_constants_i.CL_CATEGORY].item():
                    # delete the node
                    df.drop(idx_node)
                    break
