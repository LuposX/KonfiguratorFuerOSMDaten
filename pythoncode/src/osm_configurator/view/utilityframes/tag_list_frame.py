


class TagListFrame:
    """
    This Frame shows a TextBox with a List of Strings, that can be edited.
    """

    def __init__(self, entries):
        """
        This Method Creates a TextBox with the given entries.

        Args:
            entries list[str]: A List of Strings, that will be shown on th TextBox.
        """
        pass

    def set_text_list(self, entries):
        """
        Throws away all the entries currently on the TextBox and replaces them, with the given Text.

        Args:
            entries list[str]: A List of Strings, that will be shown on the TextBox.

        Returns:
            bool: True if the replacement was succsessfull, false else.
        """
        pass

    def get_text_list(self):
        """
        This Method Returns a List of Strings of the current Entries on the TextBox.

        Returns:
            list[str]: List of Strings, that are the current Entries on the TextBox.
        """
        pass
