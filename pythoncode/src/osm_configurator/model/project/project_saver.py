from src.osm_configurator.model.project.active_project import ActiveProject

class ProjectSaver:
    def __init__(self, active_project):
        """Creates a new instance of the ProjectSaver. 
        Therefore, it gets the current active project, which should be
        loaded if not newly created.

        Args:
            active_project (ActiveProject): The project the ProjectSaver shall load.
        """
        pass

    def save_project(self, path):
        """Stores all the configurations of the project.
        The informations about the configuration of the project are stored to the harddrive.
        Args:
            path (pathlib.Path): The path pointing towards the project folder. The data will be stored here

        Returns:
            bool: True, if the project was stored successfully, False, if an error accured.
        """
        pass