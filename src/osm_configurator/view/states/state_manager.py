from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_name_enum import StateName
    from src.osm_configurator.view.states.state import State
    from src.osm_configurator.view.states.positioned_frame import PositionedFrame
    from src.osm_configurator.view.states.main_window import MainWindow
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
    from src.osm_configurator.control.calculation_controller_interface import ICalculationController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
    from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
    from src.osm_configurator.control.export_controller_interface import IExportController
    from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.settings_controller_interface import ISettingsController


class StateManager:
    """
    This class manages the different states, that can be shown on a window.
    It knows what state is currently active and provides methods to change the state.
    """

    def __init__(self, main_window, export_controller, category_controller, project_controller, settings_controller,
                 aggregation_controller, application_controller, calculation_controller, cut_out_controller,
                 data_visualization_controller, osm_data_controller):
        """
        This method creates a StateManager, that will control what state is currently active and manages
        the changes between states.
        It will create all states, as well all the frames that exist and put them in the state they belong.

        Args:
            main_window (main_window.MainWindow): The MainWindow where the frames of the state shall be shown on.
            export_controller (export_controller.ExportController): Respective controller
            category_controller (category_controller.CategoryController): Respective controller
            project_controller (project_controller.ProjectController): Respective controller
            settings_controller (settings_controller.SettingsController): Respective controller
            aggregation_controller (aggregation_controller.AggregationController): Respective controller
            application_controller (application_controller.ApplicationController): Respective controller
            calculation_controller (calculation_controller.CalculationController): Respective controller
            cut_out_controller (cut_out_controller.CutOutController): Respective controller
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller
            osm_data_controller (osm_data_controller.OSMDataController): Respective controller
        """
        pass

    def default_go_right(self):
        """
        This method changes to the State that is the default_right state of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        pass

    def default_go_left(self):
        """
        This method changes to the state that is the default_left State of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        pass

    def change_state(self, new_state):
        """
        This method changes to the given state and deactivate the old one.

        Args:
            new_state (state_name_enum.StateName): The id of the new state that shall be activated.

        Returns:
            bool: True if state change was successful, false if not.
        """
        pass

    def get_state(self):
        """
        This method returns the currently active state.

        Returns:
            state.State: The currently active state.
        """
        pass

    def close_program(self):
        """
        This method closes the program and shuts the whole application down.
        """
        pass
