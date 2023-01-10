class ActiveProject:

    def __init__(self, project_folder, is_newly_created):
        """
        Creates a new instance of the ActiveProject.
        """
        pass

    def create(self, name, description):
        pass

    def get_last_step(self):
        pass

    def start_calculation(self):
        pass

    def get_project_path(self):
        pass

##From here on there are only methods to hand off
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