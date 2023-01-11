

class TagListPriorityFrame:
    """
    This frame shows a list of tags (represented as strings). The tag-priority can be changed with arrows.
    The higher an entry is on the list, the lower its priority.
    A non-deletable DEFAULT-entry will always have the lowest priority.
    """

    def __init__(self, entries):
        """
        This method will create a TagListPriorityFrame, showing a list of the given entries, ordered like the priorities.

        Args:
            entries list[str]: List of strings, that shall be the entries on the priority list.
        """
        pass

    def set_tag_list(self, entries):
        """
        Replaces all the entries with the new given entries, ordered in priority as the given List of strings is.

        Args:
            entries list[str]: The list of strings, that shall be the entries on the priority list.

        Returns:
            bool: True, if the replacement was successful, false if not.
        """
        pass

    def get_tag_list(self):
        """
        Returns the current list of entries the priority list holds, ordered from lowest to highest.

        Returns:
            list[str]: The entry list of strings on the list, ordered from the lowest to highest priority.
        """
        pass
