from __future__ import annotations

from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

# Constants
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.text_box_constants as text_box_constants_i

# Other
import customtkinter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.activatable import Activatable


class SettingsProjectFrame(TopLevelFrame, Activatable):
    """
    This frame shows the current project settings.
    """

    def __init__(self, parent, settings_controller: ISettingsController):
        """
        This method creates a SettingsProjectFrame, showing the current project settings.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            settings_controller (settings_controller.SettingsController): Respective controller.
        """
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.FOOT_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.FOOT_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.FOOT_FRAME_FG_COLOR.value)

        self._parent = parent
        self._settings_controller: ISettingsController = settings_controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=3)

        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)

        self._project_name: str = self._settings_controller.get_project_name()
        self._project_description: str = self._settings_controller.get_project_description()

        self.header: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(master=self,
                                   text="Current Project",
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value)
        self.header.grid(column=0, row=0, rowspan=1, columnspan=1)

        self.project_name_box: customtkinter.CTkTextbox = \
            customtkinter.CTkTextbox(master=self,
                                     corner_radius=text_box_constants_i.TextBoxConstants.TEXT_BOX_CORNER_RADIUS.value,
                                     border_width=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_WITH.value,
                                     fg_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_FG_COLOR.value,
                                     border_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_COLOR.value,
                                     text_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_TEXT_COLOR.value
                                     )
        self.project_name_box.insert(1.0, str(self._project_name))
        self.project_name_box.grid(column=1, row=0, rowspan=1, columnspan=1)

        self.change_project_name_button: customtkinter.CTkButton = \
            customtkinter.CTkButton(master=self,
                                    text="Change Project Name",
                                    command=self.__change_project_name,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value)
        self.change_project_name_button.grid(column=2, row=0, rowspan=1, columnspan=1)

        self.description_box: customtkinter.CTkTextbox = \
            customtkinter.CTkTextbox(master=self,
                                     corner_radius=text_box_constants_i.TextBoxConstants.TEXT_BOX_CORNER_RADIUS.value,
                                     border_width=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_WITH.value,
                                     fg_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_FG_COLOR.value,
                                     border_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_COLOR.value,
                                     text_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_TEXT_COLOR.value,
                                     )
        self.description_box.insert(1.0, str(self._project_description))
        self.description_box.grid(column=3, row=0, rowspan=1, columnspan=1)

        self.change_description_button: customtkinter.CTkButton = \
            customtkinter.CTkButton(master=self,
                                    text="Change Project Description",
                                    command=self.__change_project_description,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value)
        self.change_project_name_button.grid(column=3, row=1, rowspan=1, columnspan=1)

    def activate(self) -> bool:
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        self._project_name = ISettingsController.get_project_name(self._settings_controller)
        self._project_description = ISettingsController.get_project_description(self._settings_controller)

        if self._project_name != "":
            return True
        return False

    def __change_project_name(self):
        """
        Changes the current project name to whatever was entered in the textbox
        Reads the textbox-entry and changes the name by calling the given settings-controller
        """
        textbox_input = self.project_name_box.get("0.0", "end")  # Read everything submitted to the textbox
        if textbox_input == "":
            #  invalid (no) name => show popup and reload page
            popup = AlertPopUp("Name must be at least one character long")
            popup.mainloop()  # show popup
            self.activate()  # reload page
            return
        self._project_name = textbox_input
        ISettingsController.set_project_name(self._settings_controller, textbox_input)

    def __change_project_description(self):
        """
        Changes the current project description to whatever was entered in the according textbox
        Reads the textbox-entry and changes the description by calling the given settings-controller
        """
        textbox_input = self.description_box.get("0.0", "end")
        #  no null-checks required since description is optional
        self._project_description = textbox_input
        ISettingsController.set_project_description(self._settings_controller, textbox_input)
