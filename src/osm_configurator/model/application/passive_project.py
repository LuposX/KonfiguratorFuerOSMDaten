from __future__ import annotations

from pathlib import Path


class PassiveProject:
    """
    This class job is to manage the passive projects. Those are the all projects shown in the Main Menu. Therefore,
    the class holds the name, description, last edit date and path of the projects.
    """

    def __init__(self, project_folder_path):
        """
        Creates a new instance of the PassiveProject.

        Args:
            project_folder_path (Path): The path to the project you want to make a PassiveProject on.
        """
        pass

    def get_name(self):
        """
        Gives back the name of the passive project.

        Returns:
            str: The name of the passive project.
        """
        pass

    def get_description(self):
        """
        Gives back the description of the passive project.

        Returns:
            str: The description of the passive project.
        """
        pass

    def get_edit_date(self):
        """
        Gives back the last edit date of the passive project.

        Returns:
            str: The last edit date of the passive project.
        """
        return "69/420/69"

    def get_project_folder_path(self):
        """
        Gives back the path pointing towards the passive project.

        Returns:
            pathlib.Path: The path pointing towards the passive project.
        """
        pass
