import src.osm_configurator.view.toplevelframes.project_head_frame


class ExportFrame:
    """
    The ExportFrame provides a dropdown menu that providing the following Options:
    - project export
    - calculation export
    - Configurations Export
    """

    def __init__(self, parent_frame, control):
        """
        This method creates an ExportFrame that provides the user with different export options.

        Args:
            parent_frame (project_head_frame.ProjectHeadFrame): The parent of the ExportFrame is the HeadFrame where the export feature is located.
            control (control_interface.IControl): The control the frame calls to gain access to the model to export.
        """
        pass
