class ExportController:
    """The ExportController forwards requests to the model, regarding the export of information as files, in the currently selected project.
    """

    def __init__(self):
        """Creates a new instance of the ExportController, with a association to the model.

        Args:
            model (IApplication): The interface which is used to communicate with the model.
        """
        pass

    def export_project(self, path):
        """Exports the currently selected project.
        The folders and files of he project are copied to the given destination.

        Args:
            path (Path): The place in storage, where the project should be exported to.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage or there was no project selected.
        """
        pass

    def export_calculations(self, path):
        """Exports the result of the calculations of the currently selected project.
        The folders and files regarding the results of the calculations are copied to the given destination.

        Args:
            path (Path): The place in storage, where the results should be exported to.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage, the calculations have not produced results yet or there was no project selected.
        """
        pass

    def export_configurations(self, path):
        """Exports the category file of the currently selected project.
        A list of categories in the current project is stored at the given destination.
        Args:
            path (Path): The place in storage, where the categories should be stored at.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage or there was no project selected.
        """
        pass