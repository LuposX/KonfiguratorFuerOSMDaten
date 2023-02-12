from __future__ import annotations

import os
from pathlib import Path
import csv


class PassiveProject:
    """
    This class job is to manage the passive projects. Those are the all projects shown in the Main Menu. Therefore,
    the class holds the name, description, last edit date and path of the projects.
    """

    def __init__(self, settings_file):
        """
        Creates a new instance of the PassiveProject.

        Args:
            settings_file (Path): The settings file of to the project you want to make a PassiveProject on.
        """
        with open(settings_file, 'r') as f:
            reader = csv.reader(f)
            self.data = list(reader)

    def get_name(self) -> str:
        """
        Gives back the name of the passive project.

        Returns:
            str: The name of the passive project.
        """
        return self.data[0][1]

    def get_description(self) -> str:
        """
        Gives back the description of the passive project.

        Returns:
            str: The description of the passive project.
        """
        return self.data[1][1]

    def get_edit_date(self):
        """
        Gives back the last edit date of the passive project.

        Returns:
            str: The last edit date of the passive project.
        """
        return self.data[4][1]

    def get_project_folder_path(self) -> Path:
        """
        Gives back the path pointing towards the passive project.

        Returns:
            pathlib.Path: The path pointing towards the passive project.
        """
        return Path(self.data[2][1])
