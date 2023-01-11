import src.osm_configurator.model.application.application_interface
import pathlib
import matplotlib


class DataVisualizationController:
    """
    The DataVisualizationController is responsible for forwarding requests to the model, regarding the visualization of data from the model.
    """

    def __init__(self):
        """
        Creates a new instance of the DataVisualizationController, with a association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def generate_cut_out_map(self):
        """
        Generates a map of the data of the currently selected project.
        Using the cut-out file of the project, this function creates a map as a html-file of the project.
        The path to the html-file is returned.

        Returns:
            pathlib.Path: The path to the file, where the map is stored.
        """
        pass

    def get_calculation_visualization(self):
        """Generates a graphic that visualizes the results of the calculations of the currently selected project.

        Returns:
            matplotlib.axes.Axes: The resulting visualization as axes of the matplotlib library.
        """
        pass