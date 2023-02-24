from __future__ import annotations

import tkinter

import src.osm_configurator.control.settings_controller_interface as settings_controller_i

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.text_box_constants as text_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.entry_constants as entry_constants_i

from pathlib import Path
import customtkinter
from tkinter import filedialog

from typing import TYPE_CHECKING

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

if TYPE_CHECKING:
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp


class SettingsApplicationFrame(TopLevelFrame):
    """
    This frame shows the settings of the application.
    """

    def __init__(self, parent, settings_controller: ISettingsController):
        """
        This method creates a SettingsApplicationFrame, showing the settings of the application.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            settings_controller (settings_controller.SettingsController): Respective controller.
        """
        super().__init__(
            master=parent,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 2,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value,
        )

        self._parent = parent
        self._settings_controller = settings_controller

        self._project_default_folder: Path = self._settings_controller.get_project_default_folder()

        self._labels: list[customtkinter.CTkLabel] = []  # holds all labels to allow uniform styling
        self._buttons: list[customtkinter.CTkButton] = []  # holds all buttons to allow uniform styling
        self._entries: list[customtkinter.CTkEntry] = []  # holds all entries to allow uniform styling

        self._frozen: bool = False  # indicates whether the window is frozen or not

        # Defining the grid-structure
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = \
            customtkinter.CTkLabel(master=self,
                                   text="General Settings",
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                   )
        self.header.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        self._labels.append(self.header)

        # Setting: Default folder

        self.path_default_header = \
            customtkinter.CTkLabel(master=self,
                                   text="Default Folder",
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                   )
        self.path_default_header.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        self._labels.append(self.path_default_header)

        self.path_default_label = \
            customtkinter.CTkLabel(master=self,
                                   text=str(self._project_default_folder),
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                   )
        self.path_default_label.grid(row=1, column=1, padx=10,
                                     pady=10)  # Creates a read-only textbox showing the default-filepath
        self._labels.append(self.path_default_label)

        self.change_default_path_button = \
            customtkinter.CTkButton(master=self,
                                    text="Change Default Folder",
                                    command=self.__change_default_folder,
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
                                    )
        self.change_default_path_button.grid(row=1, column=3, padx=10,
                                             pady=10)  # button to browse for a new default folder
        self._buttons.append(self.change_default_path_button)

        # Setting: Number of Processes
        self.path_process_header = \
            customtkinter.CTkLabel(master=self,
                                   text="Number of Processes [Multiprocessing]",
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                   )
        self.path_process_header.grid(row=2, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        self._labels.append(self.path_process_header)

        self.processes_entry: customtkinter.CTkEntry = \
            customtkinter.CTkEntry(master=self,
                                   corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                   fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                   text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value,
                                   )
        self.processes_entry.grid(row=2, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.processes_entry.bind("<KeyRelease>", self.__processes_entry_edited)
        self._entries.append(self.processes_entry)

        # Setting: Number of Key Recommendations
        self.path_key_recom_header = \
            customtkinter.CTkLabel(master=self,
                                   text="Number of Key Recommendations",
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                   )
        self.path_key_recom_header.grid(row=3, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        self._labels.append(self.path_key_recom_header)

        self.key_recom_entry: customtkinter.CTkEntry = \
            customtkinter.CTkEntry(master=self,
                                   corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                   fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                   text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value,
                                   )
        self.key_recom_entry.grid(row=3, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.key_recom_entry.bind("<KeyRelease>", self.__key_recom_entry_edited)
        self._entries.append(self.key_recom_entry)

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.
        """
        self._project_default_folder = self._settings_controller.get_project_default_folder()

        self.path_default_label.configure(
            text=self._project_default_folder
        )

        self.processes_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self.key_recom_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

        self.processes_entry.delete(0, tkinter.END)
        self.processes_entry.insert(0, self._settings_controller.get_number_of_processes())

        self.key_recom_entry.delete(0, tkinter.END)
        self.key_recom_entry.insert(0, self._settings_controller.get_number_of_key_recommendations())

    def __change_default_folder(self):
        """
        Opens the explorer making the user choose a new path for the default folder
        Changes the default folder to the path that was chosen.
        Checks if the path is valid and confirms changes if so.
        If the path is not valid a popup will be shown reloading the page
        """
        new_path = Path(self.__browse_files())

        if new_path.exists():
            self._project_default_folder = new_path
            self._settings_controller.set_project_default_folder(new_path)  # Updates the path
            self.path_default_label.configure(text=new_path.name)  # Updates the textbox
            return
        AlertPopUp("Please enter a valid path!")
        self.activate()  # reloads the page

    def __processes_entry_edited(self, event: tkinter.Event):
        if self.processes_entry.get().isdigit():
            self._settings_controller.set_number_of_processes(self.processes_entry.get())
            self.processes_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        else:
            self.processes_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def __key_recom_entry_edited(self, event: tkinter.Event):
        if self.key_recom_entry.get().isdigit():
            self._settings_controller.set_number_of_key_recommendations(self.key_recom_entry.get())
            self.key_recom_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        else:
            self.key_recom_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the default-folder making the user browse for the searched path
        Returns:
            str: Name of the chosen path
        """
        new_path = \
            filedialog.askdirectory(initialdir=str(self._project_default_folder),
                                    title="Select a File")
        return new_path

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        self._frozen = True

        for button in self._buttons:
            button.configure(state=tkinter.DISABLED)

        for label in self._labels:
            label.configure(state=tkinter.DISABLED)

        for entry in self._entries:
            entry.configure(state=tkinter.DISABLED)

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        self._frozen = False

        for button in self._buttons:
            button.configure(state=tkinter.NORMAL)

        for label in self._labels:
            label.configure(state=tkinter.NORMAL)

        for entry in self._entries:
            entry.configure(state=tkinter.NORMAL)
