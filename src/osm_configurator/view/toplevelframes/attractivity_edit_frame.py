from __future__ import annotations

import tkinter

import customtkinter

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.category_controller_interface

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.options_menu_constants as options_menu_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.entry_constants as entry_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.configuration.attractivity_attribute as attractivity_attribute_i
import src.osm_configurator.view.states.state_name_enum as state_name_enum_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i
import src.osm_configurator.view.popups.yes_no_pop_up as yes_no_pop_up_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.category_controller_interface import ICategoryController

# Finals
ELEMENT_BORDER_DISTANCE: Final = 42


class AttractivityEditFrame(TopLevelFrame):
    """
    This frame lets the user edit, create and delete attractivity attributes for the categories.
    Two drop-down menus will be shown: One will select the category, the other the attractivity attributes.
    Editing options for the attractivity attributes will be offered in a textbox to change the name. Smaller boxes
    provide the means of changing the factors for different attributes.
    Two buttons provide creation and deletion tools.
    """

    def __init__(self, state_manager: StateManager, category_controller: ICategoryController):
        """
        This method creates an AttractivityEditFrame, where the attractivity attributes of categories can be edited,
        created or be deleted.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, when it wants to change to another state.
            category_controller (category_controller.CategoryController): Respective controller
        """
        # Starting with no master
        # Also setting other settings
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)

        # Setting Private Attributes
        self._state_manager: StateManager = state_manager
        self._category_controller: ICategoryController = category_controller

        # Frame starts unfrozen
        self._frozen: bool = False

        self._categories: [category_i.Category] = []
        self._attractivities: [attractivity_attribute_i.AttractivityAttribute] = []

        self._selected_category: category_i.Category = None
        self._selected_attribute: attractivity_attribute_i.AttractivityAttribute = None

        # Making the grid
        # It is a 8x3 grid, but the bottom has some lower weights, because the labels and textfields will be smaller
        # and the other buttons will be taking 2 rows
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)

        # Making the Category drop down
        # Starts empty
        self._category_drop_down_menu: customtkinter.CTkOptionMenu = customtkinter.CTkOptionMenu(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (2 / 3) - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_CORNER_RADIUS.value,
            fg_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_FG_COLOR.value,
            button_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BUTTON_COLOR.value,
            button_hover_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BUTTON_HOVER_COLOR.value,
            dropdown_fg_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_FG_COLOR.value,
            dropdown_hover_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_HOVER_COLOR.value,
            dropdown_text_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_TEXT_COLOR.value,
            anchor=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_ANCHOR.value,
            hover=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_HOVER.value,
            state=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_STATE.value,
            values=[],
            command=self._category_drop_down_menu_edited)
        self._category_drop_down_menu.grid(row=0, column=1, rowspan=1, columnspan=2)

        # The Attractivity Drop Down Menu
        # Also starts empty
        self._attractivity_drop_down_menu: customtkinter.CTkOptionMenu = customtkinter.CTkOptionMenu(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (2 / 3) - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_CORNER_RADIUS.value,
            fg_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_FG_COLOR.value,
            button_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BUTTON_COLOR.value,
            button_hover_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BUTTON_HOVER_COLOR.value,
            dropdown_fg_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_FG_COLOR.value,
            dropdown_hover_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_HOVER_COLOR.value,
            dropdown_text_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_TEXT_COLOR.value,
            anchor=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_ANCHOR.value,
            hover=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_HOVER.value,
            state=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_STATE.value,
            values=[],
            command=self._attractivity_drop_down_menu_edited)
        self._attractivity_drop_down_menu.grid(row=1, column=1, rowspan=1, columnspan=2)

        # The Labels for the Drop Down Menus
        # Choose Categories Label
        self._choose_categories_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                       width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                       height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                       fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                       text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                       anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                       padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                       pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                       text="Choose Categories:")
        self._choose_categories_label.grid(row=0, column=0, rowspan=1, columnspan=1)

        # Label for Attractivity Attribute
        self._choose_attractivity_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
                                                                                         corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                         fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                         text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                         anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                         padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                         pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                         text="Choose Attractivity:")
        self._choose_attractivity_label.grid(row=1, column=0, rowspan=1, columnspan=1)

        # Now the Label for the Attractivity Name
        self._attractivity_name_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                       width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                       height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                       fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                       text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                       anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                       padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                       pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                       text="Attractivity Name:")
        self._attractivity_name_label.grid(row=2, column=0, rowspan=1, columnspan=1)

        # The Entry to edit the Attractivity Name
        self._attractivity_name_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self,
                                                                                       width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                               2 / 3) - ELEMENT_BORDER_DISTANCE,
                                                                                       height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                                                                       fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                                                                       text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._attractivity_name_entry.bind("<KeyRelease>", self._attractivity_name_entry_edited)
        self._attractivity_name_entry.grid(row=2, column=1, rowspan=1, columnspan=2)

        # Now Making all the Labels for editing the Attribute-Factors
        # The Label that says Attribute
        self._attribute_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                               width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                               height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
                                                                               corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                               fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                               text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                               anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                               padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                               pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                               text="Attribute:")
        self._attribute_label.grid(row=3, column=0, rowspan=1, columnspan=1)

        # The Label that says Factor
        self._factor_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
                                                                            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                            padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                            pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                            text="Factor:")
        self._factor_label.grid(row=3, column=1, rowspan=1, columnspan=1)

        # Area Label
        self._area_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                          width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                          height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                          corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                          fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                          text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                          anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                          padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                          pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                          text="Area:")
        self._area_label.grid(row=4, column=0, rowspan=1, columnspan=1)

        # Numbers of Floors Label
        self._number_of_floors_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                      width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                      height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                                      corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                      fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                      text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                      anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                      padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                      pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                      text="Number of Floors:")
        self._number_of_floors_label.grid(row=5, column=0, rowspan=1, columnspan=1)

        # Floor Area Label
        self._floor_area_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                                corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                text="Floor Area:")
        self._floor_area_label.grid(row=6, column=0, rowspan=1, columnspan=1)

        # Base Attractivity Label
        self._base_attractivity_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                       width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                       height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                       fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                       text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                       anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                       padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                       pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                       text="Base Attractivity:")
        self._base_attractivity_label.grid(row=7, column=0, rowspan=1, columnspan=1)

        # Now the Entry Boxes to fill in a Value
        # The all also have a previous value, since only Numbers will be allowed, specific only floats
        # The Area Entry
        self._area_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self,
                                                                          width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                          height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                          corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                                                          fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                                                          text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._area_entry.bind("<KeyRelease>", self._area_entry_edited)
        self._area_entry.grid(row=4, column=1, rowspan=1, columnspan=1)

        # The Number of Floors Entry
        self._numbers_of_floors_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self,
                                                                                       width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                       height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                                                                       fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                                                                       text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._numbers_of_floors_entry.bind("<KeyRelease>", self._number_of_floors_entry_edited)
        self._numbers_of_floors_entry.grid(row=5, column=1, rowspan=1, columnspan=1)

        # The Floor Area Entry
        self._floor_area_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self,
                                                                                width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                                corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                                                                fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                                                                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._floor_area_entry.bind("<KeyRelease>", self._floor_area_entry_edited)
        self._floor_area_entry.grid(row=6, column=1, rowspan=1, columnspan=1)

        # The Base Attractivity Entry
        self._base_attractivity_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self,
                                                                                       width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                                                                                       height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 8 - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                                                                       fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                                                                       text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
        self._base_attractivity_entry.bind("<KeyRelease>", self._base_attractivity_entry_edited)
        self._base_attractivity_entry.grid(row=7, column=1, rowspan=1, columnspan=1)

        # Now the Buttons to change to the attractivity view
        # and to create and delete attractivities

        # The View Button
        self._view_attractivity_list_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="View\nAttractivity-List",
            command=self._view_attractivity_list_pressed)
        self._view_attractivity_list_button.grid(row=3, column=2, rowspan=1, columnspan=1)

        # The Create Button
        self._create_new_attractivity_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="Create new Attractivity",
            command=self._create_new_attractivity_button_pressed)
        self._create_new_attractivity_button.grid(row=4, column=2, rowspan=2, columnspan=1)

        # The Delete Button
        self._delete_attractivity_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="Delete Selected Attractivity",
            command=self._delete_attractivity_button_pressed)
        self._delete_attractivity_button.grid(row=6, column=2, rowspan=2, columnspan=1)

    def activate(self):

        # unfreezing the frame
        self.unfreeze()

        # First getting all categories, that are active!
        all_categories: List[category_i.Category] = self._category_controller.get_list_of_categories()
        # Also resetting the categories, that the frame knows of
        self._categories: [category_i.Category] = []

        category: category_i.Category
        for category in all_categories:
            if category.is_active():
                self._categories.append(category)

        if len(self._categories) == 0:
            self._selected_category: category_i.Category = None
        else:
            self._selected_category: category_i.Category = self._categories[0]

        self._load_category(self._selected_category)

    def _category_drop_down_menu_edited(self):

        category: category_i.Category
        for category in self._categories:
            if category.get_category_name() == self._category_drop_down_menu.get():
                self._load_category(category)
                break

    def _attractivity_drop_down_menu_edited(self):

        attractivity: attractivity_attribute_i.AttractivityAttribute
        for attractivity in self._attractivities:
            if attractivity.get_attractivity_attribute_name() == self._attractivity_drop_down_menu.get():
                self._load_attractivity(attractivity)
                break

    def _attractivity_name_entry_edited(self, event: tkinter.Event):

        # Checking if the name already exists
        name_exists: bool = False
        attractivity: attractivity_attribute_i.AttractivityAttribute
        for attractivity in self._attractivities:
            if (attractivity.get_attractivity_attribute_name() == self._attractivity_name_entry.get()) and (
                    attractivity is not self._selected_attribute):
                # If the Name already exsist, the Name will be shown red, and not be saved,
                # so the old name remains!
                self._attractivity_name_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)
                name_exists: bool = True
                break

        # First checking if the name is valid
        if not name_exists:
            # and if it is valid, trying to change it
            if (not self._selected_attribute.set_attractivity_attribute_name(self._attractivity_name_entry.get())) and (
                    not name_exists):
                # If it went wrong, alert pop up will show
                alert_pop_up_i.AlertPopUp("Could not set the name for the Attractivity-Attribute!")
            else:
                # if went ok, the text will be normal colored again!
                self._attractivity_name_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

    def _area_entry_edited(self, event: tkinter.Event):
        # Checking if the Valua can be casted into a float
        try:
            # if possible set the new value
            factor: float = float(self._area_entry.get())
            self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

            if not self._selected_attribute.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, factor):
                # If setting the factor fails, a popup will emerge!
                alert_pop_up_i.AlertPopUp("Could not set the area-factor, for this Attractivity-Attribute!")
                # also making the text invalid colored again!
                self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

        except ValueError:
            # If not make text invalid colored and don't save value
            self._area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _number_of_floors_entry_edited(self, event: tkinter.Event):
        # Checking if the value is castable to a float
        try:
            # if possible set the new value
            factor: float = float(self._numbers_of_floors_entry.get())
            self._numbers_of_floors_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

            if not self._selected_attribute.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, factor):
                # if setting factor fails, text shows invalid and popup emerges!
                alert_pop_up_i.AlertPopUp("Could not set the floor-factor, for this Attractivity-Attribute!")
                self._numbers_of_floors_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

        except ValueError:
            # If not possible, set text red and don't save Value
            self._numbers_of_floors_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _floor_area_entry_edited(self, event: tkinter.Event):
        # Checking if value is castable to a float
        try:
            # if possible save factor
            factor: float = float(self._floor_area_entry.get())
            self._floor_area_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

            if not self._selected_attribute.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, factor):
                # If not possible to set, show error through popup and invalid text color!
                alert_pop_up_i.AlertPopUp("Could not set the ground-area-factor, for this Attractivity-Attribute!")
                self._floor_area_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

        except ValueError:
            # If not possible, set text red and don't save Value
            self._floor_area_entry.configure(
                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _base_attractivity_entry_edited(self, event: tkinter.Event):
        # Checking if value is castable to a float
        try:
            # If possible, save value
            factor: float = float(self._base_attractivity_entry.get())
            self._base_attractivity_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)

            if not self._selected_attribute.set_base_factor(factor):
                # If setting the factor fails, popup emerges and text color is invalid!
                alert_pop_up_i.AlertPopUp("Could not set the base-factor, for this Attractivity-Attribute!")
                self._base_attractivity_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

        except ValueError:
            # If not possible, make text red and don't save value
            self._base_attractivity_entry.configure(
                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _view_attractivity_list_pressed(self):
        if not self._state_manager.change_state(state_name_enum_i.StateName.ATTRACTIVITY_VIEW):
            alert_pop_up_i.AlertPopUp("Changing to View Attractivity List Failed!")

    def _create_new_attractivity_button_pressed(self):
        dialog = customtkinter.CTkInputDialog(title="Creating new Attractivity-Attribute",
                                              text="Type in the name, for the Attractivity-Attribute:",
                                              fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value,
                                              button_fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                              button_hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                              button_text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                              entry_fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                              entry_text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value,
                                              text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value)

        name: str = dialog.get_input()

        # Cheking if name is not a duplicate
        name_ok: bool = True
        attribute: attractivity_attribute_i.AttractivityAttribute
        for attribute in self._attractivities:
            if (attribute.get_attractivity_attribute_name() == name) and (attribute is not self._selected_attribute):
                alert_pop_up_i.AlertPopUp("Attractivity-Attribute with name: '" + name + "' already exists!")
                name_ok: bool = False
                break

        if name_ok:
            new_attractivity: attractivity_attribute_i.AttractivityAttribute = attractivity_attribute_i.AttractivityAttribute(
                name)
            if not self._selected_category.add_attractivity_attribute(new_attractivity):
                alert_pop_up_i.AlertPopUp("Creation of Attractivity-Attribute Failed!")
            else:
                self._attractivities: [
                    attractivity_attribute_i.AttractivityAttribute] = self._selected_category.get_attractivity_attributes()

                # Loading the category anew, to refresh the attribute drop down menu and refreshing everything else
                self._load_category(self._selected_category)

                # Now loading the new attribute
                # technically the load category loaded automatically one, we just override it, nor problem
                self._load_attractivity(new_attractivity)

    def _delete_attractivity_button_pressed(self):
        self._state_manager.freeze_state()
        yes_no_pop_up_i.YesNoPopUp("Want to delete, currently selected Attractivity-Attribute?", self._pop_up_answer)

    def _pop_up_answer(self, answer: bool):
        self._state_manager.unfreeze_state()

        if answer:
            if not self._selected_category.remove_attractivity_attribute(self._selected_attribute):
                alert_pop_up_i.AlertPopUp("Could not delete Attractivity-Attribute!")
            else:
                # If it worked, doing activate after, to refresh the Frame
                self.activate()

    def _load_category(self, category: category_i.Category):
        if category is None:
            self._category_drop_down_menu.configure(values=[])
            self._category_drop_down_menu.set("")
            self._deactivate_whole_editing()
        else:
            self._activate_whole_editing()

            # Getting all the names of the categories
            # No worries about empty list, since if category isn't None, the List has to have Elements
            categories_strings: [str] = []
            c: category_i.Category
            for c in self._categories:
                categories_strings.append(c.get_category_name())

            # Automatically selecting the first category in Category Drop Down
            self._category_drop_down_menu.configure(values=categories_strings)
            self._category_drop_down_menu.set(categories_strings[0])

            if len(category.get_attractivity_attributes()) == 0:
                self._selected_attribute: attractivity_attribute_i.AttractivityAttribute = None
                self._attractivities: [attractivity_attribute_i.AttractivityAttribute] = []

                self._attractivity_drop_down_menu.configure(values=[])
                self._attractivity_drop_down_menu.set("")
            else:
                self._attractivities: [
                    attractivity_attribute_i.AttractivityAttribute] = category.get_attractivity_attributes()
                self._selected_attribute: attractivity_attribute_i.AttractivityAttribute = self._attractivities[0]

                attractivity_strings: List[str] = []
                a: attractivity_attribute_i.AttractivityAttribute
                for a in self._attractivities:
                    attractivity_strings.append(a.get_attractivity_attribute_name())

                # Automatically selecting first attribute
                self._attractivity_drop_down_menu.configure(values=attractivity_strings)
                self._attractivity_drop_down_menu.set(attractivity_strings[0])

            self._load_attractivity(self._selected_attribute)

    def _load_attractivity(self, attractivity: attractivity_attribute_i.AttractivityAttribute):
        if attractivity is None:
            self._deactivate_attractivity_editing()
        else:
            self._activate_attractivity_editing()

            # Inserting the Name
            self._attractivity_name_entry.delete(0, tkinter.END)
            self._attractivity_name_entry.insert(0, attractivity.get_attractivity_attribute_name())

            # Inserting all the Factors
            self._area_entry.delete(0, tkinter.END)
            self._area_entry.insert(0,
                                    str(attractivity.get_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA)))

            self._numbers_of_floors_entry.delete(0, tkinter.END)
            self._numbers_of_floors_entry.insert(0,
                                                 str(attractivity.get_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR)))

            self._floor_area_entry.delete(0, tkinter.END)
            self._floor_area_entry.insert(0, str(attractivity.get_attribute_factor(
                attribute_enum_i.Attribute.NUMBER_OF_FLOOR)))

            self._base_attractivity_entry.delete(0, tkinter.END)
            self._base_attractivity_entry.insert(0, str(attractivity.get_base_factor()))

    def _deactivate_whole_editing(self):

        self._attractivity_drop_down_menu.configure(values=[], state="disabled")
        self._attractivity_drop_down_menu.set("")

        # No Attractivities can be created or deleted now!
        self._create_new_attractivity_button.configure(state="disabled")
        self._delete_attractivity_button.configure(state="disabled")

        self._deactivate_attractivity_editing()

    def _activate_whole_editing(self):

        self._attractivity_drop_down_menu.configure(state="normal")

        self._create_new_attractivity_button.configure(state="normal")
        self._delete_attractivity_button.configure(state="normal")

        self._activate_attractivity_editing()

    def _deactivate_attractivity_editing(self):

        # Disabling Name
        self._attractivity_name_entry.delete(0, tkinter.END)
        self._attractivity_name_entry.configure(state="disabled",
                                                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        # Disabling all the Factor Entries
        self._area_entry.delete(0, tkinter.END)
        self._area_entry.configure(state="disabled", text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        self._numbers_of_floors_entry.delete(0, tkinter.END)
        self._numbers_of_floors_entry.configure(state="disabled", text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        self._floor_area_entry.delete(0, tkinter.END)
        self._floor_area_entry.configure(state="disabled",
                                         text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        self._base_attractivity_entry.delete(0, tkinter.END)
        self._base_attractivity_entry.configure(state="disabled",
                                                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        # Disabling delete Button
        self._delete_attractivity_button.configure(state="disabled")

        # Create Button is not getting touched, here, and the view button never!

    def _activate_attractivity_editing(self):

        # Activating Name
        self._attractivity_name_entry.configure(state="normal",
                                                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        # ACtivating all Factor Entries
        self._area_entry.configure(state="normal", text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)
        self._numbers_of_floors_entry.configure(state="normal", text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)
        self._floor_area_entry.configure(state="normal", text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)
        self._base_attractivity_entry.configure(state="normal",
                                                text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR)

        # Activating the Delete Button
        self._delete_attractivity_button.configure(state="normal")

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        if not self._frozen:
            self._category_drop_down_menu.configure(state="disabled")
            self._attractivity_drop_down_menu.configure(state="disabled")
            self._attractivity_name_entry.configure(state="disabled")
            self._area_entry.configure(state="disabled")
            self._numbers_of_floors_entry.configure(state="disabled")
            self._floor_area_entry.configure(state="disabled")
            self._view_attractivity_list_button.configure(state="disabled")
            self._create_new_attractivity_button.configure(state="disabled")
            self._delete_attractivity_button.configure(state="disabled")

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        if self._frozen:
            self._category_drop_down_menu.configure(state="normal")
            self._attractivity_drop_down_menu.configure(state="normal")
            self._attractivity_name_entry.configure(state="normal")
            self._area_entry.configure(state="normal")
            self._numbers_of_floors_entry.configure(state="normal")
            self._floor_area_entry.configure(state="normal")
            self._view_attractivity_list_button.configure(state="normal")
            self._create_new_attractivity_button.configure(state="normal")
            self._delete_attractivity_button.configure(state="normal")

            # Deactivating stuff if needed again!
            if self._selected_category is None:
                self._deactivate_whole_editing()
            elif self._selected_attribute is None:
                self._deactivate_attractivity_editing()

            self._frozen: bool = False
