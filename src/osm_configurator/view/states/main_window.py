from __future__ import annotations

import customtkinter

import screeninfo

import src.osm_configurator.control.export_controller_interface
import src.osm_configurator.control.category_controller_interface
import src.osm_configurator.control.project_controller_interface
import src.osm_configurator.control.settings_controller_interface
import src.osm_configurator.control.aggregation_controller_interface
import src.osm_configurator.control.application_controller
import src.osm_configurator.control.calculation_controller_interface
import src.osm_configurator.control.cut_out_controller_interface
import src.osm_configurator.control.data_visualization_controller_interface
import src.osm_configurator.control.osm_data_controller_interface

import src.osm_configurator.view.states.state_manager as state_manager_i
import src.osm_configurator.view.states.state as state_i
import src.osm_configurator.view.states.positioned_frame as positioned_frame_i

import src.osm_configurator.view.states.view_constants as view_constants_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.control.export_controller_interface import IExportController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
    from src.osm_configurator.control.application_controller import ApplicationController
    from src.osm_configurator.control.calculation_controller_interface import ICalculationController
    from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
    from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
    from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
    from src.osm_configurator.view.states.state import State

# Final Variablen
TOP_ROW_WEIGHT: Final = 1
BOTTOM_ROW_WEIGHT: Final = 1
MIDDLE_ROW_WEIGHT: Final = 4
COLUM_WEIGHT: Final = 1


class MainWindow:
    """
    This class provides the GUI, the user will be working on.
    It is made dynamic and can change between different frames, to show different information and buttons to the user.
    Its job is to just show the frames of different states and create the window the GUI will be used on.
    """

    def __init__(self, export_controller: IExportController, category_controller: ICategoryController, project_controller: IProjectController, settings_controller: ISettingsController,
                 aggregation_controller: IAggregationController, calculation_controller: ICalculationController, cut_out_controller: ICutOutController,
                 data_visualization_controller: IDataVisualizationController, osm_data_controller: IOSMDataController):
        """
        This method creates a MainWindow with a connection to the given control.

        Args:
            export_controller (export_controller.ExportController): Respective controller.
            category_controller (category_controller.CategoryController): Respective controller.
            project_controller (project_controller.ProjectController): Respective controller.
            settings_controller (settings_controller.SettingsController): Respective controller.
            aggregation_controller (aggregation_controller.AggregationController): Respective controller.
            calculation_controller (calculation_controller.CalculationController): Respective controller.
            cut_out_controller (cut_out_controller.CutOutController): Respective controller.
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller.
            osm_data_controller (osm_data_controller.OSMDataController): Respective controller.
        """
        # Creating the mainWindow and setting its position, and making it resizable
        self._window = customtkinter.CTk()
        self._window.title(view_constants_i.ViewConstants.WINDOW_TITLE.value)

        # Selecting the primary Monitor to get accurate location for centering the window
        primary_monitor = None
        for monitor in screeninfo.get_monitors():
            if monitor.is_primary:
                primary_monitor = monitor
                break

        screen_height = primary_monitor.height
        screen_width = primary_monitor.width

        true_height = screen_height / 2 - view_constants_i.ViewConstants.MAIN_WINDOW_HEIGHT.value / 2
        true_width = screen_width / 2 - view_constants_i.ViewConstants.MAIN_WINDOW_WIDTH.value / 2

        self._window.geometry("%dx%d+%d+%d" % (view_constants_i.ViewConstants.MAIN_WINDOW_WIDTH.value,
                                               view_constants_i.ViewConstants.MAIN_WINDOW_HEIGHT.value,
                                               true_width, true_height))
        self._window.minsize(view_constants_i.ViewConstants.MAIN_WINDOW_WIDTH_MINIMUM.value,
                             view_constants_i.ViewConstants.MAIN_WINDOW_HEIGHT_MINIMUM.value)
        self._window.resizable(True, True)

        # Configurating the grid for the Application
        self._window.grid_columnconfigure(0, weight=COLUM_WEIGHT)
        self._window.grid_rowconfigure(0, weight=TOP_ROW_WEIGHT)
        self._window.grid_rowconfigure(1, weight=MIDDLE_ROW_WEIGHT)
        self._window.grid_rowconfigure(2, weight=BOTTOM_ROW_WEIGHT)

        # Creating the StateManager
        self._state_manager = state_manager_i.StateManager(self, export_controller, category_controller,
                                                           project_controller,
                                                           settings_controller, aggregation_controller,
                                                           calculation_controller,
                                                           cut_out_controller, data_visualization_controller,
                                                           osm_data_controller)

        # Starting the mainloop
        self._window.mainloop()

    def change_state(self, last_state: State, new_state: State) -> bool:
        """
        This method changes from an old given state to a new given state to show on the MainWindow.

        Args:
            last_state (state.State): The state that needs to me removed from the MainWindow.
            new_state (state.State): The state that shall be shown by the MainWindow.

        Returns:
            bool: True, if the state change was successful, false if not.
        """
        # Making sure both states are not None
        if (last_state is None) or (new_state is None):
            return False

        # First making the last State invisible
        succsess = self._make_invisible(last_state)

        # If last State was succesfully removed, then we try to make the new state visible
        if not succsess:
            return False
        else:
            succsess = succsess and self._make_visible(new_state)

            return succsess

    def _make_visible(self, state: State) -> bool:
        """
        This method makes the given State visible on the MainWindow.

        Args:
            state (state.State): The state that shall be made visible.

        Returns:
            bool: True if the state could be made visible, false if not.
        """
        if state is None:
            return False

        frames: list[positioned_frame_i.PositionedFrame] = state.get_active_frames()

        # First getting all information about position and then placing the actual_frame there
        for frame in frames:
            column = frame.get_column()
            row = frame.get_row()
            column_span = frame.get_colum_span()
            row_span = frame.get_row_span()
            actual_frame = frame.get_frame()
            sticky_type = frame.get_sticky()

            actual_frame.master = self._window
            actual_frame.grid(row=row, column=column, rowspan=row_span, column_span=column_span, sticky=sticky_type)

        return True

    def _make_invisible(self, state: State) -> bool:
        """
        This method removes a given State from the MainWindow, so it cant be seen or interacted with anymore.

        Args:
            state (state.State): The state that shall not be visible anymore.

        Returns:
            bool: True, if the given state could be made invisible, false if not.
        """
        if state is None:
            return False

        frames: list[positioned_frame_i.PositionedFrame] = state.get_active_frames()

        # Getting all frames and removing them from the grid
        for frame in frames:
            actual_frame = frame.get_frame()
            actual_frame.grid_remove()

        return True
