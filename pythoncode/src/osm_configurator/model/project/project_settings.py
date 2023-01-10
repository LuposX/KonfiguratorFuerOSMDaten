class ProjectSettings:
    """
    This class saves all the different settings of a project and provides methods to view and change them.
    """

    def __init__(self, location, project_name, description):
        """
        This method creates a new ProjectSettings class with the given settings.

        Args:
            location (str): The location, the project is stored
            project_name (str): The name of the project
            description list[str]: A description of the project
        """
        pass

    def get_location(self):
        """
        This method returns the string, containing the project's location.

        Returns:
            str: The location of the project
        """
        pass

    def change_location(self, new_location):
        """
        This method changes the location where the project will be stored.

        Args:
            new_location (str): The new location for the project

        Returns:
            bool: true, if location change was successful, false else
        """
        pass

    def change_name(self, new_name):
        """
        This method changes the name of the project.

        Args:
            new_name (str): The new name of the project

        Returns:
            bool: true if change was successful, false else
        """
        pass

    def get_name(self):
        """
        This method returns the name of the project.

        Returns:
            str: name of the project
        """
        pass

    def change_description(self, new_description):
        """
        This method changes the description of the project.

        Args:
            new_description list[str]: The new description of the project

        Returns:
            bool: true if change successful, false else
        """
        pass

    def get_description(self):
        """
        This method returns the description of the project.

        Returns:
            list[str]: The description of the project
        """
        pass
