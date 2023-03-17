from __future__ import annotations

from pathlib import Path
import csv

READ: str = "r"

# The data loaded by this class is stored in csv or txt files
# The data in those files are stored as described below
SETTINGS_TABLE_FIRST_COLUMN: int = 0  # Describes the type of data stored in the following columns.
SETTINGS_TABLE_SECOND_COLUMN: int = 1  # In this column specific data is stored
SETTING_TABLE_FIRST_ROW: int = 0  # This row stores the name of the project
SETTING_TABLE_SECOND_ROW: int = 1  # This row stores the description of the project
SETTING_TABLE_THIRD_ROW: int = 2  # This row stores the location of the project
SETTING_TABLE_Forth_ROW: int = 3  # This row stores the last_edit_date of the project


class PassiveProject:
    """
    This class job is to manage the passive projects. Those are the all projects shown in the Main Menu. Therefore,
    the class holds the name, description, last edit date and path of the projects.
    """

    def __init__(self, settings_file: Path):
        """
        Creates a new instance of the PassiveProject.

        Args:
            settings_file (Path): The settings file of to the project you want to make a PassiveProject on.
        """
        with open(settings_file, READ, encoding="utf-8") as file:
            reader = csv.reader(file)
            self.data = list(reader)

    def get_name(self) -> str:
        """
        Gives back the name of the passive project.

        Returns:
            str: The name of the passive project.
        """
        return self.data[SETTING_TABLE_FIRST_ROW][SETTINGS_TABLE_SECOND_COLUMN]

    def get_description(self) -> str:
        """
        Gives back the description of the passive project.

        Returns:
            str: The description of the passive project.
        """
        return self.data[SETTING_TABLE_SECOND_ROW][SETTINGS_TABLE_SECOND_COLUMN]

    def get_project_folder_path(self) -> Path:
        """
        Gives back the path pointing towards the passive project.

        Returns:
            pathlib.Path: The path pointing towards the passive project.
        """
        return Path(self.data[SETTING_TABLE_THIRD_ROW][SETTINGS_TABLE_SECOND_COLUMN])

    def get_edit_date(self) -> str:
        """
        Gives back the last edit date of the passive project.

        Returns:
            str: The last edit date of the passive project.
        """
        return self.data[SETTING_TABLE_Forth_ROW][SETTINGS_TABLE_SECOND_COLUMN]
