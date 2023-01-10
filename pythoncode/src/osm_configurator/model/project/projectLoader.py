from src.osm_configurator.model.project.active_project import ActiveProject

class ProjectLoader:

    def __init__(self, active_project):
        """
        Creates a new instance of the ProjectLoader. Therefore, it gets the current active project, which should be
        loaded if not newly created.

        Args:
            active_project (ActiveProject): The project the ProjectLoader shall load.
        """
        pass

    def build_project(self, path):
        """
        This method is to build the given project. To do this it reads out the configurations and stores them in the
        ConfigurationManager.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.
        """
        pass