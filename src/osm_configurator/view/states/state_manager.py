from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.view.states.state_name_enum as state_name_enum_i
import src.osm_configurator.view.states.state as state_i
import src.osm_configurator.view.states.positioned_frame as positioned_frame_i
import src.osm_configurator.view.states.main_window as main_window_i

import src.osm_configurator.view.toplevelframes.top_level_frame as top_level_frame_i

import src.osm_configurator.view.toplevelframes.aggregation_frame as aggregation_frame_i
import src.osm_configurator.view.toplevelframes.main_menu_frame as main_menu_frame_i
import src.osm_configurator.view.toplevelframes.create_project_frame as create_project_frame_i
import src.osm_configurator.view.toplevelframes.project_head_frame as project_head_frame_i
import src.osm_configurator.view.toplevelframes.project_foot_frame as project_foot_frame_i
import src.osm_configurator.view.toplevelframes.attractivity_view_frame as attractivity_view_frame_i
import src.osm_configurator.view.toplevelframes.attractivity_edit_frame as attractivity_edit_frame_i
import src.osm_configurator.view.toplevelframes.calculation_frame as calculate_frame_i
import src.osm_configurator.view.toplevelframes.category_frame as category_frame_i
import src.osm_configurator.view.toplevelframes.data_frame as data_frame_i
import src.osm_configurator.view.toplevelframes.reduction_frame as reduction_frame_i
import src.osm_configurator.view.toplevelframes.settings_frame as settings_frame_i

import src.osm_configurator.view.toplevelframes.lockable as lockable_i

if TYPE_CHECKING:
    from typing import Final
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
    from src.osm_configurator.control.application_controller import ApplicationController
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.toplevelframes.aggregation_frame import AggregationFrame
    from src.osm_configurator.view.toplevelframes.main_menu_frame import MainMenuFrame
    from src.osm_configurator.view.toplevelframes.create_project_frame import CreateProjectFrame
    from src.osm_configurator.view.toplevelframes.project_head_frame import ProjectHeadFrame
    from src.osm_configurator.view.toplevelframes.project_foot_frame import ProjectFootFrame
    from src.osm_configurator.view.toplevelframes.attractivity_view_frame import AttractivityViewFrame
    from src.osm_configurator.view.toplevelframes.attractivity_edit_frame import AttractivityEditFrame
    from src.osm_configurator.view.toplevelframes.calculation_frame import CalculationFrame
    from src.osm_configurator.view.toplevelframes.category_frame import CategoryFrame
    from src.osm_configurator.view.toplevelframes.data_frame import DataFrame
    from src.osm_configurator.view.toplevelframes.reduction_frame import ReductionFrame
    from src.osm_configurator.view.toplevelframes.settings_frame import SettingsFrame

# Final Variables
FRAME_STICKY_TOP_LEFT: Final = "NW"
FRAME_STICKY_TOP_RIGHT: Final = "NE"
FRAME_STICKY_BOTTOM_LEFT: Final = "SW"
FRAME_STICKY_BOTTOM_RIGHT: Final = "SE"
FRAME_STICKY_WHOLE_CELL: Final = "NSEW"

AGGREGATION_ROW: Final = 1
AGGREGATION_COLUM: Final = 0
AGGREGATION_ROW_SPAN: Final = 1
AGGREGATION_COLUM_SPAN: Final = 1

MAIN_MENU_ROW: Final = 0
MAIN_MENU_COLUM: Final = 0
MAIN_MENU_ROW_SPAN: Final = 3
MAIN_MENU_COLUM_SPAN: Final = 1

CREATE_PROJECT_ROW: Final = 0
CREATE_PROJECT_COLUM: Final = 0
CREATE_PROJECT_ROW_SPAN: Final = 3
CREATE_PROJECT_COLUM_SPAN: Final = 1

PROJECT_HEAD_FRAME_ROW: Final = 0
PROJECT_HEAD_FRAME_COLUM: Final = 0
PROJECT_HEAD_FRAME_ROW_SPAN: Final = 1
PROJECT_HEAD_FRAME_COLUM_SPAN: Final = 1

PROJECT_FOOT_FRAME_ROW: Final = 2
PROJECT_FOOT_FRAME_COLUM: Final = 0
PROJECT_FOOT_FRAME_ROW_SPAN: Final = 1
PROJECT_FOOT_FRAME_COLUM_SPAN: Final = 1

ATTRACTIVITY_VIEW_FRAME_ROW: Final = 1
ATTRACTIVITY_VIEW_FRAME_COLUM: Final = 0
ATTRACTIVITY_VIEW_FRAME_ROW_SPAN: Final = 1
ATTRACTIVITY_VIEW_FRAME_COLUM_SPAN: Final = 1

