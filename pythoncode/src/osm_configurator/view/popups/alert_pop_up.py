from __future__ import annotations

from customtkinter import CTkToplevel


class AlertPopUp(CTkToplevel):
    """
    This class creates popups, that will pop up in front of the GUI.
    This instance is an Alert-PopUp. It provides a message and one 'OK' button, to close the PopUp again.
    """

    def __init__(self, message):
        """
        This constructor will create an AlertPopUp. It will provide the given message and an 'OK' button to close
        the PopUp again.

        Args:
            message (str): The message that will be shown by the AlertPopUp.
        """
        pass


if __name__ == '__main__':
    AlertPopUp("du kek")