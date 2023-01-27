from __future__ import annotations

import customtkinter

POPUPSIZE = "400x200"  # Holds the size of the Popup


class AlertPopUp(customtkinter.CTk):
    """
    This class creates popups, that will pop up in front of the GUI.
    This instance is an Alert-PopUp. It provides a message and one 'OK' button, to close the PopUp again.
    """

    def __init__(self, message):
        """
        Creates a new popup showing the given message. If OK-Button is pressed the popup will close
        """
        popup = super().__init__()
        self.geometry(POPUPSIZE)

        self.title("Alert")

        label = customtkinter.CTkLabel(popup, text=message)
        label.pack(side="top", fill="both", expand="True", padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="OK", command=self.close_popup)
        self.button.pack(side="top", padx=40, pady=40)

    def close_popup(self):
        """
        Closes the calling popup
        """
        self.destroy()
