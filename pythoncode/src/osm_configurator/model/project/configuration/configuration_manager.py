import pathlib


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

    def create_category(self):
        """
        Creates a new category, that will be empty.

        Returns:
            category.Category: The newly created category.
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

    def get_active_project(self):
        """
        This method gives back the active project.

        Returns:
            pathlib.Path: The path pointing towards the current project folder.
        """
        pass

    def get_is_data_downloaded(self):
        """
        Gives back if data in DownloadData is downloaded.

        Returns:
            bool: True if data is downloaded, otherwise false.
        """

