from __future__ import annotations

import customtkinter

import src.osm_configurator.view.states.state_manager as state_manager_i
import src.osm_configurator.control.export_controller_interface
import src.osm_configurator.control.project_controller_interface
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.states.state as state_i
import src.osm_configurator.view.states.state_name_enum as state_name_enum_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from PIL import Image

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.export_controller_interface import IExportController
    from src.osm_configurator.control.project_controller_interface import IProjectController

# Final Constants
# Icons shall be square!
ICON_HEIGHT_AND_WIDTH: Final = 42

BUTTON_SPACE_TO_BORDER: Final = 10
BUTTON_HEIGHT: Final = frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value - (2 * BUTTON_SPACE_TO_BORDER)
BUTTON_WIDTH: Final = frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value / 8 - (2 * BUTTON_SPACE_TO_BORDER)


class ProjectHeadFrame(TopLevelFrame):
    """
    This frame shows the header pipeLine of the application, if a project is opened.
    Functionality the user can use:
    - Exit to the main menu
    - Save the project
    - Go to the settings
    - Change between different frames to edit configurations
    - Use exports

    This frame is always on the top of the window. Below it there will be presented a frame to edit some part of the project
    and below that one there will be a FootFrame.
    Exceptions are the MainMenu and the creation of a new project without this header.
    """

    def __init__(self, state_manager: StateManager, export_controller: IExportController,
                 project_controller: IProjectController):
        """
        This method creates a ProjectHeadFrame, letting the user navigate the pipeline and exit back to the main menu.
        The user can also open the settings, save the project or export the project.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            export_controller (export_controller.ExportController): Respective controller
            project_controller (project_controller.ProjectController): Respective controller
        """
        # Starting with no master
        # Also setting other constants, based on what is in the constant enum
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value)

        # Setting private Attributes
        self._state_manager = state_manager
        self._export_controller = export_controller
        self._project_controller = project_controller

        # Making the grid of the Frame
        # It consists of 8 Columns, one column for each Button, and two rows, to make MainMenu and Save in one Column
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Making all the Buttons
        # MainMenu Button
        self._main_menu_button = customtkinter.CTkButton(master=self, height=int(BUTTON_HEIGHT / 2), width=BUTTON_WIDTH,
                                                         corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                         border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                         fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                         hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                         border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                         text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                         command=self._main_menu_button_pressed,
                                                         text="Main Menu")
        self._main_menu_button.grid(row=0, column=0, rowspan=1, columnspan=1)

        # Save Button
        self._save_button = customtkinter.CTkButton(master=self, height=int(BUTTON_HEIGHT / 2), width=BUTTON_WIDTH,
                                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                    command=self._save_button_pressed,
                                                    text="Save")
        self._save_button.grid(row=1, column=0, rowspan=1, columnspan=1)

        # Data Button
        self._data_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                    command=self._data_button_pressed,
                                                    text="Data")
        self._data_button.grid(row=0, column=1, rowspan=2, columnspan=1)

        # Category Button
        self._category_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                        corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                        border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                        fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                        hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                        border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                        text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                        command=self._category_button_pressed,
                                                        text="Categories")
        self._category_button.grid(row=0, column=2, rowspan=2, columnspan=1)

        # Reduction Button
        self._reduction_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                         corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                         border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                         fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                         hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                         border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                         text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                         command=self._reduction_button_pressed,
                                                         text="Reduction")
        self._reduction_button.grid(row=0, column=3, rowspan=2, columnspan=1)

        # Attractivity Button
        self._attractivity_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                            command=self._attractivity_button_pressed,
                                                            text="Attractivity")
        self._attractivity_button.grid(row=0, column=4, rowspan=2, columnspan=1)

        # Aggregation Button
        self._aggregation_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                           corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                           border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                           fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                           hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                           border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                           text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                           command=self._attractivity_button_pressed,
                                                           text="Aggregation")
        self._aggregation_button.grid(row=0, column=5, rowspan=2, columnspan=1)

        # Calculate Button
        self._calculate_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                         corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                         border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                         fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                         hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                         border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                         text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                         command=self._calculate_button_pressed,
                                                         text="Calculate")
        self._calculate_button.grid(row=0, column=6, rowspan=2, columnspan=1)

        # Options Button

        # Options Icon Used: https://www.flaticon.com/free-icon/cogwheel_44427
        options_icon = customtkinter.CTkImage(light_image=Image.open("../view_icons/options.png"),
                                              dark_image=Image.open("../view_icons/options.png"),
                                              size=(ICON_HEIGHT_AND_WIDTH, ICON_HEIGHT_AND_WIDTH))
        self._options_button = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                       corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                       border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                       fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                       hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                       border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                       text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                       command=self._options_button_pressed,
                                                       text="",
                                                       image=options_icon)
        self._options_button.grid(row=0, column=7, rowspan=2, columnspan=1)

    def activate(self):
        # Getting what is the current state
        current_state: state_i.State = self._state_manager.get_state()
        current_state_name = current_state.get_state_name()

        # Activating all Buttons first, to prevent all buttons getting disabled eventually
        self._main_menu_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                         text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._save_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._data_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._category_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                        text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._reduction_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                         text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._attractivity_button.configure(state="normal",
                                            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._aggregation_button.configure(state="normal",
                                           fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                           text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._calculate_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                         text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)
        self._options_button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                       text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)

        # Now checking what state is active and disabling the corrosponding button
        match current_state_name:
            case state_name_enum_i.StateName.MAIN_MENU:
                raise RuntimeError("Can't be in MainMenu State with this Frame active!")

            case state_name_enum_i.StateName.CREATE_PROJECT:
                raise RuntimeError("Can't be in CreateProject State with this Frame active!")

            case state_name_enum_i.StateName.DATA:
                self._data_button.configure(state="disabled",
                                            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.CATEGORY:
                self._category_button.configure(state="disabled",
                                                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.REDUCTION:
                self._reduction_button.configure(state="disabled",
                                                 fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                                 text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.ATTRACTIVITY_EDIT:
                self._attractivity_button.configure(state="disabled",
                                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.ATTRACTIVITY_VIEW:
                self._attractivity_button.configure(state="disabled",
                                                    fg_color=button_constants_i.ViewConstants.BUTTON_FG_COLOR_DISABLED,
                                                    text_color=button_constants_i.ViewConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.AGGREGATION:
                self._aggregation_button.configure(state="disabled",
                                                   fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                                   text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.CALCULATION:
                self._calculate_button.configure(state="disabled",
                                                 fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                                 text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            case state_name_enum_i.StateName.SETTINGS:
                self._options_button.configure(state="disabled",
                                               fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                               text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

    def _main_menu_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before leaving a Project, it shall be saved!
        self._save_project()

        # Now changing to the MainMenu
        if not self._state_manager.change_state(state_name_enum_i.StateName.MAIN_MENU):
            alert_pop_up_i.AlertPopUp("Opening the Main Menu Failed!")

    def _save_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        self._save_project()

    def _data_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Data State
        if not self._state_manager.change_state(state_name_enum_i.StateName.DATA):
            alert_pop_up_i.AlertPopUp("Opening Data Failed!")

    def _category_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Category State
        if not self._state_manager.change_state(state_name_enum_i.StateName.CATEGORY):
            alert_pop_up_i.AlertPopUp("Opening Categories Failed!")

    def _reduction_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Reduction State
        if not self._state_manager.change_state(state_name_enum_i.StateName.REDUCTION):
            alert_pop_up_i.AlertPopUp("Opening Reduction Failed!")

    def _attractivity_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Attractivity_VIEW State
        if not self._state_manager.change_state(state_name_enum_i.StateName.ATTRACTIVITY_VIEW):
            alert_pop_up_i.AlertPopUp("Opening Attractivity Failed!")

    def _aggregation_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Aggregation State
        if not self._state_manager.change_state(state_name_enum_i.StateName.AGGREGATION):
            alert_pop_up_i.AlertPopUp("Opening Aggregation Failed!")

    def _calculate_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Calculate State
        if not self._state_manager.change_state(state_name_enum_i.StateName.CALCULATION):
            alert_pop_up_i.AlertPopUp("Opening Calculation Failed!")

    def _options_button_pressed(self):
        # Buttons don't get activated or disabled, because if we change back into a state with the HeadFrame
        # activate() will be called and to just that!

        # Before changing a state the application auto saves!
        self._save_project()

        # Changing to Option/Setting State
        if not self._state_manager.change_state(state_name_enum_i.StateName.SETTINGS):
            alert_pop_up_i.AlertPopUp("Opening Settings Failed!")

    def _save_project(self):
        # If the project can't be saved, an PopUp will pop up
        if not self._project_controller.save_project():
            alert_pop_up_i.AlertPopUp("Project could not be saved!")
