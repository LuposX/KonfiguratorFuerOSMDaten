from abc import ABC, abstractmethod
import src.osm_configurator.model.project.calculation.calculation_phase_enum
import src.osm_configurator.model.project.configuration.category


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
            destination (pathlib.Path): The path, where the new project should be saved.

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
            path (pathlib.Path): The path of the project, to be loaded.
        Returns:
            bool: True if loading the project is working, otherwise false.
        """
        pass

    @abstractmethod
    def start_calculation(self, calculation_phase):
        """
        This method is to start the calculation (after the configuration is finished).

        Args:
            calculation_phase (calculation_phase_enum.CalculationPhase): The calculation phase, where the calculation shall start.

        Returns:
            CalculationState: The calculation state where the calculation started. Can be an error state, so signify an error, that prevents the start of the calculation.
        """
        pass

    @abstractmethod
    def get_osm_data(self):
        """
        Gives back the path pointing towards the OSM data file.

        Returns:
            pathlib.Path: The path pointing towards the OSM data.
        """
        pass

    @abstractmethod
    def set_osm_data(self, osm_data):
        """
        Edits the path pointing towards the OSM data file.

        Args:
            osm_data (pathlib.Path): The new path towards the osm data file.

        Returns:
            bool: True if changing the path works, otherwise false.
        """
        pass

    @abstractmethod
    def get_all_aggregation_methods(self):
        """
        Gives back a List of all possible aggregation methods.

        Returns:
            list[aggregation_method_enum.AggregationMethod]: A list containing all aggregation methods.
        """
        pass

    @abstractmethod
    def is_aggregation_method_active(self, method):
        """
        Checks, if a given aggregation method is active.

        Args:
            method (aggregation_method_enum.AggregationMethod): The method, which is to be checked.

        Returns:
            bool: True if the aggregation method is active, otherwise false.
        """
        pass

    @abstractmethod
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

    @abstractmethod
    def get_cut_out_mode(self):
        """
        Gives back the used cut-out mode.

        Returns:
            cut_out_mode_enum.CutOutMode: The used cut-out mode.
        """
        pass

    @abstractmethod
    def set_cut_out_mode(self, new_cut_out_mode):
        """
        Changes the cut-out mode used during the reduction phase in the calculation.

        Args:
            new_cut_out_mode (cut_out_mode_enum.CutOutMode): The new cut-out mode for the calculation.

        Returns:
            bool: True if changing the cut-out mode works, otherwise false.
        """
        pass

    @abstractmethod
    def get_cut_out_path(self):
        """
        Gives back the path pointing towards the cut-out file.

        Returns:
            pathlib.Path: The path pointing towards the cut-out.
        """
        pass

    @abstractmethod
    def set_cut_out_path(self, path):
        """
        Changes the path pointing towards the cut-out file.

        Args:
            path (pathlib.Path): The new path, towards a cut-out file.

        Returns:
            bool: True if changing the cut-out path works, otherwise false.
        """
        pass

    @abstractmethod
    def get_category(self, index):
        """
        Gets a category based on the index.

        Args:
            index (int): Index in the categories-list, that will be returned.

        Returns:
            category.Category: The Category we wanted, NONE if the index is out of bounds of the list.
        """
        pass

    @abstractmethod
    def get_categories(self):
        """
        Getter for all the Categories.

        Returns:
            list[category.Category]: List of the chosen categories.
        """
        pass

    @abstractmethod
    def create_category(self):
        """
        Creates a new category, that will be empty.

        Returns:
            category.Category: The newly created category.
        """
        pass

    @abstractmethod
    def remove_category(self, category):
        """
        Removes the given category from the categories list, if element is inside the List.

        Args:
            category (category.Category): Category that will be removed.

        Returns:
            bool: True, if the element was removed correctly, else false.
        """
        pass

    @abstractmethod
    def override_categories(self, new_category_list):
        """
        Overwrites the list of categories with the given list, if both lists are not identical.

        Args:
            new_category_list (list[category.Category]): List of categories, that will overwrite the already existing list.

        Returns:
            bool: True, if the replacement was successful, else false.
        """
        pass

    @abstractmethod
    def merge_categories(self, category_input_list):
        """
        Merges the existing category list with the given list if both lists are not identical.
        If two categories conflict in their name, the newer category will be used.

        Args:
            category_input_list (list[category.Category]): New list of categories that will be merged into the existing list.

        Returns:
            bool: True, if the merging was successful, else False.
        """
        pass

    @abstractmethod
    def create_map(self, cut_out):
        """
        This method to create a map from to given cut-out.

        Args:
            cut_out (cut_out_configuration.CutOutConfiguration): The cut-out configuration from which the map should be created.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        pass

    @abstractmethod
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

    @abstractmethod
    def get_location(self):
        """
        Getter for the location of the active project on the disk.

        Returns:
            pathlib.Path: The location of the active project
        """
        pass

    def get_default_location(self):
        """
        Gives back the path pointing towards the project.

        Returns:
            Path: Returns the path of the default location.
        """
        pass

    def set_default_location(self, new_location):
        """
        Sets the default path pointing towards the project to a new Location.

        Args:
            new_location (pathlib.Path): The new Location, where the user wants to save new projects.
        """
        pass

    @abstractmethod
    def set_name(self, new_name):
        """
        This method changes the name of the project.

        Args:
            new_name (str): The new name of the project

        Returns:
            bool: true if change was successful, false else
        """
        pass

    @abstractmethod
    def get_name(self):
        """
        This method returns the name of the project.

        Returns:
            str: name of the project
        """
        pass

    @abstractmethod
    def set_description(self, new_description):
        """
        This method changes the description of the project.

        Args:
            new_description (str): The new description of the project

        Returns:
            bool: true if change successful, false else
        """
        pass

    @abstractmethod
    def get_description(self):
        """
        This method returns the description of the project.

        Returns:
            str: The description of the project
        """
        pass

    @abstractmethod
    def export_project(self, path):
        """
        Exports the whole project to the given path.

        Args:
            path (pathlib.Path): The path where the project shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
    def export_map(self, path):
        """
        Exports an HTML-Data with the map in it, to the given path.

        Args:
            path (Path): The path, where the map shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass
