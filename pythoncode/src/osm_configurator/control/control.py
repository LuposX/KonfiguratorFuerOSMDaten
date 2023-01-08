from src.osm_configurator.control.control_interface import IControl


class Control(IControl):
    """
    This implementation of the interface IControl forwards all requests to other classes of this package.
    For details see the documentation of the corresponding functions.
    """
    __doc__ = IControl.__doc__ + __doc__

    def __init__(self):
        """Creates a new instance of Control, with a association to the model.

        Args:
            model (IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_list_of_passive_projects(self):
        pass

    def load_project(self, path):
        pass

    def create_project(self, name, description, destination):
        pass

    def delete_passive_project(self, project):
        pass

    def save_project(self):
        pass

    def set_current_config_phase(self, config_phase):
        pass

    def get_current_config_phase(self):
        pass

    def is_project_loaded(self):
        pass

    def set_osm_data_reference(self, path):
        pass

    def get_osm_data_reference(self):
        pass

    def get_cut_out_mode(self):
        pass

    def set_cut_out_mode(self, mode):
        pass

    def set_cut_out_reference(self, path):
        pass

    def get_cut_out_reference(self):
        pass

    def check_conflicts_in_category_configuration(self, path):
        pass

    def import_category_configuration(self, path):
        pass

    def get_list_of_categories(self):
        pass

    def create_category(self):
        pass

    def delete_category(self, category):
        pass

    def get_list_of_tag_recommendations(self, current_input):
        pass

    def get_attractivities_of_category(self, category):
        pass

    def get_aggregation_methods():
        pass

    def is_aggregation_method_active(self, method):
        pass

    def set_aggregation_method_active(self, method, active):
        pass

    def start_calculations(self, starting_phase):
        pass

    def get_calculation_state(self):
        pass

    def get_current_calculation_phase(self):
        pass

    def get_current_calculation_process(self):
        pass

    def cancel_calculations(self):
        pass

    def export_project(self, path):
        pass

    def export_calculations(self, path):
        pass

    def export_configurations(self, path):
        pass

    def get_project_name(self):
        pass

    def set_project_name(self, name):
        pass

    def get_project_description(self):
        pass

    def set_project_description(self, description):
        pass

    def get_project_default_folder(self):
        pass

    def set_project_default_folder(self, default_folder):
        pass

    def generate_cut_out_map(self):
        pass

    def get_calculation_visualization(self):
        pass