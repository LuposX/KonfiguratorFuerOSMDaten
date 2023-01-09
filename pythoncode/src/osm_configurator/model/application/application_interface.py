from abc import ABC, abstractmethod


class ApplicationInterface(ABC):
    """
    The ApplicationInterface job, is to...

    """

    @abstractmethod
    def create_project(self, name, description):
        """
        ...

        Args:
            name (str): The name of the new project.
            description (str): The description of the new project.

        Returns:
            bool: true when create_project is valid, otherwise false.
        """
        pass

    @abstractmethod
    def load_project(self, path):
        """
        ...

        Args:
            path (str): The path of the new project.
        Returns:
            bool: true when loading the project is working, otherwise false.
        """
        pass

    @abstractmethod
    def load_external_project(self, location):
        """
        ...

        Args:
            location (str): The path of the new external project.
        Returns:
            bool: true when loading the external project is working, otherwise false.
        """
        pass
