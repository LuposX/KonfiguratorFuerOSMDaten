from __future__ import annotations

from typing import Callable

from customtkinter import CTkToplevel


class YesNoPopUp(CTkToplevel):
    """
    This class creates PopUps, that will pop up in front of the GUI.
    This instance is a YesNoPopUp: It will provide a message, an 'OK' and an 'Cancel' button.
    Pressing a button will return the information back to the creating instance and close the PopUp.
    """

    def __init__(self, message, func):
        """
        This constructor will create an YesNoPopUp, that will show the given message, as well as an 'OK' and
        'Cancel' button. If one of the buttons is pressed or the PopUp closed, it will send a message back via the
        given function, what button had been pressed.
        If 'OK' has been pressed, the given function will be called with a boolean = true.
        If 'Cancel' has been pressed, or the PopUp was closed otherwise, the given function will be called with
        a boolean = false.

        Args:
            message (str): The message to be shown in the PopUp.
            func (typing.Callable): A Function that takes one Boolean and has no return, for the PopUp to send a message back.
        """
        super.__init__(message, func)

    def close_pop_up(self):
        self.destroy()