

class TagListPriorityFrame:
    """
    This Frame shows a List of Tags (Represented as Strings), that can be changed in order, to represent a Priority.
    The Higher an Entry is on the List, the Lower its Priority is.
    There will always be a DEFAULT Entry, that will have the lowest Priority, that can't be deleted.
    """

    def __init__(self, entries):
        """
        This Method will create a TagListPriorityFrame, that will show a List of the given Entries, ordered in
        Priority as the given List of Strings is.

        Args:
            entries list[str]: List of Strings, that shall be the Entries on the PriorityList.
        """
        pass

    def set_tag_list(self, entries):
        """
        Replaces all the Entries with the new given Entries, ordered in Priority as the given List of Strings is.

        Args:
            entries list[str]: The List of Strings, that shall be the Entries on the PriorityList.

        Returns:
            bool: True, if the replacement was succsessfull, false if not.
        """
        pass

    def get_tag_list(self):
        """
        Returns the current List of Entries, the PriorityList holds, ordered from lowest to highest in a List.

        Returns:
            list[str]: The Entry List of Strings on the List, ordered from the lowest Priority to highest.
        """
        pass
