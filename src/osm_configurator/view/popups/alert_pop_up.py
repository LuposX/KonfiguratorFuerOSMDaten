from __future__ import annotations

import src.osm_configurator.view.states.view_constants as vc

import customtkinter

POPUPSIZE = vc.ViewConstants.POPUPSIZE.value  # Holds the size of the Popup


class AlertPopUp(customtkinter.CTk):
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
        popup = super().__init__()
        self.geometry(POPUPSIZE)

        self.title("Alert")

        label = customtkinter.CTkLabel(popup, text=message)
        label.pack(side="top", fill="both", expand="True", padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="OK", command=self.destroy)
        self.button.pack(side="top", padx=40, pady=40)
