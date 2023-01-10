import src.osm_configurator.model.application.application_interface
import src.osm_configurator.model.project.configuration.cut_out_mode_enum
import pathlib


class CutOutController:
    """The CutOutController is responsible for consistently forwarding requests to the model, concerning the cut-out filter of the currently selected project.
    """

    def __init__(self):
        """Creates a new instance of the CutOutController, with a association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_cut_out_mode(self):
        """Gives the method of cutting out of the geofilter of the currently selected project.

        Returns:
            cut_out_mode_enum.CutOutMode: The cut-out-mode of the currently selected project.
        """
        pass

    def set_cut_out_mode(self, mode):
        """Sets the method of cutting out of the geofilter of the currently selected project.

        Args:
            mode (cut_out_mode_enum.CutOutMode): The mode, to be set

        Returns:
            bool: True, if the CutOutMode was set successfully; False, if an error accured or no project is currently selected.
        """
        pass

    def set_cut_out_reference(self, path):
        """Sets the reference to the cut-out file of the currently selected project.
        This file is later used to calculate the geofilter.

        Args:
            path (pathlib.Path): The path to the file containing the cut-out-geometries

        Returns:
            bool: True, if the reference was set successfully; False, if an error accured. An error accures, if no project is currently selected or if the given path is not valid or occupied.
        """
        pass

    def get_cut_out_reference(self):
        """Gets the reference to the cut-out file of the currently selected project.

        Returns:
            pathlib.Path: The current reference to the cut-out file.
        """ 
        pass