from __future__ import annotations

from typing import Final

import src.osm_configurator.view.constants.pop_up_constants as pop_up_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.utility_methods as utility_methods_i

import customtkinter

POPUP_SIZE: Final = pop_up_constants_i.PopUpConstants.POPUP_SIZE.value  # The Size of the PopUp
MESSAGE_LENGTH: Final = 60
MESSAGE_ROWS: Final = 4
MESSAGE_DOTS: Final = False
MESSAGE_ROWS_UNLIMITED: Final = True
MESSAGE_WORD_BREAK: Final = True


class AlertPopUp(customtkinter.CTkToplevel):
    """
    This class creates popups, that will pop up in front of the GUI.
    This instance is an Alert-PopUp. It provides a message and one 'OK' button, to close the PopUp again.
    """

    def __init__(self, message: str):
        """
        Creates a new popup showing the given message. If OK-Button is pressed the popup will close
        Args:
            message (str): String containing the message that will be shown
        """
        super().__init__()
        self.geometry(vc.ViewConstants.POPUP_SIZE.value)

        self.title("Alert")

        self.lift()
        self.attributes("-topmost", True)
        self.focus_force()

        # Making the Grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        reformatted_message = utility_methods_i.reformat_string(
            message, MESSAGE_LENGTH, MESSAGE_ROWS, MESSAGE_DOTS,
            MESSAGE_ROWS_UNLIMITED, MESSAGE_WORD_BREAK)

        label = customtkinter.CTkLabel(
            master=self,
            text=reformatted_message,
            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR_POP_UP.value,
            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value)
        label.grid(row=0, column=0, rowspan=1, columnspan=1)

        self.button = customtkinter.CTkButton(self, text="OK", command=self.destroy,
                                              corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                              border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                              fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                              hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                              border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                              text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                              width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_SMALL.value,
                                              height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_SMALL.value)
        self.button.grid(row=1, column=0, rowspan=1, columnspan=1)
