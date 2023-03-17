from __future__ import annotations

import sys

import customtkinter

import screeninfo

import src.osm_configurator.view.constants.main_window_constants as main_window_constants_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.control.export_controller_interface import IExportController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
    from src.osm_configurator.control.calculation_controller_interface import ICalculationController
    from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
    from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
    from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
    from src.osm_configurator.view.states.state import State
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.states.positioned_frame import PositionedFrame
    from screeninfo import Monitor

# Final Variables
TOP_ROW_WEIGHT: Final = 1
BOTTOM_ROW_WEIGHT: Final = 1
MIDDLE_ROW_WEIGHT: Final = 10
COLUM_WEIGHT: Final = 1


class MainWindow(customtkinter.CTk):
    """
    This class provides the GUI, the user will be working on.
    It is made dynamic and can change between different frames, to show different information and buttons to the user.
    Its job is to just show the frames of different states and create the window the GUI will be used on.
    """

    def __init__(self, export_controller: IExportController, category_controller: ICategoryController,
                 project_controller: IProjectController, settings_controller: ISettingsController,
                 aggregation_controller: IAggregationController, calculation_controller: ICalculationController,
                 cut_out_controller: ICutOutController, data_visualization_controller: IDataVisualizationController,
                 osm_data_controller: IOSMDataController):
        """
        This method creates a MainWindow that shows the GUI.

        Args:
            export_controller (export_controller.ExportController): Respective controller.
            category_controller (category_controller.CategoryController): Respective controller.
            project_controller (project_controller.ProjectController): Respective controller.
            settings_controller (settings_controller.SettingsController): Respective controller.
            aggregation_controller (aggregation_controller.AggregationController): Respective controller.
            calculation_controller (calculation_controller.CalculationController): Respective controller.
            cut_out_controller (cut_out_controller.CutOutController): Respective controller.
            data_visualization_controller (data_visualization_controller.DataVisualizationController):
                Respective controller.
            osm_data_controller (osm_data_controller.OSMDataController): Respective controller.
        """
        # Creating the mainWindow and setting its position, and making it resizable
        super().__init__()
        self.title(main_window_constants_i.MainWindowConstants.WINDOW_TITLE.value)

        # Selecting the primary Monitor to get accurate location for centering the window
        primary_monitor: Monitor | None = None
        monitor: Monitor
        for monitor in screeninfo.get_monitors():
            if monitor.is_primary:
                primary_monitor: Monitor = monitor
                break

        screen_height: int = primary_monitor.height
        screen_width: int = primary_monitor.width

        true_height: int = screen_height / 2 - main_window_constants_i.MainWindowConstants.MAIN_WINDOW_HEIGHT.value / 2
        true_width: int = screen_width / 2 - main_window_constants_i.MainWindowConstants.MAIN_WINDOW_WIDTH.value / 2

        self.geometry("%dx%d+%d+%d" % (main_window_constants_i.MainWindowConstants.MAIN_WINDOW_WIDTH.value,
                                       main_window_constants_i.MainWindowConstants.MAIN_WINDOW_HEIGHT.value,
                                       true_width, true_height))
        self.minsize(main_window_constants_i.MainWindowConstants.MAIN_WINDOW_WIDTH_MINIMUM.value,
                     main_window_constants_i.MainWindowConstants.MAIN_WINDOW_HEIGHT_MINIMUM.value)
        self.resizable(True, True)

        # Configuration of the grid for the Application
        self.grid_columnconfigure(0, weight=COLUM_WEIGHT)
        self.grid_rowconfigure(0, weight=TOP_ROW_WEIGHT)
        self.grid_rowconfigure(1, weight=MIDDLE_ROW_WEIGHT)
        self.grid_rowconfigure(2, weight=BOTTOM_ROW_WEIGHT)

        # Creating the StateManager
        from src.osm_configurator.view.states.state_manager import StateManager
        self._state_manager: StateManager = StateManager(self, export_controller, category_controller,
                                                         project_controller,
                                                         settings_controller, aggregation_controller,
                                                         calculation_controller,
                                                         cut_out_controller,
                                                         data_visualization_controller,
                                                         osm_data_controller)

    def start_main_window(self):
        """
        Starts the Loop of the MainWindow and therefor the whole View
        """
        self.wm_protocol("WM_DELETE_WINDOW", self._window_closed)
        self.mainloop()

    def change_state(self, last_state: State | None, new_state: State | None) -> bool:
        """
        This method changes from an old given state to a new given state to show on the MainWindow.

        Args:
            last_state (state.State): The state that needs to me removed from the MainWindow.
            new_state (state.State): The state that shall be shown by the MainWindow.

        Returns:
            bool: True, if the state change was successful, false if not.
        """
        # Making sure the new state is not None
        if new_state is None:
            return False

        # First making the last State invisible
        success: bool = False
        if last_state is not None:
            success: bool = self._make_invisible(last_state)
        else:
            # If Last state is none, there is no need to make anything invisible
            success: bool = True

        # If last State was successfully removed, then we try to make the new state visible
        if not success:
            return False
        else:
            success: bool = success and self._make_visible(new_state)

            return success

    def _make_visible(self, state: State | None) -> bool:
        """
        This method makes the given State visible on the MainWindow.

        Args:
            state (state.State): The state that shall be made visible.

        Returns:
            bool: True if the state could be made visible, false if not.
        """
        if state is None:
            # If there is no new state given, then you can't make anything visible
            return False

        positioned_frame: PositionedFrame
        for positioned_frame in state.get_active_frames():
            column: int = positioned_frame.get_column()
            row: int = positioned_frame.get_row()
            column_span: int = positioned_frame.get_colum_span()
            row_span: int = positioned_frame.get_row_span()
            sticky_type: str = positioned_frame.get_sticky()

            toplevel_frame: TopLevelFrame = positioned_frame.get_frame()

            toplevel_frame.master = self
            toplevel_frame.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, sticky=sticky_type)

        return True

    @staticmethod
    def _make_invisible(state: State | None) -> bool:
        """
        This method removes a given State from the MainWindow, so it cant be seen or interacted with anymore.

        Args:
            state (state.State): The state that shall not be visible anymore.

        Returns:
            bool: True, if the given state could be made invisible, false if not.
        """
        if state is None:
            # If there is nothing, then it is already invisible!
            return True

        positioned_frame: PositionedFrame
        for positioned_frame in state.get_active_frames():
            toplevel_frame: TopLevelFrame = positioned_frame.get_frame()
            toplevel_frame.grid_remove()

        return True

    def _window_closed(self):
        self.quit()
        self.destroy()
        sys.exit()
