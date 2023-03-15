from __future__ import annotations

import src.osm_configurator.view.constants.pop_up_constants as pop_up_constants_i

import customtkinter

POPUP_SIZE = pop_up_constants_i.PopUpConstants.POPUP_SIZE.value  # The Size of the PopUp


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
        self.geometry(POPUP_SIZE)

        self.title("Alert")

        self.lift()
        self.attributes("-topmost", True)
        self.focus_force()

        label = customtkinter.CTkLabel(self, text=message)
        label.pack(side="top", fill="both", expand="True", padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="OK", command=self.destroy)
        self.button.pack(side="top", padx=40, pady=40)
