from __future__ import annotations


class TagListFrame:
    """
    This frame shows a textbox with a List of editable strings.
    """

    def __init__(self, entries):
        """
        This method creates a textbox with the given entries.

        Args:
            entries list[str]: A list of strings that will be written in the textbox.
        """
        pass

    def set_text_list(self, entries):
        """
        Replaces all shown textbox entries with the given text.

        Args:
            entries list[str]: A list of strings that will be shown on the textbox.

        Returns:
            bool: True if the replacement was successful, otherwise false.
        """
        pass

    def get_text_list(self):
        """
        This method returns a list of strings containing the current textbox entries.

        Returns:
            list[str]: List of strings containing the current textbox entries.
        """
        pass
