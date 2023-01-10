from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState

class ActiveProject:

    """
    This class job is to manage the active project the user is working on.
    """

    def __init__(self, project_folder, is_newly_created):
        """
        Creates a new instance of the ActiveProject. In this process it creates the ConfigurationManager and also
        differentiate between the case that the project is new or loaded. In the case of an existing project it
        calls the ProjectLoader, otherwise it creates a new project.

        Args:
            project_folder (pathLib.Path): This is path pointing towards the folder, where the project is saved.
            is_newly_created (bool): This argument is true if the project is newly created, otherwise false.
        """
        pass

    def create(self, name, description):
        """
        This method creates a new project and adds a name and a description to it.

        Args:
            name (str): The name of the project.
            description (str): A description of the project.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        pass

    def get_last_step(self):
        """
        This method is there so that the user can continue working in the same phase in an existing project
        where he previously stopped.

        Returns:
            ConfigPhase: The last phase the user was working on.
        """
        pass

    def start_calculation(self):
        """
        This method is to start the calculation after the configuration is finished.

        Returns:
            CalculationState: True if the configuration is complete so the calculation can be started, otherwise false.
        """
        pass

    def get_project_path(self):
        """
        This method is to give back the path pointing towards the project folder.

        Returns:
            pathlib.Path: The path pointing towards the project folder.
        """
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