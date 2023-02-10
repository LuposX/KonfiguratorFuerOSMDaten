from __future__ import annotations

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.pop_up_constants as pop_up_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i

# Other
from typing import TYPE_CHECKING
import customtkinter

if TYPE_CHECKING:
    import src.osm_configurator.view.constants.button_constants as button_constants_i
    import src.osm_configurator.view.constants.pop_up_constants as pop_up_constants_i
    import src.osm_configurator.view.constants.frame_constants as frame_constants_i
    import src.osm_configurator.view.constants.label_constants as label_constants_i


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
        # TODO: Adjust customtkinter attributes to the given enums

        self.func = func

        super().__init__(
            master=None,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value,
            title="Alert",
            geometry=pop_up_constants_i.PopUpConstants.POPUPSIZE.value
        )

        # Configuring the grid
        self.grid_columnconfigure(0, weight=1)  # Topbar: showing nothing
        self.grid_columnconfigure(1, weight=4)  # Shows the error message
        self.grid_columnconfigure(2, weight=2)  # Displays the buttons
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=1)

        customtkinter.CTkLabel(master=self,
                               text=message,
                               corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                               fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                               text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                               anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value, ) \
            .grid(row=1, column=1, rowspan=1, columnspan=1, padx=10, pady=10)

        self.accept_button = \
            customtkinter.CTkButton(master=self,
                                    text="Accept",
                                    command=combine_funcs(self.accept, self.destroy),
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                    ) \
            .grid(row=2, column=0, rowspan=1, columnspan=1, padx=10, pady=10)

        self.cancel_button = \
            customtkinter.CTkButton(master=self,
                                    text="Cancel",
                                    command=combine_funcs(self.cancel, self.destroy),
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                    ) \
            .grid(row=2, column=2, rowspan=1, columnspan=1, padx=10, pady=10)

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
