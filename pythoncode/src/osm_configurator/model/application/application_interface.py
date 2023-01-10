from abc import ABC, abstractmethod


class ApplicationInterface(ABC):
    """
    The ApplicationInterface job, is to...

    """

    @abstractmethod
    def create_project(self, name, description, destination):
        """
        ...

        Args:
            name (str): The name of the new project.
            description (str): The description of the new project.
            destination (Path): The path, where the new project should be saved.

        Returns:
            bool: true when create_project completed successfully, otherwise false.
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
    def start_calculation(self):
        pass

    @abstractmethod
    def get_osm_data(self):
        pass

    @abstractmethod
    def set_osm_data(self, osm_data):
        pass

    @abstractmethod
    def get_all_aggregation_methods(self):
        pass

    @abstractmethod
    def is_aggregation_method_active(self, method):
        pass

    @abstractmethod
    def set_aggregation_method_active(self, method, active):
        pass

    @abstractmethod
    def get_cut_out_mode(self):
        pass

    @abstractmethod
    def set_cut_out_mode(self, new_cut_out_mode):
        pass

    @abstractmethod
    def set_cut_out_path(self, path):
        pass

    @abstractmethod
    def get_category(self, number):
        pass

    @abstractmethod
    def get_categories(self):
        pass

    @abstractmethod
    def add_category(self, new_category):
        pass

    @abstractmethod
    def remove_category(self, category):
        pass

    @abstractmethod
    def override_categories(self, category_input_list):
        pass

    @abstractmethod
    def merge_categories(self, category_input_list):
        pass
