

class TagListPriorityFrame:
    """
    This Frame shows a List of Tags (Represented as Strings). The Tag-Priority can be changed with arrows.
    The Higher an Entry is on the List, the lower its Priority.
    A non-deletable DEFAULT-Entry will always have the lowest Priority.
    """

    def __init__(self, entries):
        """
        This Method will create a TagListPriorityFrame, showing a List of the given Entries, ordered like the Priorities.

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
            bool: True, if the replacement was successful, false if not.
        """
        pass

    def get_tag_list(self):
        """
        Returns the current List of Entries the PriorityList holds, ordered from lowest to highest.

        Returns:
            list[str]: The Entry List of Strings on the List, ordered from the lowest to highest Priority.
        """
        pass
