from __future__ import annotations

import os.path

from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i

import pathlib
import matplotlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from pathlib import Path
    from typing import Final

MAP_FILENAME: Final = "map_of_traffic_cells.html"
BOXPLOT_FILENAME: Final = "boxplot_of_result.png"


class DataVisualizationController(IDataVisualizationController):
    __doc__ = IDataVisualizationController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the DataVisualizationController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._model = model

    def generate_cut_out_map(self) -> Path | None:
        """
        Generates a cut out map, which visualizes the cut out data.

        Returns:
            Path: The Path towards the cut out data.
            None: If there was an error during saving creation of the map.
        """
        cut_out_file: Path = self._model.get_active_project().get_config_manager().get_cut_out_configuration() \
            .get_cut_out_path()

        map_saving_path: Path = self._model.get_active_project().get_project_path()

        if self._model.get_active_project().get_data_visualizer().create_map(cut_out_file=cut_out_file,
                                                                             map_saving_path=map_saving_path,
                                                                             filename=MAP_FILENAME):

            return Path(os.path.join(map_saving_path, MAP_FILENAME))

        # If saving or creating failed
        else:
            return None

    def generate_calculation_visualization(self) -> Path | None:
        """
        Generates a boxplot which visualizes the final data.

        Returns:
            Path: The path point towards the image which visualizes the data.
            None: If sth. went wrong.
        """
        boxplot_saving_path: Path = self._model.get_active_project().get_project_path()

        # Get where the data is saved for the results
        data_path: str = os.path.join(self._model.get_active_project().get_project_path(),
                                      calculation_phase_enum_i.CalculationPhase.get_folder_name_for_results())

        data_path: Path = Path(os.path.join(data_path,
                                            calculation_phase_enum_i.CalculationPhase.AGGREGATION_PHASE
                                            .get_folder_name_for_results()))

        if self._model.get_active_project().get_data_visualizer().create_boxplot(data_path=data_path,
                                                                                 boxplot_saving_path=boxplot_saving_path,
                                                                                 filename=BOXPLOT_FILENAME
                                                                                 ):
            return Path(os.path.join(data_path, BOXPLOT_FILENAME))

        # If saving or creating failed
        else:
            return None
