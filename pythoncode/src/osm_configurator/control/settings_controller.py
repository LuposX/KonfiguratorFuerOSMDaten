import src.osm_configurator.model.application.application_interface
import pathlib


class SettingsController:
    """
    The SettingsController is responsible for forwarding requests to the model,
    regarding the settings of the application and the currently selected project.
    """

    def __init__(self, model):
        """
        Creates a new instance of the SettingsController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_project_name(self):
        """
        Gets the name of the currently selected project.

        Returns:
            str: The name of the project.
        """
        pass

    def set_project_name(self, name):
        """
        Sets the name of the currently selected project.

        Args:
            name (str): The new name of the project, may not contain line breaks.

        Returns:
            bool: True, if the name was changed successfully; False, if an error occurred: The name is not valid or no project was selected.
        """
        pass

    def get_project_description(self):
        """
        Gets the description of the currently selected project.

        Returns:
            str: The description of the project.
        """
        pass

    def set_project_description(self, description):
        """
        Sets the description of the currently selected project.

        Args:
            description (str): The new description of the project, may contain line breaks.

        Returns:
            bool: True, if the description was changed successfully; False, otherwise.
        """
        pass

    def get_project_default_folder(self):
        """
        Gets the project default folder.
        The project default folder is the folder where projects are stored by default.

        Returns:
            pathlib.Path: The path to the project default folder.
        """
        pass

    def set_project_default_folder(self, default_folder):
        """
        Sets the project default folder.
        The project default folder is the folder, where projects are stored by default.
        Projects of an old default folder will not be copied over.

        Args:
            default_folder (pathlib.Path): The path to the new project default folder.

        Returns:
            bool: True, if the default folder was set successfully; False if an error occurred: The path is not valid or occupied.
        """
        pass
