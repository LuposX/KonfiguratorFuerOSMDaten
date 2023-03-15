from __future__ import annotations

import src.osm_configurator.view.states.view_constants as vc

import customtkinter


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

        label = customtkinter.CTkLabel(self, text=message)
        label.pack(side="top", fill="both", expand="True", padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="OK", command=self.destroy)
        self.button.pack(side="top", padx=40, pady=40)
