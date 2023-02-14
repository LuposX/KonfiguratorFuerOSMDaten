from __future__ import annotations

import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.prepare_calculation_phase as prepare_calculation_phase_i

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception import TagsWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.osm_data_wrongly_formatted_Exception import \
    OSMDataWronglyFormatted

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.parser.osm_data_parser import OSMDataParser
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import Tuple, List, Any
    from geopandas import GeoDataFrame


class TagFilterPhase(ICalculationPhase):
    """
    This calculation phase is responsible for sorting OSM-elements into their corresponding categories.
    For details see the method calculate().
    """
    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE

    def calculate(self, configuration_manager_o: ConfigurationManager) -> Tuple[CalculationState, str]:
        """
        Sorts OSM-elements into their corresponding categories.
        Firstly this method reads in the OSM-files of the previously executed calculation phase. Every category has
        defined a tag filter in the configuration phase. The OSM-Elements are now sorted into the categories, depending
        on whether they do pass or do not pass the corresponding tag filters. A tag filter is defined by a
        black- and a whitelist. Each list is a collection of constraints of the tags of the osm-elements. An
        osm-element passes a tag filter, if all constraints of the whitelist are satisfied and no entry of the
        blacklist is satisfied.
        After execution the results shall be stored again on the hard-drive.

        Args:
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the configuration needed for an execution.

        Returns:
            Tuple[CalculationState, str]: The state of the calculation after this phase finished its execution or failed trying so and a string which describes what happened e.g. an error.
        """
        # Prepare various stuff for the calculation phase
        prepare_calc_tuple: Tuple[Any, Any, Any, Any] = prepare_calculation_phase_i.PrepareCalculationPhase\
            .prepare_phase(configuration_manager_o=configuration_manager_o,
                           current_calculation_phase=calculation_phase_enum_i.CalculationPhase.TAG_FILTER_PHASE,
                           last_calculation_phase=calculation_phase_enum_i.CalculationPhase.GEO_DATA_PHASE)

        # Return if we got an error
        if type(prepare_calc_tuple[0]) == calculation_state_enum_i.CalculationState:
            return prepare_calc_tuple[0], prepare_calc_tuple[1]

        else:
            cut_out_dataframe = prepare_calc_tuple[0]
            checkpoint_folder_path_last_phase = prepare_calc_tuple[1]
            checkpoint_folder_path_current_phase = prepare_calc_tuple[2]
            list_of_traffic_cell_checkpoints = prepare_calc_tuple[3]

        # Get the CategoryManager
        category_manager_o: CategoryManager = configuration_manager_o.get_category_manager()

        # create a new osm data parser, which is used to parse the osm data
        osm_data_parser_o: OSMDataParser = osm_data_parser_i.OSMDataParser()

        # parse the osm data  with the parser
        return self._parse_the_data_file(osm_data_parser_o=osm_data_parser_o,
                                         list_of_traffic_cell_checkpoints=list_of_traffic_cell_checkpoints,
                                         category_manager_o=category_manager_o,
                                         configuration_manager_o=configuration_manager_o,
                                         checkpoint_folder_path_current_phase=checkpoint_folder_path_current_phase)

    def _parse_the_data_file(self,
                             osm_data_parser_o: OSMDataParser,
                             list_of_traffic_cell_checkpoints: List,
                             category_manager_o: CategoryManager,
                             configuration_manager_o: ConfigurationManager,
                             checkpoint_folder_path_current_phase: Path) -> Tuple[CalculationState, str]:

        for file_path in list_of_traffic_cell_checkpoints:
            try:
                traffic_cell_data_frame: GeoDataFrame = osm_data_parser_o \
                    .parse_osm_data_file(file_path,
                                         category_manager_o,
                                         configuration_manager_o
                                         .get_cut_out_configuration()
                                         .get_cut_out_mode(),
                                         configuration_manager_o
                                         .get_cut_out_configuration()
                                         .get_cut_out_path())

            except TagsWronglyFormatted as err:
                return calculation_state_enum_i.CalculationState.ERROR_TAGS_WRONGLY_FORMATTED, ''.join(str(err))

            except OSMDataWronglyFormatted as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, ''.join(str(err))

                # name of the file
            file_name = file_path.stem

            # save the parsed osm data
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
