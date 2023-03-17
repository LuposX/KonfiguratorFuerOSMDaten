from __future__ import annotations

import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i
import src.osm_configurator.model.project.calculation.prepare_calculation_phase as prepare_calculation_phase_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.paralellization.work_manager as work_manager_i
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum
import src.osm_configurator.model.project.calculation.paralellization.work as work_i

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception import TagsWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.osm_data_wrongly_formatted_Exception import \
    OSMDataWronglyFormatted
from fiona.errors import DriverError
from src.osm_configurator.model.application.application_settings import ApplicationSettings

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.parser.osm_data_parser import OSMDataParser
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import Tuple
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.project.calculation.paralellization.work_manager import WorkManager
    from src.osm_configurator.model.project.calculation.paralellization.work import Work
    from src.osm_configurator.model.project.calculation.prepare_calculation_information import \
        PrepareCalculationInformation


def _parse_the_data_file(osm_data_parser_o: OSMDataParser,
                         traffic_cell_file_path: Path,
                         category_manager_o: CategoryManager,
                         configuration_manager_o: ConfigurationManager,
                         checkpoint_folder_path_current_phase: Path):
    traffic_cell_data_frame: GeoDataFrame = osm_data_parser_o \
        .parse_osm_data_file(traffic_cell_file_path,
                             category_manager_o,
                             configuration_manager_o
                             .get_cut_out_configuration()
                             .get_cut_out_mode(),
                             configuration_manager_o
                             .get_cut_out_configuration()
                             .get_cut_out_path())

    # name of the file
    file_name = traffic_cell_file_path.stem

    # save the parsed osm data
    traffic_cell_data_frame. \
        to_csv(checkpoint_folder_path_current_phase.
               joinpath(file_name + osm_file_format_enum_i.OSMFileFormat.CSV.get_file_extension()))


class TagFilterPhase(ICalculationPhase):
    """
    This calculation phase is responsible for sorting OSM-elements into their corresponding categories.
    For details see the method calculate().
    """

    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE

    def calculate(self, configuration_manager_o: ConfigurationManager,
                  application_manager: ApplicationSettings) -> Tuple[CalculationState, str]:
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
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the
                configuration needed for an execution.
            application_manager (ApplicationSettings): The settings of the application

        Returns:
            Tuple[CalculationState, str]: The state of the calculation after this phase finished its execution or
                failed trying so and a string which describes what happened e.g. an error.
        """
        # Prepare various stuff for the calculation phase
        prepare_calc_obj: PrepareCalculationInformation = prepare_calculation_phase_i.PrepareCalculationPhase \
            .prepare_phase(configuration_manager_o=configuration_manager_o,
                           current_calculation_phase=calculation_phase_enum_i.CalculationPhase.TAG_FILTER_PHASE,
                           last_calculation_phase=calculation_phase_enum_i.CalculationPhase.GEO_DATA_PHASE)

        # Return if we got an error
        if prepare_calc_obj.get_calculation_state() is not None:
            return prepare_calc_obj.get_calculation_state(), prepare_calc_obj.get_error_message()

        # Get the CategoryManager
        category_manager_o: CategoryManager = configuration_manager_o.get_category_manager()

        # create a new osm data parser, which is used to parse the osm data
        osm_data_parser_o: OSMDataParser = osm_data_parser_i.OSMDataParser()

        # Iterate over all traffic cells and generate the attractiveness (using multiprocessing)
        work_manager: WorkManager = work_manager_i.WorkManager(
            application_manager.get_setting(application_settings_enum.ApplicationSettingsDefault.NUMBER_OF_PROCESSES))

        # parse the osm data  with the parser
        for traffic_cell_file_path in prepare_calc_obj.get_list_of_traffic_cell_checkpoints():
            execute_traffic_cell: Work = work_i.Work(
                target=_parse_the_data_file,
                args=(osm_data_parser_o,
                      traffic_cell_file_path,
                      category_manager_o,
                      configuration_manager_o,
                      prepare_calc_obj.get_checkpoint_folder_path_current_phase()
                      )
            )
            work_manager.append_work(execute_traffic_cell)

        # Start the processes
        try:
            work_manager.do_all_work()

        except TagsWronglyFormatted as err:
            return calculation_state_enum_i.CalculationState.ERROR_TAGS_WRONGLY_FORMATTED, ''.join(str(err))

        except OSMDataWronglyFormatted as err:
            return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, ''.join(str(err))

        # If there's an error while encoding the file.
        except (ValueError, DriverError, UnicodeDecodeError) as err:
            return calculation_state_enum_i.CalculationState.ERROR_ENCODING_THE_FILE, ''.join(str(err))

        return calculation_state_enum_i.CalculationState.RUNNING, "running"
