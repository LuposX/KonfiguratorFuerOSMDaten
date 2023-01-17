import src.osm_configurator.model.application.application_interface
import src.osm_configurator.model.application.passive_project
import src.osm_configurator.model.project.config_phase_enum
import pathlib



class ProjectController:
    """
    The ProjectController is responsible for consistently forwarding requests regarding the project management
    to the model.
    It is responsible for managing, saving, loading, deleting and creating projects.
    """

    def __init__(self, model):
        """
        Creates a new instance of the ProjectController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_list_of_passive_projects(self):
        """
        Returns the list of (passive) projects, which are in the default project folder of the application.

        Returns:
            list[passive_project.PassiveProject]: The list of passive projects in the default project folder.
        """
        pass

    def load_project(self, path):
        """
        Loads a project
        All relevant data of a project are verified and loaded in memory. All coming project-referring calls will be directed to the given project.

        Args:
            path (pathlib.Path): The path to the project folder of the project, to be loaded.

        Returns:
            bool: True, if the project was loaded successfully; False if an error occurred, while trying to load the project. An error happens, if the path is not pointing to a valid project folder or if the project has corrupted files.
        """
        pass

    def create_project(self, name, description, destination):
        """
        Creates a new project with the given attributes and loads it.
        The model creates a new project folder at the given destination, all relevant files are generated and the project is loaded into memory.

        Args:
            name (str): The name of the to-be-created project, may not contain any line-breaks.
            description (str): The description of the to-be-created project. May contain line-breaks.
            destination (pathlib.Path): The path to the location, where the project-folder of the project should be created.

        Returns:
            bool: True, if the project was created successfully; False if an error occurred. An error occurs, if the name of the project is not valid, if the destination-path is not valid or if the destination-location is already occupied.
        """
        pass

    def delete_passive_project(self, project):
        """
        Deletes a project out of the default project folder.

        Args:
            project (passive_project.PassiveProject): The project that is going to be deleted.

        Returns:
            bool: True, if the (passive) project has been deleted successfully; False otherwise: The project does not exist or the application has not the right permissions to delete the project.
        """
        pass

    def save_project(self):
        """
        Saves the project.
        The currently selected project is stored on the disk. All progress made since the last saving are saved.

        Returns:
            bool: True, if the project was saved successfully; False if an error occurred, while attempting to save the project or when there is no project selected.
        """
        pass

    def set_current_config_phase(self, config_phase):
        """
        Stores the current configuration phase in the model.

        Args:
            config_phase (config_phase_enum.ConfigPhase): The new configuration phase.

        Returns:
            bool: True, if setting the configuration phase was successful; False, otherwise.
        """
        pass

    def get_current_config_phase(self):
        """
        Returns the configuration phase, that is currently stored in the model.

        Returns:
            config_phase_enum.ConfigPhase: The configuration phase, that is currently stored in the model.
        """
        pass

    def is_project_loaded(self):
        """
        Checks, whether any project is currently loaded/selected.

        Returns:
            bool: True, if a project is currently selected; False, otherwise.
        """
        pass
