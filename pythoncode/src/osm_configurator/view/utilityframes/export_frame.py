import src.osm_configurator.view.toplevelframes.project_head_frame
import src.osm_configurator.control.control_interface


class ExportFrame:
    """
    The Export Frame provides a DropDown Menu that give the following Export Options:
    - Project Export
    - Calculation Export
    - Configurations Export
    """

    def __init__(self, parent_frame, control):
        """
        This Method Creates an ExportFrame, that provides the suer with different Export Options.

        Args:
            parent_frame (project_head_frame.ProjectHeadFrame): The Parent of the ExportFrame is the HeadFrame,
            where the Export Feature is located.
            control (control_interface.IControl): The Control the Frame calls, to get access to
            the Model for the Exports.
        """
        pass