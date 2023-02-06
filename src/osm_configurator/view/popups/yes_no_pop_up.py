from __future__ import annotations

import src.osm_configurator.view.states.view_constants as vc

import customtkinter

POPUPSIZE = vc.ViewConstants.POPUPSIZE.value  # Holds the size of the Popup


class YesNoPopUp(customtkinter.CTk):
    """
    This class creates PopUps, that will pop up in front of the GUI.
    This instance is a YesNoPopUp: It will provide a message, an 'OK' and an 'Cancel' button.
    Pressing a button will return the information back to the creating instance and close the PopUp.
    """

    def __init__(self, message: str, func):
        """
        This constructor will create an YesNoPopUp, that will show the given message, as well as an 'Accept' and
        'Cancel' button. If one of the buttons is pressed or the PopUp closed, it will send a message back via the
        given function, what button had been pressed.
        If 'Accept' has been pressed, the given function will be called with a boolean = true.
        If 'Cancel' has been pressed, or the PopUp was closed otherwise, the given function will be called with
        a boolean = false.

        Args:
            message (str): The message to be shown in the PopUp.
            func (typing.Callable): Function taking one Boolean and has no return for the PopUp to return a message
        """
        self.func = func

        popup = super().__init__()
        self.geometry(POPUPSIZE)

        self.title("Alert")

        customtkinter.CTkLabel(popup, text=message) \
            .pack(side="top", fill="both", expand="True", padx=10, pady=10)

        customtkinter.CTkButton(self, text="Accept", command=combine_funcs(self.accept, self.destroy)) \
            .pack(side="bottom", padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="Cancel",
                                              command=combine_funcs(self.cancel, self.destroy)) \
            .pack(side="bottom", padx=10, pady=10)

    def accept(self):
        """
        Models the acceptance-process if a button is pressed.
        It will return "True" to the given function.
        """
        self.func(True)
        return True

    def cancel(self):
        """
        Models the cancelling-process if a button is pressed.
        It will return "False" to the given function.
        """
        self.func(False)
        return False


def combine_funcs(*funcs):
    """
    Will execute a list of functions in the given order.
    Args:
        *funcs: Contains the functions that will be executed
    """

    def inner_combined_funcs(*args, **kwargs):
        """
        Actually calls the functions
        Args:
            *args: contains the arguments of the given function
            *kwargs: Function will receive a dictionary of arguments, because the actual number is not
            clear before execution
        """
        for f in funcs:
            f(*args, **kwargs)

    return inner_combined_funcs

