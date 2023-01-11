import src.osm_configurator.model.project.configuration.cut_out_configuration
import seaborn


class DataVisualizer:
    """
    This class job is to visualize the cut-out file or data of the project.
    """

    def __init__(self):
        """
        Creates a new instance of the DataVisualizer.
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
            data (seaborn.boxplot): A plot of the data which we want to visualize.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        pass

    def _save_map(self, destination_path):
        """
        This method so to save the map after creating it at a given path.
        The map in an HTML file format.

        Args:
            destination_path (pathlib.Path): The path, where the map should be saved.

        Returns:
            bool: True if saving the map works, otherwise false.
        """
        pass
