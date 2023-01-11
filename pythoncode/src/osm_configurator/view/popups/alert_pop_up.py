from customtkinter import CTkToplevel


class AlertPopUp(CTkToplevel):
    """
    This class creates PopUps, that will pop up in front of the GUI.
    This instance is an Alert-PopUp. It provides a message and one 'OK' Button, to close the PopUp again.
    """

    def __init__(self, message):
        """
        This Constructor will create an AlertPopUp. It will provide the given message and an 'OK' Button to close
        the PopUp again.

        Args:
            message (str): The message that will be shown by the AlertPopUp
        """
        pass
