from __future__ import annotations

import tkinter

import customtkinter

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i

import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i
import src.osm_configurator.view.popups.yes_no_pop_up as yes_no_pop_up_i

import src.osm_configurator.view.utilityframes.tag_list_priority_frame as tag_list_priority_frame_i

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.entry_constants as entry_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

import src.osm_configurator.model.model_constants as model_constants_i

from src.osm_configurator.view.freezable import Freezable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.states.state_manager import StateManager

# Finals
ELEMENT_BORDER_DISTANCE: Final = 12


class ReductionDefaultValueFrame(customtkinter.CTkFrame, Freezable):
    """
    This frame shows a list of tags in a priority order, that can be expanded by adding or removing tags.
    These tags can hold default values on attributes that can be used in the calculation.
    """

    def __init__(self, parent: TopLevelFrame, width: int, height: int, state_manager: StateManager):
        """
        This method creates a ReductionDefaultValueFrame where the User can edit default-values on tags for
        categories.

        Args:
            parent (reduction_frame.ReductionFrame): This is the parent frame of this frame.
                The frame will be located here.
            width (int): The width of the frame
            height (int): The height of the frame
            state_manager (StateManager): The StateManager to call if states need to be frozen
        """
        super().__init__(master=parent,
                         width=width,
                         height=height,
                         corner_radius=frame_constants_i.FrameConstants.UTILITY_FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.SUB_FRAME_FG_COLOR.value)

        # Setting private Attributes
        self._parent: TopLevelFrame = parent
        self._width: int = width
        self._height: int = height
        self._state_manager: StateManager = state_manager

        # starts unfrozen
        self._frozen: bool = False

        self._selected_category: category_i.Category | None = None
        self._selected_entry: default_value_entry_i.DefaultValueEntry | None = None

        # Making the grid
        # It is a 7x3 grid, left column is heavier weighted
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)

        # The tag list label
        self._tag_list_label: customtkinter.CTkLabel \
            = customtkinter.CTkLabel(master=self,
                                     width=int(
                                         self._width / 2) - ELEMENT_BORDER_DISTANCE,
                                     height=int(self._height * (
                                             1 / 7)) - ELEMENT_BORDER_DISTANCE,
                                     corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                     fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                     text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                     anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                     text="Tag-List:")
        self._tag_list_label.grid(row=0, column=0, rowspan=1, columnspan=1,
                                  pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                  padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # The Tag List
        self._tag_list: tag_list_priority_frame_i.TagListPriorityFrame = \
            tag_list_priority_frame_i.TagListPriorityFrame(self,
                                                           int(self._width / 2 - ELEMENT_BORDER_DISTANCE),
                                                           int(self._height * (6 / 7) - ELEMENT_BORDER_DISTANCE))
        self._tag_list.grid(row=1, column=0, rowspan=6, columnspan=1)

        # Now the Labels for all the text fields
        # Tag Label
        self._tag_label: customtkinter.CTkLabel \
            = customtkinter.CTkLabel(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=int(self._height * (
                                             1 / 7) - ELEMENT_BORDER_DISTANCE),
                                     corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                     fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                     text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                     anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                     text="Tag")
        self._tag_label.grid(row=1, column=1, rowspan=1, columnspan=1,
                             pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                             padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # Area label
        self._area_label: customtkinter.CTkLabel \
            = customtkinter.CTkLabel(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=int(self._height * (
                                             1 / 7) - ELEMENT_BORDER_DISTANCE),
                                     corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                     fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                     text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                     anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                     text="Area")
        self._area_label.grid(row=2, column=1, rowspan=1, columnspan=1,
                              pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                              padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # Number of Floors Label
        self._number_of_floors_label: customtkinter.CTkLabel \
            = customtkinter.CTkLabel(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=int(self._height * (
                                             1 / 7) - ELEMENT_BORDER_DISTANCE),
                                     corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                     fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                     text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                     anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                     text="Number of floors")
        self._number_of_floors_label.grid(row=3, column=1, rowspan=1, columnspan=1,
                                          pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                          padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # Floor Area Label
        self._floor_area_label: customtkinter.CTkLabel \
            = customtkinter.CTkLabel(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=int(self._height * (
                                             1 / 7) - ELEMENT_BORDER_DISTANCE),
                                     corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                     fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                     text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                     anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                     text="Floor area")
        self._floor_area_label.grid(row=4, column=1, rowspan=1, columnspan=1,
                                    pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                    padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # The text field (Entries) for the Labels
        # Tag Entry
        self._tag_entry: customtkinter.CTkEntry \
            = customtkinter.CTkEntry(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=entry_constants_i.EntryConstants.ENTRY_BASE_HEIGHT_BIG.value,
                                     corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                     fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                     text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._tag_entry.grid(row=1, column=2, rowspan=1, columnspan=1)
        self._tag_entry.bind("<KeyRelease>", self._tag_entry_edited)

        # Area Entry
        self._area_entry: customtkinter.CTkEntry \
            = customtkinter.CTkEntry(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=entry_constants_i.EntryConstants.ENTRY_BASE_HEIGHT_BIG.value,
                                     corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                     fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                     text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._area_entry.grid(row=2, column=2, rowspan=1, columnspan=1)
        self._area_entry.bind("<KeyRelease>", self._area_entry_edited)

        # Number of floors entry
        self._number_of_floors_entry: customtkinter.CTkEntry \
            = customtkinter.CTkEntry(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=entry_constants_i.EntryConstants.ENTRY_BASE_HEIGHT_BIG.value,
                                     corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                     fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                     text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._number_of_floors_entry.grid(row=3, column=2, rowspan=1, columnspan=1)
        self._number_of_floors_entry.bind("<KeyRelease>", self._number_of_floors_entry_edited)

        # Floor Area entry
        self._floor_area_entry: customtkinter.CTkEntry \
            = customtkinter.CTkEntry(master=self,
                                     width=int(self._width * (
                                             1 / 4)) - ELEMENT_BORDER_DISTANCE,
                                     height=entry_constants_i.EntryConstants.ENTRY_BASE_HEIGHT_BIG.value,
                                     corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                     fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                     text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._floor_area_entry.grid(row=4, column=2, rowspan=1, columnspan=1)
        self._floor_area_entry.bind("<KeyRelease>", self._floor_area_entry_edited)

        # The Buttons to create and delete Tags
        self._create_tag_button: customtkinter.CTkButton \
            = customtkinter.CTkButton(master=self,
                                      width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
                                      height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value,
                                      corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                      border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                      fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                      hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                      border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                      text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                      text="Create new tag",
                                      command=self._create_tag_button_pressed)
        self._create_tag_button.grid(row=5, column=1, rowspan=1, columnspan=2)

        # The Button to delete tags
        self._delete_tag_button: customtkinter.CTkButton \
            = customtkinter.CTkButton(master=self,
                                      width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
                                      height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value,
                                      corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                      border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                      fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value,
                                      hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                      border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                      text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                      text="Delete tag",
                                      command=self._delete_tag_button_pressed)
        self._delete_tag_button.grid(row=6, column=1, rowspan=1, columnspan=2)

    def load_category(self, category: category_i.Category) -> bool:
        """
        Loads the given category into the frame to edit that categories default values.

        Args:
            category (category.Category): The category that shall be edited

        Returns:
            bool: True if category was loaded successfully, false else
        """

        self._selected_category: category_i.Category = category

        # resetting the text in the entries
        self._reset_text_entries()

        # Checking for None
        if self._selected_category is None:
            # Works with None, so category can just be given, and also giving none, since no entry si selected yet
            self._tag_list.load_category(self._selected_category, None)

            self._deactivate_frame()
        else:
            self._tag_list.load_category(self._selected_category, None)

            self._activate_frame()

        return True

    def load_entry(self, entry: default_value_entry_i.DefaultValueEntry) -> bool:
        """
        Loads the given default value entry into the frame, so it can be edited.

        Args:
            entry (default_value_entry.DefaultValueEntry): The default value entry, that shall be edited.

        Returns:
            bool: True if entry was successfully loaded, false else
        """

        self._selected_entry: default_value_entry_i.DefaultValueEntry = entry

        # If it is not None, insert information
        if self._selected_entry is not None:
            self._reset_text_entries()

            self._activate_editing()

            # Activating entry, so value can be set
            self._tag_entry.configure(state="normal")
            # Deleting stuff inside first
            self._tag_entry.delete(0, tkinter.END)
            # now inserting new stuff
            self._tag_entry.insert(0, self._selected_entry.get_default_value_entry_tag())
            # deactivating entry again, if it is the default value, so it can't be edited
            if self._selected_entry.get_default_value_entry_tag() == model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG:
                self._tag_entry.configure(state="disabled")
            else:
                self._tag_entry.configure(state="normal")

            self._area_entry.insert(0, self._selected_entry.get_attribute_default(
                attribute_enum_i.Attribute.PROPERTY_AREA))

            self._number_of_floors_entry.insert(0, self._selected_entry.get_attribute_default(
                attribute_enum_i.Attribute.NUMBER_OF_FLOOR))

            self._floor_area_entry.insert(0, self._selected_entry.get_attribute_default(
                attribute_enum_i.Attribute.FLOOR_AREA))

        else:
            self._reset_text_entries()
            self._deactivate_editing()

        return True

    def _tag_entry_edited(self, event: tkinter.Event):

        # Checking for valid string
        tag: str = self._tag_entry.get()

        invalid: bool = False
        entry: default_value_entry_i.DefaultValueEntry
        for entry in self._selected_category.get_default_value_list():
            if (entry.get_default_value_entry_tag() == tag) and (entry is not self._selected_entry):
                invalid: bool = True
                break

        if invalid:
            # If invalid, don't save
            self._tag_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)
        else:
            # if valid try to save
            if not self._selected_entry.set_tag(self._tag_entry.get()):
                # Could not save, mark bad and send error message
                alert_pop_up_i.AlertPopUp("Could not set tag!")
                self._tag_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)
            else:
                # Save worked, mark text good and update button
                self._tag_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
                if not self._tag_list.update_button(self._tag_entry.get()):
                    alert_pop_up_i.AlertPopUp("Updating the buttons on the tag ist has failed!")

    def _area_entry_edited(self, event: tkinter.Event):

        try:
            area: float = float(self._area_entry.get())

            # If it didn't crash we can try to set the value
            if not self._selected_entry.set_attribute_default(attribute_enum_i.Attribute.PROPERTY_AREA, area):
                alert_pop_up_i.AlertPopUp("Could not set area!")
                self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)
            else:
                self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        except ValueError:
            # If it did crash, mark value as bad, and don't save
            self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _number_of_floors_entry_edited(self, event: tkinter.Event):

        try:
            number_of_floors: float = float(self._number_of_floors_entry.get())

            # If it didn't crash, try setting value
            if not self._selected_entry.set_attribute_default(attribute_enum_i.Attribute.NUMBER_OF_FLOOR,
                                                              number_of_floors):
                alert_pop_up_i.AlertPopUp("Could not set number of floors!")
                self._number_of_floors_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)
            else:
                self._number_of_floors_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        except ValueError:
            # If it fails, don't save, and mark as bad
            self._number_of_floors_entry.configure(
                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _floor_area_entry_edited(self, event: tkinter.Event):

        try:
            floor_area: float = float(self._floor_area_entry.get())

            # If it didn't crash, try setting value
            if not self._selected_entry.set_attribute_default(attribute_enum_i.Attribute.FLOOR_AREA, floor_area):
                alert_pop_up_i.AlertPopUp("Could not set floor area!")
                self._floor_area_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)
            else:
                self._floor_area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        except ValueError:
            # If it did crash, mark as bad and don't save
            self._floor_area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _create_tag_button_pressed(self):
        # Letting the user choose a Name
        dialog = customtkinter.CTkInputDialog(
            title="Creating new Tag",
            text="Type in the name, for the Tag:",
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value,
            button_fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            button_hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            button_text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            entry_fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
            entry_text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
        )
        tag: str = dialog.get_input()

        invalid: bool = False
        entry: default_value_entry_i.DefaultValueEntry
        for entry in self._selected_category.get_default_value_list():
            if entry.get_default_value_entry_tag() == tag:
                invalid: bool = True
                break

        if not invalid:
            new_entry: default_value_entry_i.DefaultValueEntry = default_value_entry_i.DefaultValueEntry(tag)

            if self._selected_category.add_default_value_entry(new_entry):
                self._selected_entry: default_value_entry_i.DefaultValueEntry = new_entry

                self._tag_list.load_category(self._selected_category, self._selected_entry)
                self.load_entry(self._selected_entry)
            else:
                alert_pop_up_i.AlertPopUp("Could not create new default value tag!")
        else:
            alert_pop_up_i.AlertPopUp("Default Value Tag, with the tag '" + tag + "' already exists!")

    def _delete_tag_button_pressed(self):
        self._state_manager.freeze_state()
        yes_no_pop_up_i.YesNoPopUp("Want to delete, selected default value entry?", self._pop_up_answer)

    def _pop_up_answer(self, answer: bool):
        self._state_manager.unfreeze_state()

        if answer:
            if self._selected_category.remove_default_value_entry(self._selected_entry):
                # If deletion was successfully, reload category
                self.load_category(self._selected_category)
            else:
                self.after(1, alert_pop_up_i.AlertPopUp, "Could not delete default value entry!")

    def _deactivate_editing(self):
        self._delete_tag_button.configure(
            state="disabled",
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value
        )

        self._tag_entry.configure(state="disabled")
        self._area_entry.configure(state="disabled")
        self._number_of_floors_entry.configure(state="disabled")
        self._floor_area_entry.configure(state="disabled")

    def _activate_editing(self):

        self._delete_tag_button.configure(state="normal",
                                          text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                          fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value)

        # Only deactivating the tag entry if this is the Default Value, so it doesn't get edited
        if self._selected_entry.get_default_value_entry_tag() == model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG:
            self._tag_entry.configure(state="disabled")
        else:
            self._tag_entry.configure(state="normal")

        self._area_entry.configure(state="normal")
        self._number_of_floors_entry.configure(state="normal")
        self._floor_area_entry.configure(state="normal")

    def _deactivate_frame(self):

        self._create_tag_button.configure(
            state="disabled",
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value
        )

        self._deactivate_editing()

    def _activate_frame(self):

        self._create_tag_button.configure(state="normal",
                                          text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                          fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value)

        self._activate_editing()

    def _reset_text_entries(self):
        # Deleting everything in all the Text Entries
        # And setting the color to normal
        self._tag_entry.delete(0, tkinter.END)
        self._tag_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

        self._area_entry.delete(0, tkinter.END)
        self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

        self._number_of_floors_entry.delete(0, tkinter.END)
        self._number_of_floors_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

        self._floor_area_entry.delete(0, tkinter.END)
        self._floor_area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        if not self._frozen:
            self._tag_entry.configure(state="disabled")
            self._area_entry.configure(state="disabled")
            self._number_of_floors_entry.configure(state="disabled")
            self._floor_area_entry.configure(state="disabled")

            self._create_tag_button.configure(state="disabled")
            self._delete_tag_button.configure(state="disabled")

            self._tag_list.freeze()

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        if self._frozen:

            # Only deactivating the tag entry if this is the Default Value, so it doesn't get edited
            if self._selected_entry.get_default_value_entry_tag() == model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG:
                self._tag_entry.configure(state="disabled")
            else:
                self._tag_entry.configure(state="normal")

            self._area_entry.configure(state="normal")
            self._number_of_floors_entry.configure(state="normal")
            self._floor_area_entry.configure(state="normal")

            self._create_tag_button.configure(state="normal")
            self._delete_tag_button.configure(state="normal")

            # Deactivating stuff again if nothing is loaded
            if self._selected_category is None:
                self._deactivate_frame()
            elif self._selected_entry is None:
                self._deactivate_editing()

            self._tag_list.unfreeze()

            self._frozen: bool = False
