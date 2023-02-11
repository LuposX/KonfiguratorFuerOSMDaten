from __future__ import annotations

import customtkinter

import src.osm_configurator.view.states.state_manager as state_manager_i
import src.osm_configurator.control.project_controller_interface
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
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
    from src.osm_configurator.control.project_controller_interface import IProjectController

# Final Variables
ICON_HEIGHT_AND_WIDTH: Final = 30
BUTTON_SPACE_TO_BORDER: Final = 5
BUTTON_HEIGHT: Final = frame_constants_i.FrameConstants.FOOT_FRAME_HEIGHT.value - (2 * BUTTON_SPACE_TO_BORDER)
# Buttons here are squared!
BUTTON_WIDTH: Final = BUTTON_HEIGHT


class ProjectFootFrame(TopLevelFrame, Lockable):
    """
    This frame shows two arrows on the bottom of the Window. The user can navigate the pipeline by going left or right.
    """

    def __init__(self, state_manager: StateManager, project_controller: IProjectController):
        """
        This method creates a ProjectFootFrame that lets the user navigate the pipeline by going left or right.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch states.
            project_controller (project_controller.ProjectController): Respective controller
        """
        # Starting with no master
        # Also setting other constants, based on what is in the constant enum
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.FOOT_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.FOOT_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.FOOT_FRAME_FG_COLOR.value)

        # Setting private Attributes
        self._state_manager = state_manager
        self._project_controller = project_controller
        self._locked: bool = None
        self._button_list: List[customtkinter.CTkButton] = []

        # Making the grid of the frame
        self.grid_columnconfigure(0, weight=1)
        # Middle Column shall be extra thick, to space out the buttons
        self.grid_columnconfigure(1, weight=100)
        self.grid_columnconfigure(2, weight=1)

        # There is only one row
        self.grid_rowconfigure(0, weight=1)

        # Making all the Buttons.
        # Left Arrow.
        # Arrow Used: https://www.flaticon.com/free-icon/right-arrow_626053?term=arrow+right&page=1&position=85&origin=search&related_id=626053
        left_arrow_icon: customtkinter.CTkImage = customtkinter.CTkImage(
            light_image=Image.open("../view_icons/arrow_left.png"),
            dark_image=Image.open("../view_icons/arrow_left.png"),
            size=(ICON_HEIGHT_AND_WIDTH, ICON_HEIGHT_AND_WIDTH))
        self._left_arrow: customtkinter.CTkButton = customtkinter.CTkButton(master=self, width=BUTTON_WIDTH,
                                                                            height=BUTTON_HEIGHT,
                                                                            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                            command=self._left_arrow_pressed,
                                                                            text="",
                                                                            image=left_arrow_icon)
        self._left_arrow.grid(row=0, column=0, rowspan=1, columnspan=1)
        self._button_list.append(self._left_arrow)

        # Right Arrow
        right_arrow_icon: customtkinter.CTkImage = customtkinter.CTkImage(
            light_image=Image.open("../view_icons/arrow_right.png"),
            dark_image=Image.open("../view_icons/arrow_right.png"),
            size=(ICON_HEIGHT_AND_WIDTH, ICON_HEIGHT_AND_WIDTH))
        self._right_arrow: customtkinter.CTkButton = customtkinter.CTkButton(master=self, width=BUTTON_WIDTH,
                                                                             height=BUTTON_HEIGHT,
                                                                             corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                             border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                             hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                             border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                             command=self._right_arrow_pressed,
                                                                             text="",
                                                                             image=right_arrow_icon)
        self._right_arrow.grid(row=0, column=2, rowspan=1, columnspan=1)
        self._button_list.append(self._right_arrow)

    def activate(self):
        # If Frame is activated, it is unlocked
        self._locked: bool = False

        # Getting what is the current state
        current_state: state_i.State = self._state_manager.get_state()

        # Activating all buttons, so they don't all end up beeing disabled
        button: customtkinter.CTkButton
        for button in self._button_list:
            button.configure(state="normal", fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE,
                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR)

        # If there is no default left, the left arrow is disabled
        if current_state.get_default_left() is None:
            self._left_arrow.configure(state="disabled",
                                       fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                       text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

        # If there is no default right, the right arrow is disabled
        if current_state.get_default_right() is None:
            self._right_arrow.configure(state="disabled",
                                        fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                        text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

    def _left_arrow_pressed(self):
        # Button activation and deactivation happens in activate()

        # If Frame gest changed, project gets saved
        self._save_project()

        if not self._state_manager.default_go_left():
            alert_pop_up_i.AlertPopUp("Frame change Failed!")

    def _right_arrow_pressed(self):
        # Button activation and deactivation happens in activate()

        # If Frame gest changed, project gets saved
        self._save_project()

        if not self._state_manager.default_go_right():
            alert_pop_up_i.AlertPopUp("Frame change Failed!")

    def _save_project(self):
        # If the project can't be saved, an PopUp will pop up
        if not self._project_controller.save_project():
            alert_pop_up_i.AlertPopUp("Project could not be saved!")

    def lock(self) -> bool:
        if self._locked:
            return False
        else:
            # Disabling all Buttons
            button: customtkinter.CTkButton
            for button in self._button_list:
                button.configure(state="disabled",
                                 fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED,
                                 text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

            self._locked: bool = True
            return True

    def unlock(self) -> bool:
        if not self._locked:
            return False
        else:
            # Activate does exactly what we want, it enables all buttons, except for those wo shall not be active,
            # since there is no default left or right
            self.activate()
            self._locked: bool = False
            return True
