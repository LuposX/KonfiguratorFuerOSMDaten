from __future__ import annotations

import src.osm_configurator.control.aggregation_controller as aggregation_controller
import src.osm_configurator.control.calculation_controller as calculation_controller
import src.osm_configurator.control.category_controller as category_controller
import src.osm_configurator.control.cut_out_controller as cut_out_controller
import src.osm_configurator.control.data_visualization_controller as data_visualization_controller
import src.osm_configurator.control.export_controller as export_controller
import src.osm_configurator.control.osm_data_controller as osm_data_controller
import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.settings_controller as settings_controller

import src.osm_configurator.model.application.application as application

import src.osm_configurator.view.states.main_window as main_window

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.aggregation_controller import AggregationController
    from src.osm_configurator.control.calculation_controller import CalculationController
    from src.osm_configurator.control.category_controller import CategoryController
    from src.osm_configurator.control.cut_out_controller import CutOutController
    from src.osm_configurator.control.data_visualization_controller import DataVisualizationController
    from src.osm_configurator.control.export_controller import ExportController
    from src.osm_configurator.control.osm_data_controller import OSMDataController
    from src.osm_configurator.control.project_controller import ProjectController
    from src.osm_configurator.control.settings_controller import SettingsController

    from src.osm_configurator.model.application.application import Application

    from src.osm_configurator.view.states.main_window import MainWindow


class ApplicationController:
    """
    The application controller is responsible for creating the model, the view and the control. It is the start of the
    application and boots everything up.
    """

    def __init__(self):
        """
        Creates a new Application. It creates the view, the model and the control. It is responsible for starting
        everything up and to prepare the normal workflow of the application.
        """
        # Create Model
        self._application: Application = application.Application()

        # Create Control
        self._aggregation_controller: AggregationController = aggregation_controller.AggregationController(
            self._application)
        self._calculation_controller: CalculationController = calculation_controller.CalculationController(
            self._application)
        self._category_controller: CategoryController = category_controller.CategoryController(self._application)
        self._cut_out_controller: CutOutController = cut_out_controller.CutOutController(self._application)
        self._data_visualization_controller: DataVisualizationController = data_visualization_controller\
            .DataVisualizationController(self._application)
        self._export_controller: ExportController = export_controller.ExportController(self._application)
        self._osm_data_controller: OSMDataController = osm_data_controller.OSMDataController(self._application)
        self._project_controller: ProjectController = project_controller.ProjectController(self._application)
        self._settings_controller: SettingsController = settings_controller.SettingsController(self._application)

        # Create View
        self._main_window: MainWindow = main_window.MainWindow(
            self._export_controller,
            self._category_controller,
            self._project_controller,
            self._settings_controller,
            self._aggregation_controller,
            None,
            self._calculation_controller,
            self._cut_out_controller,
            self._data_visualization_controller,
            self._osm_data_controller)

    def start(self):
        """
        Starts up the Application. Enters the normal workflow of the application
        """
        pass
        # TODO: Enter the GUI loop of the main window. This should look like:
        # self._main_window.start()


def main():
    """
    Starts the application.
    This class method's only job is, to give control to an instance of the ApplicationController.
    """
    application_controller: ApplicationController = ApplicationController()
    application_controller.start()
