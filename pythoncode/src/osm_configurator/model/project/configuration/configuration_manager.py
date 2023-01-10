class ConfigurationManager:

    """
    This class job is to manage the configurations of the OSM data, aggregation, cut-out and categories.
    It also makes this information available to the calculation
    """

    def __init__(self, active_project_path):
        """
        Creates a new instance of the ConfigurationManager.

        Args:
            active_project_path (pathLib.Path): The path pointing towards the project folder.
        """
        pass

    def get_osm_data(self):
        pass

    def set_osm_data(self, osm_data):
        pass

    def get_all_aggregation_methods(self):
        pass

    def is_aggregation_method_active(self, method):
        pass

    def set_aggregation_method_active(self, method, active):
        pass

    def get_cut_out_mode(self):
        pass

    def set_cut_out_mode(self, new_cut_out_mode):
        pass

    def set_cut_out_path(self, path):
        pass

    def get_category(self, number):
        pass

    def get_categories(self):
        pass

    def add_category(self, new_category):
        pass

    def remove_category(self, category):
        pass

    def override_categories(self, category_input_list):
        pass

    def merge_categories(self, category_input_list):
        pass

    def get_active_project(self):
        """
        This method gives back the active project.

        Returns:
            pathlib.Path: The path pointing towards the current project folder.
        """
        pass

