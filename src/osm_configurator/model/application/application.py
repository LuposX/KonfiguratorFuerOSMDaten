from __future__ import annotations

from src.osm_configurator.model.application.application_interface import IApplication


class Application(IApplication):
    __doc__ = IApplication.__doc__

    def __init__(self):
        """
        Creates a new instance of the application_interface.Application.
        """
        pass

    def get_passive_project_list(self):
        pass

    def get_key_recommendation(self, input):
        pass

    def create_project(self, name, description, destination):
        pass

    def load_project(self, path):
        pass

    def start_calculation(self, calculation_phase):
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

    def get_cut_out_path(self):
        pass

    def set_cut_out_path(self, path):
        pass

    def get_category(self, index):
        pass

    def get_categories(self):
        pass

    def create_category(self):
        pass

    def remove_category(self, category):
        pass

    def override_categories(self, new_category_list):
        pass

    def merge_categories(self, category_input_list):
        pass

    def create_map(self, cut_out):
        pass

    def create_boxplot(self, data):
        pass

    def get_location(self):
        pass

    def set_name(self, new_name):
        pass

    def get_name(self):
        pass

    def set_description(self, new_description):
        pass

    def get_description(self):
        pass

    def export_project(self, path):
        pass

    def export_configuration(self, path):
        pass

    def export_calculation(self, path):
        pass

    def export_map(self, path):
        pass
