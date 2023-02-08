from __future__ import annotations

import src.osm_configurator.view.states.state_name_enum
import src.osm_configurator.view.states.state
import src.osm_configurator.view.states.positioned_frame
import src.osm_configurator.view.states.main_window


class StateManager:
    """
    This class manages the different states, that can be shown on a window.
    It knows what state is currently active and provides methods to change the state.
    """

    # TODO: Adjust customtkinter attributes to the given enums

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

    def lock_state(self):
        """
        This method locks the Application in the current Frame
        """
        pass

    def unlock_state(self):
        """
        This Method unlocks the Application to be able to change Frames again
        """
        pass
