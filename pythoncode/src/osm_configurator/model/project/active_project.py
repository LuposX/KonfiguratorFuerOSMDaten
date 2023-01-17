from pathlib import Path

import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.data_visualizer
import src.osm_configurator.model.project.project_settings
import src.osm_configurator.model.project.calculation.calculation_manager
import src.osm_configurator.model.project.export


class ActiveProject:
    """
    This class job is to manage the active project the user is working on.
    Whereby an active project, a project is that got selected by the user in the project selected screen or
    created.
    """

    def __init__(self, project_folder, is_newly_created, project_name=None, project_description=None):
        """
        Creates a new instance of the ActiveProject. In this process it creates the ConfigurationManager and also
        differentiate between the case that the project is new or loaded. In the case of an existing project it
        calls the ProjectLoader, otherwise it creates a new project.

        Args:
            project_folder (pathlib.Path): This is path pointing towards the folder, where the project is saved.
            is_newly_created (bool): This argument is true if the project is newly created, otherwise false.
            project_name (str): How we want to name the project.
            project_description (str): The description of our project.
        """
        pass

    def get_last_step(self):
        """
        This method is there so that the user can continue working in the same phase in an existing project
        where he previously stopped.

        Returns:
            config_phase_enum.ConfigPhase: The last phase the user was working on.
        """
        pass

    def get_project_path(self):
        """
        This method is to give back the path pointing towards the project folder.

        Returns:
            pathlib.Path: The path pointing towards the project folder.
        """
        pass


    def get_config_manager(self):
        """
        Getter for the configuration Manager.

        Returns:
            configuration_manager.ConfigurationManager: The configuration manager.
        """
        pass

    def get_data_visualizer(self):
        """
        Getter for the data visualizer.

        Returns:
            data_visualizer.DataVisualizer: The data visualizer.
        """
        pass

    def get_project_settings(self):
        """
        Getter for the project settings.

        Returns:
            project_settings.ProjectSettings: The project settings.
        """
        pass

    def get_calculation_manager(self):
        """
        Getter for the calculation Manager.

        Returns:
            calculation_manager.CalculationManager: The calculation Manager.
        """
        pass

    def get_export_manager(self):
        """
        Getter for the export Manager.

        Returns:
            export.Export: The  export Manager.
        """
        pass

