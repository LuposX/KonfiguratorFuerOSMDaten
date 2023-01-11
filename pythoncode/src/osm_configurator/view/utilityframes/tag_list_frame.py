
class TagListFrame:
    """
    This Frame shows a Textbox with a List of editable Strings.
    """

    def __init__(self, entries):
        """
        This Method Creates a TextBox with the given entries.

        Args:
            entries list[str]: A List of Strings, that will be written in the Textbox.
        """
        pass

    def set_text_list(self, entries):
        """
        Replaces all shown Textbox-Entries with the given Text.

        Args:
            entries list[str]: A List of Strings, that will be shown on the TextBox.

        Returns:
            bool: True if the replacement was successful, false else.
        """
        pass

    def get_text_list(self):
        """
        This Method Returns a List of Strings containing the current Textbox-Entries

        Returns:
            list[str]: List of Strings containing the current Textbox-Entries
        """
        pass
