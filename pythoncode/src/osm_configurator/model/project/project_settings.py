import pathlib


class ProjectSettings:
    """
    This class saves all the different settings of a project and provides methods to view and change them.
    """

    def __init__(self, location, project_name, description):
        """
        This method creates a new ProjectSettings class with the given settings.

        Args:
            location (pathlib.Path): The location, the project is stored
            project_name (str): The name of the project
            description (str): A description of the project
        """
        pass

    def get_location(self):
        """
        Getter for the location of the Project on the disk.

        Returns:
            pathlib.Path: The location of the project
        """
        pass

    def set_location(self, new_location):
        """
        This method changes the location where the project will be stored.

        Args:
            new_location (pathlib.Path): The new location for the project

        Returns:
            bool: true, if location change was successful, false else
        """
        pass

    def set_name(self, new_name):
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

    def set_description(self, new_description):
        """
        This method changes the description of the project.

        Args:
            new_description (str): The new description of the project

        Returns:
            bool: true if change successful, false else
        """
        pass

    def get_description(self):
        """
        This method returns the description of the project.

        Returns:
            str: The description of the project
        """
        pass

    def set_calculation_phase_checkpoints_folder(self, folder_name: str):
        """
        This method is used to set the name of the folder in which the results will be saved.

        Args:
            folder_name (str): the name of the folder
        """
        pass

    def get_calculation_phase_checkpoints_folder(self) -> str:
        """
        This method is used to get the name of the folder in which the results will be saved.

        Returns:
            str: the name of the folder
        """
        pass