ATTRACTIVITY_EDIT_FRAME_ROW: Final = 1
ATTRACTIVITY_EDIT_FRAME_COLUM: Final = 0
ATTRACTIVITY_EDIT_FRAME_ROW_SPAN: Final = 1
ATTRACTIVITY_EDIT_FRAME_COLUM_SPAN: Final = 1

CALCULATION_FRAME_ROW: Final = 1
CALCULATION_FRAME_COLUM: Final = 0
CALCULATION_FRAME_ROW_SPAN: Final = 1
CALCULATION_FRAME_COLUM_SPAN: Final = 1

CATEGORY_FRAME_ROW: Final = 1
CATEGORY_FRAME_COLUM: Final = 0
CATEGORY_FRAME_ROW_SPAN: Final = 1
CATEGORY_FRAME_COLUM_SPAN: Final = 1

DATA_FRAME_ROW: Final = 1
DATA_FRAME_COLUM: Final = 0
DATA_FRAME_ROW_SPAN: Final = 1
DATA_FRAME_COLUM_SPAN: Final = 1

REDUCTION_FRAME_ROW: Final = 1
REDUCTION_FRAME_COLUM: Final = 0
REDUCTION_FRAME_ROW_SPAN: Final = 1
REDUCTION_FRAME_COLUM_SPAN: Final = 1

SETTINGS_FRAME_ROW: Final = 1
SETTINGS_FRAME_COLUM: Final = 0
SETTINGS_FRAME_ROW_SPAN: Final = 1
SETTINGS_FRAME_COLUM_SPAN: Final = 1


