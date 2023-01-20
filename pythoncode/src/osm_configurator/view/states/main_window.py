import src.osm_configurator.control.export_controller
import src.osm_configurator.control.category_controller
import src.osm_configurator.control.project_controller
import src.osm_configurator.control.settings_controller
import src.osm_configurator.control.aggregation_controller
import src.osm_configurator.control.application_controller
import src.osm_configurator.control.calculation_controller
import src.osm_configurator.control.cut_out_controller
import src.osm_configurator.control.data_visualization_controller
import src.osm_configurator.control.osm_data_controller
import src.osm_configurator.view.states.state_name_enum


class MainWindow:
    """
    This class provides the GUI, the user will be working on.
    It is made dynamic and can change between different frames, to show different information and buttons to the user.
    Its job is to just show the frames of different states and create the window the GUI will be used on.
    """

    def __init__(self, export_controller, category_controller, project_controller, settings_controller,
                 aggregation_controller, application_controller, calculation_controller, cut_out_controller,
                 data_visualization_controller, osm_data_controller):
        """
        This method creates a MainWindow with a connection to the given control.

        Args:
            export_controller (export_controller.ExportController): Respective controller.
            category_controller (category_controller.CategoryController): Respective controller.
            project_controller (project_controller.ProjectController): Respective controller.
            settings_controller (settings_controller.SettingsController): Respective controller.
            aggregation_controller (aggregation_controller.AggregationController): Respective controller.
            application_controller (application_controller.ApplicationController): Respective controller.
            calculation_controller (calculation_controller.CalculationController): Respective controller.
            cut_out_controller (cut_out_controller.CutOutController): Respective controller.
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller.
            osm_data_controller (osm_data_controller.OSMDataController): Respective controller.
        """
        pass


    def change_state(self, last_state, new_state):
        """
        This method changes from an old given state to a new given state to show on the MainWindow.

        Args:
            last_state (state.State): The state that needs to me removed from the MainWindow.
            new_state (state.State): The state that shall be shown by the MainWindow.

        Returns:
            bool: True, if the state change was successful, false if not.
        """
        pass

    def _make_visible(self, state):
        """
        This method makes the given State visible on the MainWindow.

        Args:
            state (state.State): The state that shall be made visible.

        Returns:
            bool: True if the state could be made visible, false if not.
        """
        pass

    def _make_invisible(self, state):
        """
        This method removes a given State from the MainWindow, so it cant be seen or interacted with anymore.

        Args:
            state (state.State): The state that shall not be visible anymore.

        Returns:
            bool: True, if the given state could be made invisible, false if not.
        """
        pass
