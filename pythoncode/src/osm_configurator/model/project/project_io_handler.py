import src.osm_configurator.model.project.active_project
import pathlib


class ProjectIOHandler:
    """
    This class handles the I/O of a project.
    This includes:
    - loading a project from disk into memory that the user selected in the main menu
    - creating a project on the disk, if the user selected that
    """

    def __init__(self, active_project):
        """
        Creates a new instance of the ProjectLoader. Therefore, it gets the current active project, which should be
        loaded if not newly created.

        Args:
            active_project (active_project.ActiveProject): The project the ProjectLoader shall load.
        """
        pass

    def build_project(self, path):
        """
        This method is to build the given project. To do this it reads out the configurations and builts a folder
        structure on the disk.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        pass

    def load_project(self, path):
        """
        Loads a project in from the disk into the memory.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        pass
