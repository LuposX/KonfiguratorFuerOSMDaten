from __future__ import annotations

import customtkinter

from tkinter import filedialog

from pathlib import Path

import os

from definitions import PROJECT_DIR

import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.options_menu_constants as options_menu_constants_i
import src.osm_configurator.view.states.state as state_i
import src.osm_configurator.view.states.state_name_enum as state_name_enum_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
from src.osm_configurator.view.toplevelframes.lockable import Lockable


from PIL import Image

from typing import TYPE_CHECKING, List

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
BUTTON_WIDTH: Final = frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value / 9 - (2 * BUTTON_SPACE_TO_BORDER)

EXPORT_DISPLAYED_VALUE: Final = "Export"

EXPORT_PROJECT_STRING: Final = "Export Project"
EXPORT_CALCULATIONS_STRING: Final = "Export Calculation"
EXPORT_CONFIGURATION_STRING: Final = "Export Configurations"
EXPORT_CUT_OUT_MAP_STRING: Final = "Export Cut-Out-Map"


class ProjectHeadFrame(TopLevelFrame, Lockable):
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
        self._state_manager: StateManager = state_manager
        self._export_controller: IExportController = export_controller
        self._project_controller: IProjectController = project_controller
        # Locked and Frozen start as False
        self._locked: bool = False
        self._frozen: bool = False
        self._button_list: List[customtkinter.CTkButton] = []

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
        self.grid_columnconfigure(8, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Making all the Buttons
        # MainMenu Button
        self._main_menu_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self,
                                                                                  height=int(BUTTON_HEIGHT / 2),
                                                                                  width=BUTTON_WIDTH,
                                                                                  corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                  border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                  fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                  hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                  border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                  text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                  command=self._main_menu_button_pressed,
                                                                                  text="Main Menu")
        self._main_menu_button.grid(row=0, column=0, rowspan=1, columnspan=1)
        self._button_list.append(self._main_menu_button)

        # Save Button
        self._save_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=int(BUTTON_HEIGHT / 2),
                                                                             width=BUTTON_WIDTH,
                                                                             corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                             border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                             hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                             border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                             command=self._save_button_pressed,
                                                                             text="Save")
        self._save_button.grid(row=1, column=0, rowspan=1, columnspan=1)
        self._button_list.append(self._save_button)

        # Data Button
        self._data_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                             width=BUTTON_WIDTH,
                                                                             corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                             border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                             hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                             border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                             command=self._data_button_pressed,
                                                                             text="Data")
        self._data_button.grid(row=0, column=1, rowspan=2, columnspan=1)
        self._button_list.append(self._data_button)

        # Category Button
        self._category_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                                 width=BUTTON_WIDTH,
                                                                                 corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                 border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                 fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                 hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                 border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                 text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                 command=self._category_button_pressed,
                                                                                 text="Categories")
        self._category_button.grid(row=0, column=2, rowspan=2, columnspan=1)
        self._button_list.append(self._category_button)

        # Reduction Button
        self._reduction_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                                  width=BUTTON_WIDTH,
                                                                                  corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                  border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                  fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                  hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                  border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                  text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                  command=self._reduction_button_pressed,
                                                                                  text="Reduction")
        self._reduction_button.grid(row=0, column=3, rowspan=2, columnspan=1)
        self._button_list.append(self._reduction_button)

        # Attractivity Button
        self._attractivity_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                                     width=BUTTON_WIDTH,
                                                                                     corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                     border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                     fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                     hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                     border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                     text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                     command=self._attractivity_button_pressed,
                                                                                     text="Attractivity")
        self._attractivity_button.grid(row=0, column=4, rowspan=2, columnspan=1)
        self._button_list.append(self._attractivity_button)

        # Aggregation Button
        self._aggregation_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                                    width=BUTTON_WIDTH,
                                                                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                    command=self._attractivity_button_pressed,
                                                                                    text="Aggregation")
        self._aggregation_button.grid(row=0, column=5, rowspan=2, columnspan=1)
        self._button_list.append(self._aggregation_button)

        # Calculate Button
        self._calculate_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                                  width=BUTTON_WIDTH,
                                                                                  corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                  border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                  fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                  hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                  border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                  text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                  command=self._calculate_button_pressed,
                                                                                  text="Calculate")
        self._calculate_button.grid(row=0, column=6, rowspan=2, columnspan=1)
        self._button_list.append(self._calculate_button)

        # Export drop down menu
        self._export_values: List[str] = [EXPORT_PROJECT_STRING, EXPORT_CALCULATIONS_STRING,
                                          EXPORT_CONFIGURATION_STRING, EXPORT_CUT_OUT_MAP_STRING]
        self._export_drop_down_menu: customtkinter.CTkOptionMenu = customtkinter.CTkOptionMenu(
            master=self,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            corner_radius=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_CORNER_RADIUS.value,
            fg_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_FG_COLOR.value,
            button_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BUTTON_COLOR.value,
            button_hover_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BUTTON_HOVER_COLOR.value,
            dropdown_fg_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_FG_COLOR.value,
            dropdown_hover_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_HOVER_COLOR.value,
            dropdown_text_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_TEXT_COLOR.value,
            anchor=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_ANCHOR.value,
            hover=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_HOVER.value,
            state=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_STATE.value,
            values=self._export_values,
            command=self._export_drop_down_menu_edited)
        self._export_drop_down_menu.grid(row=0, column=7, rowspan=2, columnspan=1)

        # Options Button

        # Options Icon Used: https://www.flaticon.com/free-icon/cogwheel_44427
        options_icon: customtkinter.CTkImage = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(PROJECT_DIR, "data/view_icons/options.png")),
            dark_image=Image.open(os.path.join(PROJECT_DIR, "data/view_icons/options.png")),
            size=(ICON_HEIGHT_AND_WIDTH, ICON_HEIGHT_AND_WIDTH))

        self._options_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=BUTTON_HEIGHT,
                                                                                width=BUTTON_WIDTH,
                                                                                corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                                border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                                hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                                border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                                command=self._options_button_pressed,
                                                                                text="",
                                                                                image=options_icon)
        self._options_button.grid(row=0, column=8, rowspan=2, columnspan=1)
        self._button_list.append(self._options_button)

    def activate(self):
        # IF frame is activated, it is unlocked
        self.unlock()
        # And unfrozen
        self.unfreeze()

        # Activating all Buttons first, to prevent all buttons getting disabled eventually
        button: customtkinter.CTkButton
        for button in self._button_list:
            button.configure(state="normal",
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)

        # Activating the Export Drop Down Menu
        self._export_drop_down_menu.configure(state="normal")
        # Setting it to its displayed Value
        self._export_drop_down_menu.set(EXPORT_DISPLAYED_VALUE)

        # Disabling the button corrosponding to the current state
        self._disable_button_of_current_state()

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

    def _export_drop_down_menu_edited(self):

        # First checking what was selected
        # And then trying the export, if it fails an alertPopUp will be shown
        if self._export_drop_down_menu.get() == EXPORT_PROJECT_STRING:
            if not self._export_controller.export_project(self._file_dialog("Select Directory to export Project to")):
                alert_pop_up_i.AlertPopUp("Export of Project Failed!")
        elif self._export_drop_down_menu.get() == EXPORT_CALCULATIONS_STRING:
            if not self._export_controller.export_calculations(self._file_dialog("Select Directory to export Calculations to")):
                alert_pop_up_i.AlertPopUp("Export of Calculations Failed!")
        elif self._export_drop_down_menu.get() == EXPORT_CONFIGURATION_STRING:
            if not self._export_controller.export_configurations(self._file_dialog("Select Directory to export Configurations to")):
                alert_pop_up_i.AlertPopUp("Export of Configurations Failed!")
        elif self._export_drop_down_menu.get() == EXPORT_CUT_OUT_MAP_STRING:
            if not self._export_controller.export_cut_out_map(self._file_dialog("Select Directory to export Cut-Out-Map to")):
                alert_pop_up_i.AlertPopUp("Export of Cut-Out-Map Failed!")

        # No Else, since if none of those options where selected something that isn't an export option was selected

        # Also setting the Drop Down Menu again to its display value
        self._export_drop_down_menu.set(EXPORT_DISPLAYED_VALUE)

    def _file_dialog(self, title: str) -> Path:
        # Opens a file dialog, that will ask for a directory to save stuff in
        file_path: str = filedialog.askopenfilename(initialdir="/", title=title)
        # A Path will be returned
        return Path(file_path)

    def _save_project(self):
        # If the project can't be saved, an PopUp will pop up
        # No file type given since directories don't have that
        if not self._project_controller.save_project():
            alert_pop_up_i.AlertPopUp("Project could not be saved!")

    def _disable_button_of_current_state(self):
        # Getting what is the current state
        current_state: state_i.State = self._state_manager.get_state()
        current_state_name: state_name_enum_i.StateName = current_state.get_state_name()

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
                                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

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

    def lock(self) -> bool:
        if self._locked:
            return False
        else:
            # Disabling all Buttons, except the save Button!
            button: customtkinter.CTkButton
            for button in self._button_list:
                button.configure(state="disabled",
                                 fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                 text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)
            self._save_button.configure(state="normal",
                                        fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                                        text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)

            self._locked: bool = True
            return True

    def unlock(self) -> bool:
        if not self._locked:
            return False
        else:
            # Doing the activate method, because that excatly does what we want, it unlocks all buttons, except for the
            # one of the current state
            self.activate()
            self._locked: bool = False
            return True

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """

        if not self._frozen:
            self._main_menu_button.configure(state="disabled")
            self._save_button.configure(state="disabled")
            self._data_button.configure(state="disabled")
            self._category_button.configure(state="disabled")
            self._reduction_button.configure(state="disabled")
            self._attractivity_button.configure(state="disabled")
            self._aggregation_button.configure(state="disabled")
            self._calculate_button.configure(state="disabled")
            self._options_button.configure(state="disabled")
            self._export_drop_down_menu.configure(state="disabled")

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """

        if self._frozen:
            self._main_menu_button.configure(state="normal")
            self._save_button.configure(state="normal")
            self._data_button.configure(state="normal")
            self._category_button.configure(state="normal")
            self._reduction_button.configure(state="normal")
            self._attractivity_button.configure(state="normal")
            self._aggregation_button.configure(state="normal")
            self._calculate_button.configure(state="normal")
            self._options_button.configure(state="normal")
            self._export_drop_down_menu.configure(state="normal")

            # Disabling the button corrosponding to current state again
            self._disable_button_of_current_state()

            self._frozen: bool = False
