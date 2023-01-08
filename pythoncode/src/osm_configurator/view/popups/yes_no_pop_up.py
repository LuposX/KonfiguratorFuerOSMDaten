from typing import Callable

class YesNoPopUp:
    """
    This Class creates PopUps, that will Pop Up in front of the GUI. This specific one is a YesNoPopUp, so it will
    provide a message and an 'OK' and an 'Cancel' Button. Pressing one of the Buttons will send a message back to the
    Creater of the PopUp, giving it the Answer on what had been pressed and closing den Pop Up afterwards.
    """

    def __init__(self, message, func):
        """
        This Constructor will create an YesNoPopUp, that will show the given message, as well as an 'OK' and
        'Cancel' Button. If one of the Buttons is pressed, or the PopUp Closed, it will send a message back, via the
        given function, what Button had been pressed.
        If 'OK' has been pressed, the given function will be called with a Boolean = true.
        If 'Cancel' has been pressed, or the PopUp was closed otherwise, the given function will be called with
        a Boolean = false.

        Args:
            message (str): The message to be shown in the PopUp.
            func (Callable): A Function that takes one Boolean and has no return, for the PopUp to send a message back.
        """
        pass