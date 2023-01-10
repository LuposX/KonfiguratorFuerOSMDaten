from abc import ABC, abstractmethod
import src.osm_configurator.model.project.calculation.aggregation_method_enum
import src.osm_configurator.model.project.calculation.calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum
#import src.osm_configurator.model.project.configuration.category
#import src.osm_configurator.model.project.configuration.attractivity_attribute
import pathlib
import src.osm_configurator.model.project.configuration.cut_out_mode_enum
import matplotlib
import src.osm_configurator.model.application.passive_project
import src.osm_configurator.model.project.config_phase_enum

class IControl(ABC):
    """This class provides a consistent interface for access to the control-package. It is a facade, to make access easy.
    The control manages the access to the module. That's why this interface should give access to all the features provided by the model.
    """

    @abstractmethod
    def get_list_of_passive_projects(self):
        """Returns the list of (passive) projects, which are in the default project folder of the application.

        Returns:
            list[passive_project.PassiveProject]: The list of passive projects in the default project folder.
        """
        pass

    @abstractmethod
    def load_project(self, path):
        """Loads a project
        All relevant data of a project are verified and loaded in memory. All coming project-refering calls will be directed to the given project.

        Args:
            path (pathlib.Path): the path to the project folder of the project, to be loaded.

        Returns:
            bool: True, if the project was loaded succesfully; False if an error accured, while trying to load the project. An error accures, if the path is not pointing to a valid project folder or if the project has corrupted files.
        """
        pass

    @abstractmethod
    def create_project(self, name, description, destination):
        """Creates a new project with the given attributes and loads it.
        The model creates a new project folder at the given destination, all relevant files are generated and the project is loaded into memory.

        Args:
            name (str): The name of the to-be-created project, may not contain any line-breaks.
            description (str): The description of the to-be-created project. May contain line-breaks.
            destination (pathlib.Path): The path to the location, where the projectfolder of the project should be created.

        Returns:
            bool: True, if the project was created successfully; False if an error accured. An error accures, if the name of the project is not valid, if the destination-path is not valid or if the destination-location is already occupied.
        """
        pass

    @abstractmethod
    def delete_passive_project(self, project):
        """Deletes a project out of the default project folder.

        Args:
            project (passive_project.PassiveProject): The project, that is going to be deleted.

        Returns:
            bool: True, if the (passive) project has been deleted successfully; False otherwise: The project does not exist or the application has not the right permissions to delete the project.
        """
        pass

    @abstractmethod
    def save_project(self):
        """Saves the project.
        The currently selected project is stored on the disk. All progress made since the last saving are saved.

        Returns:
            bool: True, if the project was saved successfully; False if an error accured, while attempting to save the project or when there is no project selected.
        """
        pass

    @abstractmethod
    def set_current_config_phase(self, config_phase):
        """Stores the current configuration phase in the model.

        Args:
            config_phase (config_phase_enum.ConfigPhase): The new configuration phase.

        Returns:
            bool: True, if setting the configuration phase was successfull; False, otherwise.
        """
        pass

    @abstractmethod
    def get_current_config_phase(self):
        """Returns the configuration phase, that is currently stored in the model.

        Returns:
            config_phase_enum.ConfigPhase: The configuration phase, that is currently stored in the model.
        """
        pass

    @abstractmethod
    def is_project_loaded(self):
        """Checks, whether any project is currently loaded/selected.

        Returns:
            bool: True, if a project is currently selected; False, otherwise.
        """
        pass

    @abstractmethod
    def set_osm_data_reference(self, path):
        """Sets the reference to the osm-data for the selected project.
        The reference contains the osm-data used in the calculations of the project. This method does not check if the given data is valid.

        Args:
            path (pathlib.Path): The reference to the osm-data

        Returns:
            bool: True, if the new reference was set successfully; False, if an error accured whie setting the reference.
        """
        pass

    @abstractmethod
    def get_osm_data_reference(self):
        """Returns the path to the osm-data, that is used in the currently selected project.

        Returns:
            pathlib.Path: The path to the osm-data of the currently selected project.
        """
        pass

    @abstractmethod
    def download_osm_data(self, path):
        """Downloads osm-data
        The osm-data to be downloaded are defined by a geojson-file. The data is downloaded and the reference to the correct osm-files is stored.

        Args:
            path (pathlib.Path): The path to the above mentioned gejson-file.

        Returns:
            boolean: True on success, False otherwise
        """
        pass

    @abstractmethod
    def get_cut_out_mode(self):
        """Gives the method of cutting out of the geofilter of the currently selected project.

        Returns:
            cut_out_mode_enum.CutOutMode: The cut-out-mode of the currently selected project.
        """
        pass

    @abstractmethod
    def set_cut_out_mode(self, mode):
        """Sets the method of cutting out of the geofilter of the currently selected project.

        Args:
            mode (cut_out_mode_enum.CutOutMode): The mode, to be set

        Returns:
            bool: True, if the CutOutMode was set successfully; False, if an error accured or no project is currently selected.
        """
        pass

    @abstractmethod
    def set_cut_out_reference(self, path):
        """Sets the reference to the cut-out file of the currently selected project.
        This file is later used to calculate the geofilter.

        Args:
            path (pathlib.Path): The path to the file containing the cut-out-geometries

        Returns:
            bool: True, if the reference was set successfully; False, if an error accured. An error accures, if no project is currently selected or if the given path is not valid or occupied.
        """
        pass

    @abstractmethod
    def get_cut_out_reference(self):
        """Gets the reference to the cut-out file of the currently selected project.

        Returns:
            pathlib.Path: The current reference to the cut-out file.
        """ 
        pass

    @abstractmethod
    def check_conflicts_in_category_configuration(self, path):
        """Checks for a given file, if it is a valid category-file and checks, whether there are naming conflicts with the categories of the currently selected project.

        Args:
            path (pathlib.Path): The path to the category-file

        Returns:
            bool: True, if there is currently a project selected and there are no naming conflicts; False, otherwise.
        """
        pass

    @abstractmethod
    def import_category_configuration(self, path):
        """Imports the given categories into the currently selected project.
        Adds the given categories to the category list of the project.

        Args:
            path (pathlib.Path): The path to the category file

        Returns:
            bool: True, if the categories where added successfully; False, if an error accured: The project does not exists, The category file is corrupted or the category file does not exist.
        """
        pass

    @abstractmethod
    def get_list_of_categories(self):
        """Returns the list of all categories, that are currently in the currently selected project.

        Returns:
            list[category.Category]: A list of the categories of the project in no particular order.
        """
        pass

    @abstractmethod
    def create_category(self):
        """Creates a new category in the currently selected project.
        A new category is added to the list of categories of the project. The category has empty properties, except for an arbitrary name.

        Returns:
            category.Category: The newly created category
        """
        pass

    @abstractmethod
    def delete_category(self, category):
        """Deletes the given category.
        Removes the given category from the list of categories of the currently selected project

        Args:
            category (category.Category): The category, to be deleted

        Returns:
            bool: True, if the category was deleted successfully; False, otherwise
        """
        pass

    @abstractmethod
    def get_list_of_tag_recommendations(self, current_input):
        """Returns a list of recommended tags, based on the input that is already entered by the user.

        Args:
            current_input (str): The input, that is currently written by the user.

        Returns:
            list[str]: A list of recommendations, based on the current_input.
        """
        pass

    @abstractmethod
    def get_attractivities_of_category(self, category):
        """Returns the attractivity attributes that are defined for the given category.

        Args:
            category (category.Category): The category, whose attractivities are of interest.

        Returns:
            list[attractivity_attribute.AttractivityAttribute]: The list of attractivity attributes of the given category
        """
        pass

    @abstractmethod
    def get_aggregation_methods():
        """Returns a list of all aggregation methods that are available. 
        This function returns all available aggregation methods, not just the ones that are active in the current project.

        Returns:
            list[aggregation_method_enum.AggregationMethod]: The list of the available aggregation methods
        """
        pass

    @abstractmethod
    def is_aggregation_method_active(self, method):
        """Checks, whether a aggregation method is active in the currently selected project.

        Args:
            method (aggregation_method_enum.AggregationMethod): The aggregation method that is checked for.

        Returns:
            bool: True, if there is currently a project selected and the given aggregation method is active in it; False otherwise.
        """
        pass

    @abstractmethod
    def set_aggregation_method_active(self, method, active):
        """Activates or deactivates an aggregation method (of the currently selected project).
        Activates the given method, if active=True and deactivates it otherwise.

        Args:
            method (aggregation_method_enum.AggregationMethod): The aggregation method we want to deactivate/activate
            active (bool): True, if we want to activate the given method; False, if we want to deactivate it.

        Returns:
            bool: True, if a project is currently selected and the aggregation method was (de-)activated successfully; False, otherwise.
        """
        pass

    @abstractmethod
    def start_calculations(self, starting_phase):
        """Starts the calculations in the given calculation phase in the currently selected project.
        The calculation process is devided in different calculation phases. This function starts the calculation in a given phase.

        Args:
            starting_phase (calculation_phase_enum.CalculationPhase): The phase, in which the calculation should start

        Returns:
            calculation_state_enum.CalculationState: The status of the calculation: RUNNING, if the calculation was started successfully. For details on the meaning of this return value, see CalculationState
        """
        pass

    @abstractmethod
    def get_calculation_state(self):
        """Gives the current calculation state of the selected project.

        Returns:
            calculation_state_enum.CalculationState: Returns the current state of the calculation. For details see documentation of CalculationState.
        """
        pass

    @abstractmethod
    def get_current_calculation_phase(self):
        """Returns the calculation phase of the currently selected project.

        Returns:
            calculation_phase_enum.CalculationPhase: The phase, that is currently running. NONE, if no phase is currently running.
        """
        pass

    @abstractmethod
    def get_current_calculation_process(self):
        """Returns an approximation of the progress of the calculations in the currently selected project.
        The progress is given as a number between 0 and 1, where 0 indicates that the calculation has not started yet and 1 indicates, that the calculations are done.

        Returns:
            float: The value of the approximation.
        """
        pass

    @abstractmethod
    def cancel_calculations(self):
        """Cancels the calculations of the currently selected project.
        The calculation phase that is currently running will be stopped.

        Returns:
            bool: True, if the calculation was canceled successfully; False, otherwise.
        """
        pass

    @abstractmethod
    def export_project(self, path):
        """Exports the currently selected project.
        The folders and files of he project are copied to the given destination.

        Args:
            path (pathlib.Path): The place in storage, where the project should be exported to.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage or there was no project selected.
        """
        pass

    @abstractmethod
    def export_calculations(self, path):
        """Exports the result of the calculations of the currently selected project.
        The folders and files regarding the results of the calculations are copied to the given destination.

        Args:
            path (pathlib.Path): The place in storage, where the results should be exported to.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage, the calculations have not produced results yet or there was no project selected.
        """
        pass

    @abstractmethod
    def export_configurations(self, path):
        """Exports the category file of the currently selected project.
        A list of categories in the current project is stored at the given destination.
        Args:
            path (pathlib.Path): The place in storage, where the categories should be stored at.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage or there was no project selected.
        """
        pass

    @abstractmethod
    def export_cut_out_map(self, path):
        """Exports the map generated by the cut-out configuration.
        Args:
            path (pathlib.Path): The place in storage, where the cut out map should be stored at.

        Returns:
            bool: True, if the export was successfull; False, if an error accured: The path was not valid or occupied, there was not enought space in storage, the application wasn't able to create the map or there was no project selected.
        """
        pass

    @abstractmethod
    def get_project_name(self):
        """Gets the name of the currently selected project.

        Returns:
            str: The name of the project
        """
        pass

    @abstractmethod
    def set_project_name(self, name):
        """Sets the name of the currently selected project

        Args:
            name (str): The new name of the project, may not contain line breaks.

        Returns:
            bool: True, if the name was changed successfully; False, if an error accured: The name is not valid or no project was selected.
        """
        pass

    @abstractmethod
    def get_project_description(self):
        """Gets the description of the currently selected project.

        Returns:
            str: The description of the project
        """
        pass

    @abstractmethod
    def set_project_description(self, description):
        """Sets the description of the currently selected project

        Args:
            description (str): The new description of the project, may contain line breaks.

        Returns:
            bool: True, if the description was changed successfully; False, otherwise.
        """
        pass

    @abstractmethod
    def get_project_default_folder(self):
        """Gets the project default folder.
        The project default folder is the folder, where projects are stored by default.

        Returns:
            pathlib.Path: The path to the project default folder
        """
        pass

    @abstractmethod
    def set_project_default_folder(self, default_folder):
        """Sets the project default folder
        The project default folder is the folder, where projects are stored by default.

        Args:
            default_folder (pathlib.Path): The path to the new project default folder

        Returns:
            bool: True, if the default folder was set successfully; False if an error accured: The path is not valid or occupied.
        """
        pass

    @abstractmethod
    def generate_cut_out_map(self):
        """Generates a map of the data of the currently selected project.
        Using the cut-out file of the project, this function creates a map as a html-file of the project. The path to the html-file is returned.

        Returns:
            pathlib.Path: The path to the file, where the map is stored.
        """
        pass

    @abstractmethod
    def get_calculation_visualization(self):
        """Generates a graphic that visualizes the results of the calculations of the currently selected project.

        Returns:
            matplotlib.Axes: The resulting visualization as axes of the matplotlib library.
        """
        pass