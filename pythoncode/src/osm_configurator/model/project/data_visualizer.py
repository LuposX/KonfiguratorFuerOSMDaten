from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration

class DataVisualizer:

    """
    This class job is to visualize the cut-out or data of the project.
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
            cut_out (CutOutConfiguration): The cut-out from which the map should be created.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        pass

    def create_boxplot(self, data):
        """
        This method is to visualize the data by creating a boxplot.

        Args:
            data (DataFrame): The data, which should be visualized.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        pass

    def _save_map(self, destination_path):
        """
        This method so to save the map after creating it at a given path.

        Args:
            destination_path (pathlib.Path): The path, where the map should be saved.

        Returns:
            bool: True if saving the map works, otherwise false.
        """
        pass