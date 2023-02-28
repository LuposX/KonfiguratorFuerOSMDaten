from __future__ import annotations

import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i
import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.prepare_calculation_phase as prepare_calculation_phase_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.paralellization.work_manager as work_manager_i
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum
import src.osm_configurator.model.project.calculation.paralellization.work as work_i

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception import TagsWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.osm_data_wrongly_formatted_Exception import \
    OSMDataWronglyFormatted

import pandas as pd
from fiona.errors import DriverError

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import Tuple, Dict, List, Any
    from pandas import DataFrame
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from src.osm_configurator.model.project.calculation.paralellization.work_manager import WorkManager
    from src.osm_configurator.model.project.calculation.paralellization.work import Work
    from src.osm_configurator.model.project.calculation.prepare_calculation_information import \
        PrepareCalculationInformation


class AggregationPhase(ICalculationPhase):
    """
    This calculation phase is responsible for aggregating the attractivity attributes in the given traffic cells.
    For details see the method calculate().
    """
    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.AGGREGATION_PHASE

    def calculate(self, configuration_manager_o: ConfigurationManager,
                  application_manager: ApplicationSettings) -> Tuple[CalculationState, str]:
        """
        Aggregates the attractivity attributes in the given traffic cells.
        The calculation phase reads the data of the previous calculation phase. Now for every traffic cell all selected
        aggregation methods are performed for all attractivity attributes. For details on the different aggregation
        methods, see AggregationMethod.
        After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution.
            application_manager (ApplicationSettings): The settings of the application

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished its execution or failed trying so.
        """
        prepare_calc_obj: PrepareCalculationInformation = prepare_calculation_phase_i.PrepareCalculationPhase \
            .prepare_phase(configuration_manager_o=configuration_manager_o,
                           current_calculation_phase=calculation_phase_enum.CalculationPhase.AGGREGATION_PHASE,
                           last_calculation_phase=calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE)

        # Return if we got an error
        if prepare_calc_obj.get_calculation_state() is None:
            return prepare_calc_obj.get_calculation_state(), prepare_calc_obj.get_error_message()

        # Get the manager
        aggregation_configuration: AggregationConfiguration = configuration_manager_o.get_aggregation_configuration()
        category_manager: CategoryManager = configuration_manager_o.get_category_manager()

        # get all activated aggregation methods
        active_aggregation_methods: List[AggregationMethod] = aggregation_configuration.get_all_active_aggregation_methods()

        # Iterate over all traffic cells and generate the attractiveness (using multiprocessing)
        work_manager: WorkManager = work_manager_i.WorkManager(
            application_manager.get_setting(application_settings_enum.ApplicationSettingsDefault.NUMBER_OF_PROCESSES))

        # For each active aggregation method create one dataframe with all traffic cells in it
        aggregation_method: AggregationMethod
        for aggregation_method in active_aggregation_methods:
            execute_traffic_cell: Work = work_i.Work(
                target=self._parse_the_data,
                args=(aggregation_method,
                      category_manager,
                      prepare_calc_obj.get_checkpoint_folder_path_current_phase(),
                      prepare_calc_obj.get_list_of_traffic_cell_checkpoints()
                      )
            )
            work_manager.append_work(execute_traffic_cell)

            try:
                work_manager.do_all_work()

            except TagsWronglyFormatted as err:
                return calculation_state_enum_i.CalculationState.ERROR_TAGS_WRONGLY_FORMATTED, ''.join(str(err))

            except (OSMDataWronglyFormatted, DriverError, UnicodeDecodeError) as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, ''.join(str(err))

            # If there's an error while encoding the file.
            except ValueError as err:
                return calculation_state_enum_i.CalculationState.ERROR_ENCODING_THE_FILE, ''.join(str(err))

            # If the file cannot be opened.
            except OSError as err:
                return calculation_state_enum_i.CalculationState.ERROR_COULDNT_OPEN_FILE, ''.join(str(err))

        return calculation_state_enum_i.CalculationState.RUNNING, ""

    def _parse_the_data(self, aggregation_method: AggregationMethod,
                        category_manager: CategoryManager,
                        checkpoint_folder_path_current_phase: Path,
                        list_of_traffic_cell_checkpoints: List[Path]):

        # Create a dict where we save the dataframe
        # it has as key the name of a attractivity attribute and as value the list of calculated data entries
        # for each traffic cell.
        # Another key, value pair is the traffic cell name, per entry in a list.
        aggregation_phase_data: Dict[str, List] = {}
        aggregation_phase_data.update({model_constants_i.CL_TRAFFIC_CELL_NAME: []})

        attractivity_attribute: AttractivityAttribute
        for attractivity_attribute in category_manager.get_all_defined_attractivity_attributes():
            aggregation_phase_data.update({attractivity_attribute.get_attractivity_attribute_name(): []})

        # For each traffic cell.
        file_path: Path
        for file_path in list_of_traffic_cell_checkpoints:
            traffic_cell_data_frame: DataFrame = pd.read_csv(file_path, index_col=0)

            # add the name of the cell
            aggregation_phase_data[model_constants_i.CL_TRAFFIC_CELL_NAME].append(file_path.stem)

            # iterate over the column of the dataframe, each column corresponds to one attractivity attribute
            # This ignores the index column
            column_name: str
            for column_name in traffic_cell_data_frame.columns.values:
                # Calculate the given method
                column_result: float = aggregation_method.calculate_aggregation(traffic_cell_data_frame[column_name])

                aggregation_phase_data[column_name].append(column_result)

        aggregation_method_df: DataFrame = pd.DataFrame.from_dict(aggregation_phase_data)

        # Save the dataframe to the disk
        # This is the dataframe where all traffic cells and attractivity attributes are in it for a single
        # aggregation method.
        aggregation_method_df. \
            to_csv(checkpoint_folder_path_current_phase.
                   joinpath(aggregation_method.get_name()
                            + osm_file_format_enum_i.OSMFileFormat.CSV.get_file_extension()))