class StateManager:
    """
    This class manages the different states, that can be shown on a window.
    It knows what state is currently active and provides methods to change the state.
    """

    def __init__(self, main_window: MainWindow, export_controller: IExportController,
                 category_controller: ICategoryController, project_controller: IProjectController,
                 settings_controller: ISettingsController, aggregation_controller: IAggregationController,
                 calculation_controller: ICalculationController,
                 cut_out_controller: ICutOutController, data_visualization_controller: IDataVisualizationController,
                 osm_data_controller: IOSMDataController):
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
            calculation_controller (calculation_controller.CalculationController): Respective controller
            cut_out_controller (cut_out_controller.CutOutController): Respective controller
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller
            osm_data_controller (osm_data_controller.OSMDataController): Respective controller
        """
        # The StateManager starts unlocked
        self._locked = False
        # Setting other attributes
        self._main_window = main_window
        self._states = self.__create_states(export_controller, category_controller, project_controller,
                                            settings_controller, aggregation_controller, calculation_controller,
                                            cut_out_controller, data_visualization_controller, osm_data_controller)

        # At the beginning, there is no previous State
        self._previous_state = None

        self._current_state = None
        main_menu_state_name = state_name_enum_i.StateName.MAIN_MENU
        for state in self._states:
            if main_menu_state_name == state.get_state_name():
                self._current_state = state
                break

        # Starting the Application in the MainMenu
        self.change_state(self._current_state.get_state_name())

    def __create_states(self, export_controller: IExportController,
                        category_controller: ICategoryController, project_controller: IProjectController,
                        settings_controller: ISettingsController, aggregation_controller: IAggregationController,
                        calculation_controller: ICalculationController,
                        cut_out_controller: ICutOutController,
                        data_visualization_controller: IDataVisualizationController,
                        osm_data_controller: IOSMDataController) -> list[State]:
        all_states: list[State] = []

        # Main Menu State
        main_menu_frame = main_menu_frame_i.MainMenuFrame(self, project_controller)
        positioned_main_menu_frame = positioned_frame_i.PositionedFrame(main_menu_frame, MAIN_MENU_COLUM,
                                                                        MAIN_MENU_ROW, MAIN_MENU_COLUM_SPAN,
                                                                        MAIN_MENU_ROW_SPAN, FRAME_STICKY_WHOLE_CELL)
        state_main_menu = State([positioned_main_menu_frame], state_name_enum_i.StateName.MAIN_MENU, None, None)
        all_states.append(state_main_menu)

        # Create Project State
        create_project_frame = create_project_frame_i.CreateProjectFrame(self, project_controller)
        positioned_create_project_frame = positioned_frame_i.PositionedFrame(create_project_frame, CREATE_PROJECT_COLUM,
                                                                             CREATE_PROJECT_ROW,
                                                                             CREATE_PROJECT_COLUM_SPAN,
                                                                             CREATE_PROJECT_ROW_SPAN,
                                                                             FRAME_STICKY_WHOLE_CELL)
        state_create_project = State([positioned_create_project_frame], state_name_enum_i.StateName.CREATE_PROJECT,
                                     None, None)
        all_states.append(state_create_project)

        # Project Head Frame
        project_head_frame = project_head_frame_i.ProjectHeadFrame(self, export_controller, project_controller)
        positioned_project_head_frame = positioned_frame_i.PositionedFrame(project_head_frame, PROJECT_HEAD_FRAME_COLUM,
                                                                           PROJECT_HEAD_FRAME_ROW,
                                                                           PROJECT_HEAD_FRAME_COLUM_SPAN,
                                                                           PROJECT_HEAD_FRAME_ROW_SPAN,
                                                                           FRAME_STICKY_WHOLE_CELL)

        # Project Foot Frame
        project_foot_frame = project_foot_frame_i.ProjectFootFrame(self, project_controller)
        positioned_project_foot_frame = positioned_frame_i.PositionedFrame(project_foot_frame, PROJECT_FOOT_FRAME_COLUM,
                                                                           PROJECT_FOOT_FRAME_ROW,
                                                                           PROJECT_FOOT_FRAME_COLUM_SPAN,
                                                                           PROJECT_FOOT_FRAME_ROW_SPAN,
                                                                           FRAME_STICKY_WHOLE_CELL)

        # Aggregation Frame State
        aggregation_frame = aggregation_frame_i.AggregationFrame(self, aggregation_controller)
        positioned_aggregation_frame = positioned_frame_i.PositionedFrame(aggregation_frame, AGGREGATION_COLUM,
                                                                          AGGREGATION_ROW, AGGREGATION_COLUM_SPAN,
                                                                          AGGREGATION_ROW_SPAN, FRAME_STICKY_WHOLE_CELL)
        state_aggregation_frame = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_aggregation_frame],
            state_name_enum_i.StateName.AGGREGATION, state_name_enum_i.StateName.ATTRACTIVITY_EDIT,
            state_name_enum_i.StateName.CALCULATION)
        all_states.append(state_aggregation_frame)

        # Attractivity Frame States
        attractivity_edit_frame = attractivity_edit_frame_i.AttractivityEditFrame(self, category_controller)
        positioned_attractivity_edit_frame = positioned_frame_i.PositionedFrame(attractivity_edit_frame,
                                                                                ATTRACTIVITY_EDIT_FRAME_COLUM,
                                                                                ATTRACTIVITY_EDIT_FRAME_ROW,
                                                                                ATTRACTIVITY_EDIT_FRAME_COLUM_SPAN,
                                                                                ATTRACTIVITY_EDIT_FRAME_ROW_SPAN,
                                                                                FRAME_STICKY_WHOLE_CELL)
        attractivity_view_frame = attractivity_view_frame_i.AttractivityViewFrame(self, category_controller)
        positioned_attractivity_view_frame = positioned_frame_i.PositionedFrame(attractivity_view_frame,
                                                                                ATTRACTIVITY_VIEW_FRAME_COLUM,
                                                                                ATTRACTIVITY_VIEW_FRAME_ROW,
                                                                                ATTRACTIVITY_VIEW_FRAME_COLUM_SPAN,
                                                                                ATTRACTIVITY_VIEW_FRAME_ROW_SPAN,
                                                                                FRAME_STICKY_WHOLE_CELL)
        state_attractivity_edit = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_attractivity_edit_frame],
            state_name_enum_i.StateName.ATTRACTIVITY_EDIT, state_name_enum_i.StateName.REDUCTION,
            state_name_enum_i.StateName.AGGREGATION)
        all_states.append(state_attractivity_edit)
        state_attractivity_view = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_attractivity_view_frame],
            state_name_enum_i.StateName.ATTRACTIVITY_VIEW, state_name_enum_i.StateName.REDUCTION,
            state_name_enum_i.StateName.AGGREGATION)
        all_states.append(state_attractivity_view)

        # Calculation Frame State
        calculation_frame = calculate_frame_i.CalculationFrame(self, calculation_controller,
                                                               data_visualization_controller)
        positioned_calcualtion_frame = positioned_frame_i.PositionedFrame(calculation_frame, CALCULATION_FRAME_COLUM,
                                                                          CALCULATION_FRAME_ROW,
                                                                          CALCULATION_FRAME_COLUM_SPAN,
                                                                          CALCULATION_FRAME_ROW_SPAN,
                                                                          FRAME_STICKY_WHOLE_CELL)
        state_calculation_frame = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_calcualtion_frame],
            state_name_enum_i.StateName.CALCULATION, state_name_enum_i.StateName.AGGREGATION, None)
        all_states.append(state_calculation_frame)

        # Category Frame State
        category_frame = category_frame_i.CategoryFrame(self, category_controller)
        positioned_category_frame = positioned_frame_i.PositionedFrame(category_frame, CATEGORY_FRAME_COLUM,
                                                                       CATEGORY_FRAME_ROW, CATEGORY_FRAME_COLUM_SPAN,
                                                                       CATEGORY_FRAME_ROW_SPAN, FRAME_STICKY_WHOLE_CELL)
        state_category_frame = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_category_frame],
            state_name_enum_i.StateName.CATEGORY, state_name_enum_i.StateName.DATA,
            state_name_enum_i.StateName.REDUCTION)
        all_states.append(state_category_frame)

        # Data Frame State
        data_frame = data_frame_i.DataFrame(self, data_visualization_controller, cut_out_controller,
                                            category_controller,
                                            osm_data_controller)
        positioned_data_frame = positioned_frame_i.PositionedFrame(data_frame, DATA_FRAME_COLUM, DATA_FRAME_ROW,
                                                                   DATA_FRAME_COLUM_SPAN, DATA_FRAME_ROW_SPAN,
                                                                   FRAME_STICKY_WHOLE_CELL)
        state_data_frame = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_data_frame],
            state_name_enum_i.StateName.DATA,
            None, state_name_enum_i.StateName.CATEGORY)
        all_states.append(state_data_frame)

        # Reduction Frame State
        reduction_frame = reduction_frame_i.ReductionFrame(self, category_controller)
        positioned_reduction_frame = positioned_frame_i.PositionedFrame(reduction_frame, REDUCTION_FRAME_COLUM,
                                                                        REDUCTION_FRAME_ROW, REDUCTION_FRAME_COLUM_SPAN,
                                                                        REDUCTION_FRAME_ROW_SPAN,
                                                                        FRAME_STICKY_WHOLE_CELL)
        state_reduction_frame = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_reduction_frame],
            state_name_enum_i.StateName.REDUCTION, state_name_enum_i.StateName.CATEGORY,
            state_name_enum_i.StateName.ATTRACTIVITY_EDIT)
        all_states.append(state_reduction_frame)

        # Settings Frame State
        settings_frame = settings_frame_i.SettingsFrame(self, settings_controller)
        positioned_settings_frame = positioned_frame_i.PositionedFrame(settings_frame, SETTINGS_FRAME_COLUM,
                                                                       SETTINGS_FRAME_ROW, SETTINGS_FRAME_COLUM_SPAN,
                                                                       SETTINGS_FRAME_ROW_SPAN, FRAME_STICKY_WHOLE_CELL)
        state_settings_frame = State(
            [positioned_project_head_frame, positioned_project_foot_frame, positioned_settings_frame],
            state_name_enum_i.StateName.SETTINGS, None, None)
        all_states.append(state_settings_frame)

        return all_states

    def default_go_right(self) -> bool:
        """
        This method changes to the State that is the default_right state of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        if self._current_state.get_default_right() is None:
            return False
        else:
            return self.change_state(self._current_state.get_default_right())

    def default_go_left(self) -> bool:
        """
        This method changes to the state that is the default_left State of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        if self._current_state.get_default_left() is None:
            return False
        else:
            return self.change_state(self._current_state.get_default_left())

    def change_state(self, new_state: StateName) -> bool:
        """
        This method changes to the given state and deactivate the old one.

        Args:
            new_state (state_name_enum.StateName): The id of the new state that shall be activated.

        Returns:
            bool: True if state change was successful, false if not.
        """

        # If the StateManager is locked in a State, the State can't be changed
        if self._locked:
            return False
        else:
            # First getting the actual next State, if there is no State with the given Name,
            # change_state failed and returns False
            next_state = None
            for state in self._states:
                if state.get_state_name() == new_state:
                    next_state = state
                    break

            # If there is no next State, False is Returned
            # If there is a next State, then the state gets changed at the main_window and that will tell if
            # the State change actually worked
            if next_state is None:
                return False
            else:
                success = self._main_window.change_state(self._previous_state, next_state)
                if success:
                    self._current_state = next_state
                return success

    def get_state(self) -> State:
        """
        This method returns the currently active state.

        Returns:
            state.State: The currently active state.
        """
        return self._current_state

    def lock_state(self):
        """
        This method locks the Application in the current State
        """
        # Locking himself up
        self._locked = True

        # Locking up all Frames, that can be locked
        for frame in self._current_state.get_active_frames():
            real_frame = frame.get_frame()
            if isinstance(real_frame, lockable_i.Lockable):
                real_frame.lock()

    def unlock_state(self):
        """
        This Method unlocks the Application to be able to change States again
        """
        # Unlocking himself
        self._locked = False

        # Unlocking all Frames, that can be unlocked
        for frame in self._current_state.get_active_frames():
            real_frame = frame.get_frame()
            if isinstance(real_frame, lockable_i.Lockable):
                real_frame.unlock()
