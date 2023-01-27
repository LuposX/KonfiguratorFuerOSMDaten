from __future__ import annotations

import customtkinter

POPUPSIZE = "400x200"
gloBla = 0


class YesNoPopUp(customtkinter.CTk):
    """
    This class creates PopUps, that will pop up in front of the GUI.
    This instance is a YesNoPopUp: It will provide a message, an 'OK' and an 'Cancel' button.
    Pressing a button will return the information back to the creating instance and close the PopUp.
    """

    def __init__(self, message):
        """
        This constructor will create an YesNoPopUp, that will show the given message, as well as an 'OK' and
        'Cancel' button. If one of the buttons is pressed or the PopUp closed, it will send a message back via the
        given function, what button had been pressed.
        If 'OK' has been pressed, the given function will be called with a boolean = true.
        If 'Cancel' has been pressed, or the PopUp was closed otherwise, the given function will be called with
        a boolean = false.

        Args:
            message (str): The message to be shown in the PopUp.
            func (typing.Callable): Function taking one Boolean and has no return for the PopUp to return a message
        """
        global gloBla
        gloBla = 0

        popup = super().__init__()
        self.geometry(POPUPSIZE)

        self.title("Alert")

        customtkinter.CTkLabel(popup, text=message) \
            .pack(side="top", fill="both", expand="True", padx=10, pady=10)

        customtkinter.CTkButton(self, text="Accept", command=combine_funcs(accept, self.destroy)) \
            .pack(side="bottom", padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="Cancel", command=combine_funcs(cancel, self.destroy)) \
            .pack(side="bottom", padx=10, pady=10)


def combine_funcs(*funcs):
    def inner_combined_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return inner_combined_funcs


def accept():
    global gloBla
    gloBla = 1


def cancel():
    global gloBla
    gloBla = 0
