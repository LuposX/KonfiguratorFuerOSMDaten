from abc import ABC, abstractmethod


class IApplication(ABC):
    """
    The IApplication job, is to provide the functionality the application needs.
    """

    @abstractmethod
    def create_project(self, name, description, destination):
        """
        This method creates a new project with a name, a description and saves it at a given destination.

        Args:
            name (str): The name of the new project.
            description (str): The description of the new project.
            destination (Path): The path, where the new project should be saved.

        Returns:
            bool: True if create_project completed successfully, otherwise false.
        """
        pass

    @abstractmethod
    def load_project(self, path):
        """
        This method loads an existing project. This project can be internal or external ones. The path is pointing
        towards the folder, where the project is saved.

        Args:
            path (str): The path of the new project.
        Returns:
            bool: True if loading the project is working, otherwise false.
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

    @abstractmethod
    def create_map(self, cut_out):
        pass

    @abstractmethod
    def create_boxplot(self, data):
        pass

    @abstractmethod
    def get_location(self):
        pass

    @abstractmethod
    def change_location(self, new_location):
        pass

    @abstractmethod
    def change_name(self, new_name):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def change_description(self, new_description):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def export_project(self, path):
        pass

    @abstractmethod
    def export_configuration(self, path):
        pass

    @abstractmethod
    def export_calculation(self, path):
        pass

    @abstractmethod
    def export_map(self, path):
        pass

