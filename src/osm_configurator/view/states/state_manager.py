from __future__ import annotations

from typing import TYPE_CHECKING, List

import src.osm_configurator.view.states.state_name_enum
import src.osm_configurator.view.states.state

import src.osm_configurator.view.toplevelframes.main_menu_frame as bullshit


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
AGGREGATION_LINE: Final = 0
aggregation_colum = 0

main_menu_line = 0
main_menu_colum = 0

create_project_line = 0
create_project_colum = 0

project_head_frame_line = 0
project_head_frame_colum = 0

project_foot_frame_line = 0
project_foot_frame_colum = 0

attractivity_view_frame_line = 0
attractivity_view_frame_colum = 0

attractivity_edit_frame_line = 0
attractivity_edit_frame_colum = 0

calculation_frame_line = 0
calculation_frame_colum = 0

category_frame_line = 0
category_frame_colum = 0

data_frame_line = 0
data_frame_colum = 0

reduction_frame_line = 0
reduction_frame_colum = 0

settings_frame_line = 0
settings_frame_colum = 0


class StateManager:
    """
    This class manages the different states, that can be shown on a window.
    It knows what state is currently active and provides methods to change the state.
    """

    def __init__(self, main_window: MainWindow, export_controller: IExportController,
                 category_controller: ICategoryController, project_controller: IProjectController,
                 settings_controller: ISettingsController, aggregation_controller: IAggregationController,
                 application_controller: ApplicationController, calculation_controller: ICalculationController,
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
            application_controller (application_controller.ApplicationController): Respective controller
            calculation_controller (calculation_controller.CalculationController): Respective controller
            cut_out_controller (cut_out_controller.CutOutController): Respective controller
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller
            osm_data_controller (osm_data_controller.OSMDataController): Respective controller
        """
        self.__main_window = main_window
        self.__states = self.__create_states(export_controller, category_controller, project_controller,
                                             settings_controller, aggregation_controller, calculation_controller,
                                             cut_out_controller, data_visualization_controller, osm_data_controller)

        # At the beginning, there is no previous State
        self.__previous_state = None

        self.__current_state = None
        main_menu_state_name = StateName.MAIN_MENU
        for state in self.__states:
            if main_menu_state_name == state.get_state_name():
                self.__current_state = state
                break

        # Starting the Application in the MainMenu
        self.change_state(self.__current_state.get_state_name())

    def __create_states(self, export_controller: IExportController,
                        category_controller: ICategoryController, project_controller: IProjectController,
                        settings_controller: ISettingsController, aggregation_controller: IAggregationController,
                        calculation_controller: ICalculationController,
                        cut_out_controller: ICutOutController,
                        data_visualization_controller: IDataVisualizationController,
                        osm_data_controller: IOSMDataController) -> list[State]:
        all_states: list[State] = []

        # Main Menu State
        main_menu_frame = bullshit.MainMenuFrame(self, project_controller)
        positioned_main_menu_frame = PositionedFrame(main_menu_frame, main_menu_colum, main_menu_line)
        state_main_menu = State(list[positioned_main_menu_frame], StateName.MAIN_MENU, None, None)
        all_states.append(state_main_menu)

        # Create Project State
        create_project_frame = CreateProjectFrame(self, project_controller)
        positioned_create_project_frame = PositionedFrame(create_project_frame, create_project_colum,
                                                          create_project_line)
        state_create_project = State(list[positioned_create_project_frame], StateName.CREATE_PROJECT, None, None)
        all_states.append(state_create_project)

        # Project Head Frame
        project_head_frame = ProjectHeadFrame(self, export_controller, project_controller)
        positioned_project_head_frame = PositionedFrame(project_head_frame, project_head_frame_colum,
                                                        project_head_frame_line)

        # Project Foot Frame
        project_foot_frame = ProjectFootFrame(self, project_controller)
        positioned_project_foot_frame = PositionedFrame(project_foot_frame, project_foot_frame_colum,
                                                        project_foot_frame_line)

        # Aggregation Frame State
        aggregation_frame = AggregationFrame(self, aggregation_controller)
        positioned_aggregation_frame = PositionedFrame(aggregation_frame, aggregation_colum, AGGREGATION_LINE)
        state_aggregation_frame = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_aggregation_frame],
            StateName.AGGREGATION, StateName.ATTRACTIVITY_EDIT, StateName.CALCULATION)
        all_states.append(state_aggregation_frame)

        # Attractivity Frame States
        attractivity_edit_frame = AttractivityEditFrame(self, category_controller)
        positioned_attractivity_edit_frame = PositionedFrame(attractivity_edit_frame, attractivity_edit_frame_colum,
                                                             attractivity_edit_frame_line)
        attractivity_view_frame = AttractivityViewFrame(self, category_controller)
        positioned_attractivity_view_frame = PositionedFrame(attractivity_view_frame, attractivity_view_frame_colum,
                                                             attractivity_view_frame_line)
        state_attractivity_edit = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_attractivity_edit_frame],
            StateName.ATTRACTIVITY_EDIT, StateName.REDUCTION, StateName.AGGREGATION)
        all_states.append(state_attractivity_edit)
        state_attractivity_view = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_attractivity_view_frame],
            StateName.ATTRACTIVITY_VIEW, StateName.REDUCTION, StateName.AGGREGATION)
        all_states.append(state_attractivity_view)

        # Calculation Frame State
        calculation_frame = CalculationFrame(self, calculation_controller, data_visualization_controller)
        positioned_calcualtion_frame = PositionedFrame(calculation_frame, calculation_frame_colum,
                                                       calculation_frame_line)
        state_calculation_frame = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_calcualtion_frame],
            StateName.CALCULATION, StateName.AGGREGATION, None)
        all_states.append(state_calculation_frame)

        # Category Frame State
        category_frame = CategoryFrame(self, category_controller)
        positioned_category_frame = PositionedFrame(category_frame, category_frame_colum, category_frame_line)
        state_category_frame = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_category_frame],
            StateName.CATEGORY, StateName.DATA, StateName.REDUCTION)
        all_states.append(state_category_frame)

        # Data Frame State
        data_frame = DataFrame(self, data_visualization_controller, cut_out_controller, category_controller,
                               osm_data_controller)
        positioned_data_frame = PositionedFrame(data_frame, data_frame_colum, data_frame_line)
        state_data_frame = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_data_frame], StateName.DATA,
            None, StateName.CATEGORY)
        all_states.append(state_data_frame)

        # Reduction Frame State
        reduction_frame = ReductionFrame(self, category_controller)
        positioned_reduction_frame = PositionedFrame(reduction_frame, reduction_frame_colum, reduction_frame_line)
        state_reduction_frame = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_reduction_frame],
            StateName.REDUCTION, StateName.CATEGORY, StateName.ATTRACTIVITY_EDIT)
        all_states.append(state_reduction_frame)

        # Settings Frame State
        settings_frame = SettingsFrame(self, settings_controller)
        positioned_settings_frame = PositionedFrame(settings_frame, settings_frame_colum, settings_frame_line)
        state_settings_frame = State(
            list[positioned_project_head_frame, positioned_project_foot_frame, positioned_settings_frame],
            StateName.SETTINGS, None, None)
        all_states.append(state_settings_frame)

        return all_states

    def default_go_right(self) -> bool:
        """
        This method changes to the State that is the default_right state of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        if self.__current_state.get_default_right() is None:
            return False
        else:
            return self.change_state(self.__current_state.get_default_right())

    def default_go_left(self) -> bool:
        """
        This method changes to the state that is the default_left State of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        if self.__current_state.get_default_left() is None:
            return False
        else:
            return self.change_state(self.__current_state.get_default_left())

    def change_state(self, new_state: StateName) -> bool:
        """
        This method changes to the given state and deactivate the old one.

        Args:
            new_state (state_name_enum.StateName): The id of the new state that shall be activated.

        Returns:
            bool: True if state change was successful, false if not.
        """

        # First getting the actual next State, if there is no State with the given Name,
        # change_state failed and returns False
        next_state = None
        for state in self.__states:
            if state.get_state_name() == new_state:
                next_state = state
                break

        # If there is no next State, False is Returned
        # If there is a next State, then the state gets changed at the main_window and that will tell if
        # the State change actually worked
        if next_state is None:
            return False
        else:
            success = self.__main_window.change_state(self.__previous_state, next_state)
            if success:
                self.__current_state = next_state
            return success

    def get_state(self) -> State:
        """
        This method returns the currently active state.

        Returns:
            state.State: The currently active state.
        """
        return self.__current_state

    def close_program(self):
        """
        This method closes the program and shuts the whole application down.
        """
        pass
