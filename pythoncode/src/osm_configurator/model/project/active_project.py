import src.osm_configurator.model.project.config_phase_enum
import src.osm_configurator.model.project.calculation.calculation_state_enum
import pathlib


class ActiveProject:
    """
    This class job is to manage the active project the user is working on.
    Whereby an active project, a project is that got selected by the user in the project selected screen or
    created.
    """

    def __init__(self, project_folder, is_newly_created):
        """
        Creates a new instance of the ActiveProject. In this process it creates the ConfigurationManager and also
        differentiate between the case that the project is new or loaded. In the case of an existing project it
        calls the ProjectLoader, otherwise it creates a new project.

        Args:
            project_folder (pathlib.Path): This is path pointing towards the folder, where the project is saved.
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

    def get_osm_data(self):
        """
        Gives back the path pointing towards the OSM data file.

        Returns:
            pathlib.Path: The path pointing towards the OSM data.
        """
        pass

    def set_osm_data(self, osm_data):
        """
        Edits the path pointing towards the OSM data file.

        Args:
            osm_data (pathlib.Path): The new path towards the osm data file.

        Returns:
            bool: True if changing the path works, otherwise false.
        """
        pass

    def get_all_aggregation_methods(self):
        """
        Gives back a List of all possible aggregation methods.

        Returns:
            list[aggregation_method_enum.AggregationMethod]: A list containing all aggregation methods.
        """
        pass

    def is_aggregation_method_active(self, method):
        """
        Checks, if a given aggregation method is active.

        Args:
            method (aggregation_method_enum.AggregationMethod): The method, which is to be checked.

        Returns:
            bool: True if the aggregation method is active, otherwise false.
        """
        pass

    def set_aggregation_method_active(self, method, active):
        """
        Changes the aggregation method from active to inactive and vice versa. If an already active aggregation
        method should be activated, it stays active. The same applies to inactive aggregation methods, which should be deactivated.

        Args:
            method (aggregation_method_enum.AggregationMethod): The method, which state should be changed.
            active (bool): This is the new state of the aggregation method.

        Returns:
            bool: True if changing the state works, otherwise false.
        """
        pass

    def get_cut_out_mode(self):
        """
        Gives back the used cut-out mode.

        Returns:
            cut_out_mode_enum.CutOutMode: The used cut-out mode.
        """
        pass

    def set_cut_out_mode(self, new_cut_out_mode):
        """
        Changes the cut-out mode used during the reduction phase in the calculation.

        Args:
            new_cut_out_mode (cut_out_mode_enum.CutOutMode): The new cut-out mode for the calculation.

        Returns:
            bool: True if changing the cut-out mode works, otherwise false.
        """
        pass

    def get_cut_out_path(self):
        """
        Gives back the path pointing towards the cut-out file.

        Returns:
            pathlib.Path: The path pointing towards the cut-out.
        """
        pass

    def set_cut_out_path(self, path):
        """
        Changes the path pointing towards the cut-out file.

        Args:
            path (pathlib.Path): The new path.

        Returns:
            bool: True if changing the cut-out path works, otherwise false.
        """
        pass

    def get_category(self, index):
        """
        Gets a category based on the index.

        Args:
            index (int): Index in the categories-list, that will be returned.

        Returns:
            category.Category: The Category we wanted.
        """
        pass

    def get_categories(self):
        """
        Getter for all the Categories.

        Returns:
            list[Category]: List of the chosen categories.
        """
        pass

    def create_category(self, new_category):
        """
        Adds a new category to the list of categories, if element does not exist already.

        Args:
            new_category (Category): Category, that will be added to the list.

        Returns:
            bool: True, if the category was added successfully, else False.
        """
        pass

    def remove_category(self, category):
        """
        Removes the given category from the categories list, if element is inside the List.

        Args:
            category (Category): Category that will be removed.

        Returns:
            bool: True, if the element was removed correctly, else false.
        """
        pass

    def override_categories(self, new_category_list):
        """
        Overwrites the list of categories with the given list, if both lists are not identical.

        Args:
            new_category_list (list[Categories]): List of categories, that will overwrite the already existing list.

        Returns:
            bool: True, if the replacement was successful, else False.
        """
        pass

    def merge_categories(self, category_input_list):
        """
        Merges the existing category list with the given list if both lists are not identical.

        Args:
            category_input_list (list[Category]): New list of categories that will be merged into the existing list.

        Returns:
            bool: True, if the merging was successful, else False.
        """
        pass

    def create_map(self, cut_out):
        """
        This method to create a map from to given cut-out.

        Args:
            cut_out (cut_out_configuration.CutOutConfiguration): The cut-out configuration from which the map should be created.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        pass

    def create_boxplot(self, data):
        """
        This method is to visualize the data by creating a boxplot.
        It is used to visualize the calculated end result via a boxplot.

        Args:
            data (matplotlib.axes.Axes): A plot of the data which we want to visualize.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        pass

    def get_location(self):
        """
        Getter for the location of the Project on the disk.

        Returns:
            pathlib.Path: The location of the project
        """
        pass

    def set_location(self, new_location):
        """
        This method changes the location where the project will be stored.

        Args:
            new_location (pathlib.Path): The new location for the project

        Returns:
            bool: true, if location change was successful, false else
        """
        pass

    def set_name(self, new_name):
        """
        This method changes the name of the project.

        Args:
            new_name (str): The new name of the project

        Returns:
            bool: true if change was successful, false else
        """
        pass

    def get_name(self):
        """
        This method returns the name of the project.

        Returns:
            str: name of the project
        """
        pass

    def set_description(self, new_description):
        """
        This method changes the description of the project.

        Args:
            new_description (str): The new description of the project

        Returns:
            bool: true if change successful, false else
        """
        pass

    def get_description(self):
        """
        This method returns the description of the project.

        Returns:
            str: The description of the project
        """
        pass

    def export_project(self, path):
        """
        Exports the whole project to the given path.

        Args:
            path (pathlib.Path): The path where the project shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    def export_configuration(self, path):
        """
        Exports the configuration to the given path. More specific, exports all the categories and their configurations,
        to the given path.

        Args:
            path (pathlib.Path): The path where the configurations shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    def export_calculation(self, path):
        """
        Exports the results of the calculation to the given path.
        Whereby the calculation are a folder with all the different results from each
        calculation step in it.

        Args:
            path (Path): The path where the results of the calculation shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    def export_map(self, path):
        """
        Exports an HTML-Data with the map in it, to the given path.

        Args:
            path (Path): The path, where the map shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass
