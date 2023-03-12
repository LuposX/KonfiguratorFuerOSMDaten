from __future__ import annotations

import tkinter
from pathlib import Path
from tkinter import filedialog
from typing import TYPE_CHECKING, Iterable
import customtkinter

import webbrowser

import src.osm_configurator.view.states.state_manager as state_manager
import src.osm_configurator.control.data_visualization_controller_interface as data_visualization_controller_interface
import src.osm_configurator.control.cut_out_controller_interface as cut_out_controller_interface
import src.osm_configurator.control.category_controller_interface as category_controller_interface
import src.osm_configurator.control.osm_data_controller_interface as osm_data_controller_interface
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
import src.osm_configurator.view.popups.yes_no_pop_up as yes_no_pop_up_i

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.check_box_constants as check_box_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

if TYPE_CHECKING:
    from \
        src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
    from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
    from src.osm_configurator.control.project_controller_interface import IProjectController


class DataFrame(TopLevelFrame):
    """
    This frame lets the user edit various following Data:
    - Selection of the OSM-Data
    - Selection of the Cut-Out
    - Select, if buildings on the edge shall be included or not
    - A download button to download the OSM data after a cut-out was selected
    - Copy in category configurations
    """

    def __init__(self, state_manager: state_manager,
                 data_visualization_controller: IDataVisualizationController,
                 cut_out_controller: ICutOutController, category_controller: ICategoryController,
                 osm_data_controller: IOSMDataController, project_controller: IProjectController):
        """
        This method creates a DataFrame, that lets the User input data into the project.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller
            cut_out_controller (cut_out_controller.CutOutController): Respective controller
            category_controller (category_controller.CategoryController): Respective controller
            osm_data_controller (osm_data_controller_interface.IOSMDataController): Respective controller
        """
        super().__init__(
            master=None,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value,
        )

        self._selected_cut_out_path = None
        self._state_manager = state_manager
        self._data_visualization_controller: IDataVisualizationController = data_visualization_controller
        self._cut_out_controller: ICutOutController = cut_out_controller
        self._category_controller: ICategoryController = category_controller
        self._osm_data_controller: IOSMDataController = osm_data_controller
        self._project_controller: IProjectController = project_controller

        self._frozen: bool = False  # indicates whether the window is frozen or not

        self._selected_cut_out_path: Path
        self._selected_osm_data_path: Path
        self._buildings_on_the_edge_are_in: bool = False  # Buildings on the edge are not in by default

        self._buttons: list[customtkinter.CTkButton] = []  # Holds all buttons to make equal styling easier
        self._labels: list[customtkinter.CTkLabel] = []  # Holds all labels to make equal styling easier
        self._checkboxes: list[customtkinter.CTkCheckBox] = []  # Holds all checkboxes to makes equals styling easier

        # Defining the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        #  Implementing the buttons

        self._osm_data_select_button: customtkinter.CTkButton = \
            customtkinter.CTkButton(
                master=self,
                command=self.__select_osm_data,
                text="Select"
            )
        self._buttons.append(self._osm_data_select_button)

        self._cut_out_select_button: customtkinter.CTkButton = \
            customtkinter.CTkButton(
                master=self,
                command=self.__select_cut_out,
                text="Select"
            )
        self._buttons.append(self._cut_out_select_button)

        self._copy_button: customtkinter.CTkButton = \
            customtkinter.CTkButton(
                master=self,
                command=self.__copy_category_configurations,
                text="Select"
            )
        self._buttons.append(self._copy_button)

        self._view_cutout_button: customtkinter.CTkButton = \
            customtkinter.CTkButton(
                master=self,
                command=self.__view_cut_out,
                text="View Cutout"
            )
        self._buttons.append(self._view_cutout_button)

        # Equal styling for all buttons
        for button in self._buttons:
            button.configure(
                corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                text_color_disabled=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
                width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_SMALL.value,
                height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_SMALL.value
            )

        # Implementing the labels

        self._osm_data_select_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(
                master=self,
                text="Select OSM Data"
            )
        self._labels.append(self._osm_data_select_label)

        self._cut_out_select_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(
                master=self,
                text="Select Cut-Out"
            )
        self._labels.append(self._cut_out_select_label)

        self._copy_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(
                master=self,
                text="Copy in Category Configurations"
            )
        self._labels.append(self._copy_label)

        self._osm_data_selected_path_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(
                master=self,
                text=""
            )
        self._labels.append(self._osm_data_selected_path_label)

        self._cut_out_selected_path_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(
                master=self,
                text=""
            )
        self._labels.append(self._cut_out_selected_path_label)

        # Styles all labels the same way
        for label in self._labels:
            label.configure(
                corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
            )

        # Implementing the checkbox
        self._edge_building_are_in_checkbox: customtkinter.CTkCheckBox = \
            customtkinter.CTkCheckBox(
                master=self,
                command=self.__edge_buildings_clicked,
                fg_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_FG_COLOR.value,
                hover_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_HOVER_COLOR.value,
                text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value,
                corner_radius=check_box_constants_i.CheckBoxConstants.CHECK_BOX_CORNER_RADIUS.value,
                border_width=check_box_constants_i.CheckBoxConstants.CHECK_BOX_BORDER_WIDTH.value,
                variable=tkinter.BooleanVar(),
                text="Buildings on the edge are in",
            )

        # Aligning everything nicely in the predefined grid

        # Labels at the top
        self._osm_data_select_label.grid(
            row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10
        )

        self._cut_out_select_label.grid(
            row=0, column=1, rowspan=1, columnspan=1, padx=10, pady=10
        )

        self._copy_label.grid(
            row=0, column=2, rowspan=1, columnspan=1, padx=10, pady=10
        )

        # Buttons underneath the labels
        self._osm_data_select_button.grid(
            row=1, column=0, rowspan=1, columnspan=1, padx=10, pady=10
        )

        self._cut_out_select_button.grid(
            row=1, column=1, rowspan=1, columnspan=1, padx=10, pady=10
        )

        self._copy_button.grid(
            row=1, column=2, rowspan=1, columnspan=1, padx=10, pady=10
        )

        # Path Labels
        self._cut_out_selected_path_label.grid(
            row=2, column=1, rowspan=1, columnspan=1, padx=10, pady=10
        )

        self._osm_data_selected_path_label.grid(
            row=2, column=0, rowspan=1, columnspan=1, padx=10, pady=10
        )

        # Le Checkbox
        self._edge_building_are_in_checkbox.grid(
            row=3, column=1, rowspan=1, columnspan=1, padx=10, pady=10
        )

        # Last button at the bottom
        self._view_cutout_button.grid(
            row=4, column=1, rowspan=1, columnspan=1, padx=10, pady=10
        )

    def activate(self):
        """
        Updates the data if the page is reloaded
        """
        self._selected_cut_out_path: Path = self._cut_out_controller.get_cut_out_reference()
        self._selected_osm_data_path: Path = self._osm_data_controller.get_osm_data_reference()

        self._cut_out_selected_path_label.configure(
            text=str(self._selected_cut_out_path.stem)
        )
        self._osm_data_selected_path_label.configure(
            text=str(self._selected_osm_data_path.stem)
        )

    def __view_cut_out(self):
        """
        Lets the user view the cutout.
        Activated if the view_cutout button is activated
        """
        path = self._data_visualization_controller.generate_cut_out_map()

        self._show_map(path)

    def __copy_category_configurations(self):
        self._selected_path: Path = self.__get_directory_path()
        if self._selected_path == Path("."):
            return

        if self._category_controller.check_conflicts_in_category_configuration(self._selected_path):
            if not self._category_controller.import_category_configuration(self._selected_path):
                AlertPopUp("Importing Categories Failed!")
        else:
            self._state_manager.freeze_state()
            yes_no_pop_up_i.YesNoPopUp("Do you really want to overwrite conflicting Categories?", self.__pop_up_answer)

    def __pop_up_answer(self, answer: bool):
        self._state_manager.unfreeze_state()
        if answer:
            if not self._category_controller.import_category_configuration(self._selected_path):
                AlertPopUp("Importing Categories Failed!")

        self._selected_path = None

    def __select_cut_out(self):
        """
        Opens the explorer letting the user choose a file selecting the cut-out
        """
        chosen_path: Path = self.__get_file_path()
        print(chosen_path)
        if not chosen_path.exists() or chosen_path == Path("."):
            # Chosen path is invalid
            popup = AlertPopUp("Path is incorrect, please choose a valid Path!")
            self.activate()
            return

        self._cut_out_controller.set_cut_out_reference(path=chosen_path)  # Gives the reference to the controller
        self._selected_cut_out_path = chosen_path  # Updates path in its own class
        self._cut_out_selected_path_label.configure(
            text=str(chosen_path.stem)
        )  # Updates the label showing the chosen path

    def __select_osm_data(self):
        """
        Opens the explorer letting the user choose a file selecting the osm-data
        """
        chosen_path: Path = self.__get_file_path()

        if not chosen_path.exists() or chosen_path == Path("."):
            # chosen path is invalid
            AlertPopUp("Path is incorrect, please choose a valid Path!")
            self.activate()
            return

        self._osm_data_controller.set_osm_data_reference(chosen_path)  # Gives the reference to the controller
        self._selected_osm_data_path = chosen_path  # Updates the path in its own class
        self._osm_data_selected_path_label.configure(
            text=str(chosen_path.stem)
        )  # Updates the label showing the chosen path

    def __edge_buildings_clicked(self):
        """
        Activated if the checkbox is clicked.
        Updates the cut_out_mode and shows a popup if an error occured
        """
        check_box_value: bool = self._edge_building_are_in_checkbox.getvar(name="value")  # Gets the bool-value
        cut_out_mode: CutOutMode

        if check_box_value:
            cut_out_mode = CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED  # Checkbox marked => buildings on edge accepted
        else:
            cut_out_mode = CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED.value  # Checkbox unmarked => not accepted

        worked = self._cut_out_controller.set_cut_out_mode(cut_out_mode)  # updates the cut-out-mode

        if not worked:
            AlertPopUp(message="Sorry, this did not work!")
            self.activate()

    def __get_directory_path(self) -> Path:
        """
        Opens explorer and lets the user choose a path to a directory
        Returns:
            Path: The chosen path
        """
        new_path = \
            filedialog.askdirectory(title="Please select Your Directory",
                                    initialdir=self._project_controller.get_project_path(),
                                    )
        return Path(new_path)

    def __get_file_path(self) -> Path:
        """
        Opens explorer and lets the user choose a path to a file
        Returns:
            Path: The chosen path
        """
        new_path = filedialog.askopenfilename(title="Please select Your File",
                                              initialdir=self._project_controller.get_project_path(),
                                              )
        return Path(new_path)

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        for button in self._buttons:
            button.configure(state=tkinter.DISABLED)

        for label in self._labels:
            label.configure(state=tkinter.DISABLED)

        for checkbox in self._checkboxes:
            checkbox.configure(state=tkinter.DISABLED)

        self._frozen = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        for button in self._buttons:
            button.configure(state=tkinter.NORMAL)

        for label in self._labels:
            label.configure(state=tkinter.NORMAL)

        for checkbox in self._checkboxes:
            checkbox.configure(state=tkinter.NORMAL)

        self._frozen = False

    def _show_map(self, path_to_map: Path) -> bool:
        """
        This function is used to visualize am already created map.

         Args:
            path_to_map (Path): the path where the map is saved we want to show.

         Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        try:
            webbrowser.open_new(str(path_to_map))
        except Exception:
            return False

        return True
