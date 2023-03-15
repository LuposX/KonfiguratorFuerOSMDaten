from __future__ import annotations

from functools import partial

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.scrollbar_constants as scrollbar_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.options_menu_constants as options_menu_constants_i
import src.osm_configurator.view.constants.entry_constants as entry_constants_i
import src.osm_configurator.view.constants.check_box_constants as check_box_constants_i
import src.osm_configurator.view.constants.text_box_constants as text_box_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i
import src.osm_configurator.view.popups.yes_no_pop_up as yes_no_pop_up_i

import src.osm_configurator.model.project.configuration.category as category_i

import customtkinter
import tkinter

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from src.osm_configurator.model.parser.custom_exceptions.not_valid_name_Exception import NotValidName

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.category_controller_interface import ICategoryController

# Final Variables
ELEMENT_BORDER_DISTANCE: Final = 10
CHECKBOX_HEIGHT_AND_WIDTH: Final = 42
CHECKBOX_TEXT_ACTIVE: Final = "Category Active"
CHECKBOX_TEXT_DISABLED: Final = "Category Disabled"
RECOMMEND_BUTTON_HEIGHT: Final = 42

PAD_X: Final = 4
PAD_Y: Final = 4

# ID of the TabButton
TAB_BUTTON_ID_MAC: Final = 805306377
TAB_BUTTON_ID_WINDOWS: Final = 9


class CategoryFrame(TopLevelFrame):
    """
    This frame lets the user create, delete and edit categories.
    It shows the name of a category, as well as their black- and white-List.
    Categories also can be turned on and off with Checkboxes.
    There will also be key-recommendations be shown for the black- and white-List.
    """

    def __init__(self, state_manager: StateManager, category_controller: ICategoryController):
        """
        This method creates an CategoryFrame so the user can create, delete and edit categories.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call,
                when it wants to change to another state.
            category_controller (category_controller.CategoryController): Respective controller
        """
        # Starting with no master
        # Also setting other settings
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
                         )

        # Private Attributes
        self._state_manager: StateManager = state_manager
        self._category_controller: ICategoryController = category_controller
        # Starting with no Category
        self._categories: List[category_i.Category] = []
        self._selected_category: category_i.Category | None = None

        # starts unfrozen
        self._frozen: bool = False

        # Last edited List (Black or White List)
        # Important for, where to autofill in keys
        # As default, the whiteList was last edited
        # Both can NEVER be true or False at the same Time
        self._white_list_was_last_edited: bool = True
        self._black_list_was_last_edited: bool = False

        # Making the grid
        # ---------------
        # The grid is a 3x3 grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # The grid is made up by smaller frames
        # CategoryMenu
        self._category_menu_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 3,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
        )
        self._category_menu_frame.grid(row=0, column=0, rowspan=1, columnspan=3)
        # This frame also has a grid
        # It is a 3x2 grid, where the second column is weighted heaviest
        self._category_menu_frame.grid_columnconfigure(0, weight=1)
        self._category_menu_frame.grid_columnconfigure(1, weight=4)
        self._category_menu_frame.grid_columnconfigure(2, weight=1)
        self._category_menu_frame.grid_rowconfigure(0, weight=1)
        self._category_menu_frame.grid_rowconfigure(1, weight=1)
        # Making the Labels for the Frame
        self._choose_categories_label: customtkinter.CTkLabel = customtkinter.CTkLabel(
            master=self._category_menu_frame,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 6 - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
            text="Choose Categories"
        )
        self._choose_categories_label.grid(row=0, column=0, rowspan=1, columnspan=1,
                                           pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                           padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # CategoryNameLabel
        self._category_name_label: customtkinter.CTkLabel = customtkinter.CTkLabel(
            master=self._category_menu_frame,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 6 - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
            text="Category Name"
        )
        self._category_name_label.grid(row=1, column=0, rowspan=1, columnspan=1,
                                       pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                       padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # Making the dropdown Menu
        self._category_drop_down_menu: customtkinter.CTkOptionMenu = customtkinter.CTkOptionMenu(
            master=self._category_menu_frame,
            width=((frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3) * 2 - ELEMENT_BORDER_DISTANCE),
            height=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_BASE_HEIGHT.value,
            corner_radius=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_CORNER_RADIUS.value,
            fg_color=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_FG_COLOR.value,
            button_color=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_BUTTON_COLOR.value,
            button_hover_color=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_BUTTON_HOVER_COLOR.value,
            dropdown_fg_color=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_DROPDOWN_FG_COLOR.value,
            dropdown_hover_color=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_DROPDOWN_HOVER_COLOR.value,
            dropdown_text_color=options_menu_constants_i.OptionsMenuConstants.
            OPTIONS_MENU_CONSTANTS_DROPDOWN_TEXT_COLOR.value,
            anchor=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_ANCHOR.value,
            hover=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_HOVER.value,
            state=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_STATE.value,
            values=[],
            command=self._category_drop_down_menu_edited,
            text_color=options_menu_constants_i.OptionsMenuConstants.OPTIONS_MENU_CONSTANTS_DROPDOWN_TEXT_COLOR.value
        )
        self._category_drop_down_menu.grid(row=0, column=1, rowspan=1, columnspan=1)

        # Making the TextField / Entry for the Category Name
        self._category_name_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(
            master=self._category_menu_frame,
            width=((frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3) * 2 - ELEMENT_BORDER_DISTANCE),
            height=entry_constants_i.EntryConstants.ENTRY_BASE_HEIGHT_BIG.value,
            corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
            fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
            text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value
        )
        self._category_name_entry.grid(row=1, column=1, rowspan=1, columnspan=1)
        # Binding the Name Entry to KeyRelease, so it gets recorded, if the name gets edited
        self._category_name_entry.bind("<KeyRelease>", self._category_name_edited)

        # Making the Label for the Checkbox
        self._category_checkbox_label: customtkinter.CTkLabel = customtkinter.CTkLabel(
            master=self._category_menu_frame,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 6 - ELEMENT_BORDER_DISTANCE,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 6 - ELEMENT_BORDER_DISTANCE,
            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
            text="Activate or Deactivate Category:"
        )
        self._category_checkbox_label.grid(row=0, column=2, rowspan=1, columnspan=1,
                                           pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                           padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # Making the Checkbox, to activate and disable Categories
        self._category_checkbox: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(
            master=self._category_menu_frame,
            width=CHECKBOX_HEIGHT_AND_WIDTH,
            height=CHECKBOX_HEIGHT_AND_WIDTH,
            corner_radius=check_box_constants_i.CheckBoxConstants.CHECK_BOX_CORNER_RADIUS.value,
            border_width=check_box_constants_i.CheckBoxConstants.CHECK_BOX_BORDER_WIDTH.value,
            fg_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_FG_COLOR.value,
            hover_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_HOVER_COLOR.value,
            text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value,
            text=CHECKBOX_TEXT_ACTIVE,
            command=self._category_checkbox_edited
        )
        self._category_checkbox.grid(row=1, column=2, rowspan=1, columnspan=1)

        # WhiteListFrame
        self._white_list_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3,
            height=(
                           frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 3) * 2,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
        )
        # The grid has two rows, with the second one being higher weighted
        self._white_list_frame.grid_columnconfigure(0, weight=1)
        self._white_list_frame.grid_rowconfigure(0, weight=1)
        self._white_list_frame.grid_rowconfigure(0, weight=5)
        self._white_list_frame.grid(row=1, column=0, rowspan=2, columnspan=1)

        # The Label of the WhiteList
        self._white_list_label: customtkinter.CTkLabel = customtkinter.CTkLabel(
            master=self._white_list_frame,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
            height=(
                    frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 9 - ELEMENT_BORDER_DISTANCE),
            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
            text="White List:"
        )
        self._white_list_label.grid(row=0, column=0, rowspan=1, columnspan=1,
                                    pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                    padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # The TextBox which contains the WhiteList
        self._white_list = customtkinter.CTkTextbox(
            master=self._white_list_frame,
            width=((frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3) - 2*ELEMENT_BORDER_DISTANCE),
            height=((frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 9) * 5 - 2*ELEMENT_BORDER_DISTANCE),
            corner_radius=text_box_constants_i.TextBoxConstants.TEXT_BOX_CORNER_RADIUS.value,
            border_width=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_WITH.value,
            fg_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_FG_COLOR.value,
            border_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_COLOR.value,
            text_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_TEXT_COLOR.value
        )
        self._white_list.grid(row=1, column=0, rowspan=1, columnspan=1)
        # Binding the Whitelist to KeyRelease, so editing is recorded
        self._white_list.bind("<KeyRelease>", self._white_list_edited)

        # BlackListFrame
        self._black_list_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3,
            height=(
                           frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 3) * 2,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
        )
        # The grid is just two rows, with the second one being higher weighted
        self._black_list_frame.grid_columnconfigure(0, weight=1)
        self._black_list_frame.grid_rowconfigure(0, weight=1)
        self._black_list_frame.grid_rowconfigure(1, weight=5)
        self._black_list_frame.grid(row=1, column=1, rowspan=2, columnspan=1)

        # Making the Label of the BlackList
        self._black_list_label: customtkinter.CTkLabel = customtkinter.CTkLabel(
            master=self._black_list_frame,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
            height=(
                    frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 9 - ELEMENT_BORDER_DISTANCE),
            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
            text="Black List:"
        )
        self._black_list_label.grid(row=0, column=0, rowspan=1, columnspan=1,
                                    pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                                    padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        # Making the TextBox which contains the BlackList
        self._black_list: customtkinter.CTkTextbox = customtkinter.CTkTextbox(
            master=self._black_list_frame,
            width=((frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3) - 2*ELEMENT_BORDER_DISTANCE),
            height=((frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 9) * 5 - 2*ELEMENT_BORDER_DISTANCE),
            corner_radius=text_box_constants_i.TextBoxConstants.TEXT_BOX_CORNER_RADIUS.value,
            border_width=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_WITH.value,
            fg_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_FG_COLOR.value,
            border_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_COLOR.value,
            text_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_TEXT_COLOR.value
        )
        self._black_list.grid(row=1, column=0, rowspan=1, columnspan=1)
        # Binding Blacklist to KeyRelease, so editing is recorded
        self._black_list.bind("<KeyRelease>", self._black_list_edited)

        # RecommenderFrame
        # This is a scrollable Frame
        self._recommender_frame = customtkinter.CTkScrollableFrame(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value / 3,
            corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
            fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value
        )
        self._recommender_frame.grid(row=1, column=2, rowspan=1, columnspan=1)

        # RecommenderFrame doesn't need a grid, it will have its buttons be stacked upon
        # The RecommenderFrame starts empty
        self._recommender_frame_button_list: List[customtkinter.CTkButton] = []

        # CreateDeleteFrame
        self._create_delete_frame = customtkinter.CTkFrame(
            master=self,
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
        )
        # This Frame has a small, 1x2 grid
        self._create_delete_frame.grid_columnconfigure(0, weight=1)
        self._create_delete_frame.grid_rowconfigure(0, weight=1)
        self._create_delete_frame.grid_rowconfigure(1, weight=1)
        self._create_delete_frame.grid(row=2, column=2, rowspan=1, columnspan=1)

        # The create Button
        self._create_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self._create_delete_frame,
            width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
            height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="Create new Category",
            command=self._create_new_category_pressed
        )
        self._create_button.grid(row=0, column=0, rowspan=1, columnspan=1, pady=PAD_Y)

        # The delete Button
        self._delete_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self._create_delete_frame,
            width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
            height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DELETE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR_DELETE.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DELETE.value,
            text="Delete selected Category",
            command=self._delete_category_pressed
        )
        self._delete_button.grid(row=1, column=0, rowspan=1, columnspan=1, pady=PAD_Y)

    def activate(self):
        # First getting the Categories
        self._categories: List[category_i.Category] = self._category_controller.get_list_of_categories()
        if len(self._categories) == 0:
            self._selected_category = None
        else:
            self._selected_category: category_i.Category = self._categories[0]

        # Setting the Category Drop Down Menu
        self._set_category_drop_down_menu(self._categories, self._selected_category)

        # Loading the selected Category
        self._load_category(self._selected_category)

    def _category_drop_down_menu_edited(self, selected_element: str):
        success: bool = False
        category: category_i.Category
        for category in self._categories:
            if category.get_category_name() == selected_element:
                self._selected_category: category_i.Category = category
                self._load_category(self._selected_category)
                success: bool = True
                break
        # If there is no category corresponding to the drop-down Menu, then the drop-down Menu is incorrect, therefore
        # We reload the frame and send an error message in form of an alert pop up
        if not success:
            self.activate()
            alert_pop_up_i.AlertPopUp("There was an Error with the Category selection! The Frame has been refreshed!")

    def _category_name_edited(self, event: tkinter.Event):
        # Getting what is written in the name entry
        new_category_name: str = self._category_name_entry.get()

        successes: bool = True
        category: category_i.Category
        for category in self._categories:
            if ((category is not self._selected_category)
                and (category.get_category_name() == new_category_name)) \
                    or (new_category_name == ""):

                # If there is another Category that has that name already,
                # the value will not be saved and be marked red!
                self._category_name_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value
                )
                successes: bool = False
                break

        # If there was no conflict with the name, the name will be set
        if successes:
            if self._selected_category.set_category_name(new_category_name):
                # If name was successfully set, the text is normal again
                self._category_name_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
                # Setting the category drop down menu new, so it refreshes the name as well
                self._set_category_drop_down_menu(self._categories, self._selected_category)
            else:
                # If name could not be set, there will be an error message, and the text will be shown as invalid again!
                alert_pop_up_i.AlertPopUp("Category Name, could not ne set!")
                self._category_name_entry.configure(
                    text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR_INVALID.value)

    def _category_checkbox_edited(self):
        # Checking if checkbox is checked or unchecked
        active: int = self._category_checkbox.get()

        # If checked, set the category active
        if active == 1:
            if self._selected_category.activate():
                self._category_checkbox.configure(text=CHECKBOX_TEXT_ACTIVE)
            else:
                # If category could not be set active, revert change
                alert_pop_up_i.AlertPopUp("Could not activate Category!")
                if self._selected_category.is_active():
                    self._category_checkbox.configure(text=CHECKBOX_TEXT_ACTIVE)
                    self._category_checkbox.select()
                else:
                    self._category_checkbox.configure(text=CHECKBOX_TEXT_DISABLED)
                    self._category_checkbox.deselect()
        else:
            # if unchecked, deactivate category
            if self._selected_category.deactivate():
                self._category_checkbox.configure(text=CHECKBOX_TEXT_DISABLED)
            else:
                # if not de-activatable, revert change
                alert_pop_up_i.AlertPopUp("Could not deactivate Category!")
                if self._selected_category.is_active():
                    self._category_checkbox.configure(text=CHECKBOX_TEXT_DISABLED)
                    self._category_checkbox.deselect()
                else:
                    self._category_checkbox.configure(text=CHECKBOX_TEXT_ACTIVE)
                    self._category_checkbox.select()

    def _white_list_edited(self, event: tkinter.Event):
        # Checking if TabButton was pressed
        if (event.keycode == TAB_BUTTON_ID_MAC
            or event.keycode == TAB_BUTTON_ID_WINDOWS) \
                and self._white_list_was_last_edited:

            self._white_list.delete("end-1c linestart", "end-1c")
            self._white_list.insert("end-1c linestart", self._get_recommended_string(0))

        # Get new recommendations, based on the last line
        self._set_recommendations_based_on_input(self._white_list.get("end-1c linestart", "end-1c"))
        # Setting the new information contained in the whiteList into the Category
        if not self._selected_category.set_whitelist(self._white_list.get(1.0, "end-1c").splitlines()):
            alert_pop_up_i.AlertPopUp("Could not save WhiteList!")

        self._white_list_was_last_edited: bool = True
        self._black_list_was_last_edited: bool = False

    def _black_list_edited(self, event: tkinter.Event):
        # Checking if the TabButton was pressed
        if (event.keycode == TAB_BUTTON_ID_MAC
            or event.keycode == TAB_BUTTON_ID_WINDOWS) \
                and self._black_list_was_last_edited:

            self._black_list.delete("end-1c linestart", "end-1c")
            self._black_list.insert("end-1c linestart", self._get_recommended_string(0))

        # Get new recommendations, based on the last input
        self._set_recommendations_based_on_input(self._black_list.get("end-1c linestart", "end-1c"))
        # Setting the information in the BlackList in the Category
        if not self._selected_category.set_blacklist(self._black_list.get(1.0, "end-1c").splitlines()):
            alert_pop_up_i.AlertPopUp("Could not save BlackList!")

        self._white_list_was_last_edited: bool = False
        self._black_list_was_last_edited: bool = True

    def _recommend_button_pressed(self, button_id: int):
        if self._white_list_was_last_edited:
            self._white_list.delete("end-1c linestart", "end-1c")
            self._white_list.insert("end-1c linestart", self._get_recommended_string(button_id))
            self._set_recommendations_based_on_input(self._white_list.get("end-1c linestart", "end-1c"))

            if not self._selected_category.set_whitelist(self._white_list.get(1.0, "end-1c").splitlines()):
                alert_pop_up_i.AlertPopUp("Could not save WhiteList!")

            self._white_list.focus_force()
        elif self._black_list_was_last_edited:
            self._black_list.delete("end-1c linestart", "end-1c")
            self._black_list.insert("end-1c linestart", self._get_recommended_string(button_id))
            self._set_recommendations_based_on_input(self._black_list.get("end-1c linestart", "end-1c"))

            if not self._selected_category.set_blacklist(self._black_list.get(1.0, "end-1c").splitlines()):
                alert_pop_up_i.AlertPopUp("Could not save BlackList!")

            self._black_list.focus_force()
        else:
            alert_pop_up_i.AlertPopUp("Could not autocomplete Text!")

    def _get_recommended_string(self, index: int) -> str:

        # if there are no recommendations, an empty string will be returned!
        # Or if the index is out of bounds, an empty string is returned!
        if (len(self._recommender_frame_button_list) == 0) or (index >= len(self._recommender_frame_button_list)):
            return ""
        else:
            return self._recommender_frame_button_list[index].cget("text")

    def _set_recommendations_based_on_input(self, current_input: str):
        # First deleting all recommendation Buttons
        recommend_button: customtkinter.CTkButton
        for recommend_button in self._recommender_frame_button_list:
            recommend_button.destroy()
        self._recommender_frame_button_list = []

        new_recommendations: List[str] = self._category_controller.get_list_of_key_recommendations(current_input)

        # Adding all the new buttons
        recommended_string: str
        button_id: int = 0
        for recommended_string in new_recommendations:
            new_recommend_button: customtkinter.CTkButton = customtkinter.CTkButton(
                master=self._recommender_frame,
                width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 3 - ELEMENT_BORDER_DISTANCE,
                height=RECOMMEND_BUTTON_HEIGHT,
                corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                text=recommended_string,
                command=partial(
                    self._recommend_button_pressed,
                    button_id)
            )
            new_recommend_button.grid(row=button_id, column=0, rowspan=1, columnspan=1, padx=PAD_X, pady=PAD_Y)
            self._recommender_frame_button_list.append(new_recommend_button)
            button_id += 1

    def _create_new_category_pressed(self):

        dialog = customtkinter.CTkInputDialog(
            title="Creating new Category",
            text="Type in the name, for the Category:",
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value,
            button_fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            button_hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            button_text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            entry_fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
            entry_text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
        )

        new_category_name: str = dialog.get_input()

        # checking if the name isn't a duplicate!
        no_duplicate: bool = True
        category: category_i.Category
        for category in self._categories:
            if category.get_category_name() == new_category_name:
                alert_pop_up_i.AlertPopUp("Category with name '" + new_category_name + "' already exists!")
                no_duplicate: bool = False
                break

        if no_duplicate:
            try:
                # If there is no duplicate, we create, the new category
                new_category: category_i.Category = self._category_controller.create_category(new_category_name)

                if new_category is not None:
                    self._categories: List[category_i.Category] = self._category_controller.get_list_of_categories()
                    self._selected_category: category_i.Category = new_category
                    self._set_category_drop_down_menu(self._categories, self._selected_category)
                    self._load_category(self._selected_category)
            except NotValidName as err:
                popup = alert_pop_up_i.AlertPopUp(str(err.args))
                popup.mainloop()
                self.activate()
                return

    def _delete_category_pressed(self):
        self._state_manager.freeze_state()
        yes_no_pop_up_i.YesNoPopUp("Do you want to delete, the currently selected Category?", self._pop_up_answer)

    def _load_category(self, category: category_i.Category):

        self._selected_category: category_i.Category = category

        if self._selected_category is None:
            self._deactivate_editing()
        else:
            self._activate_editing()

            # Fill in Name
            self._category_name_entry.configure(text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value)
            self._category_name_entry.delete(0, tkinter.END)
            self._category_name_entry.insert(0, self._selected_category.get_category_name())

            # Edit Checkbox
            if self._selected_category.is_active():
                self._category_checkbox.select()
                self._category_checkbox.configure(text=CHECKBOX_TEXT_ACTIVE)
            else:
                self._category_checkbox.deselect()
                self._category_checkbox.configure(text=CHECKBOX_TEXT_DISABLED)

            # WhiteList
            self._override_white_list(self._selected_category.get_whitelist())
            self._white_list_was_last_edited: bool = True
            # BlackList
            self._override_black_list(self._selected_category.get_blacklist())
            self._black_list_was_last_edited: bool = False

            # Key Recommendations
            self._set_recommendations_based_on_input(self._white_list.get("end-1c linestart", "end-1c"))

    def _activate_editing(self):
        # Activating all the Buttons etc. but not giving them any text/information

        self._category_name_entry.configure(state="normal")

        self._category_checkbox.configure(state=tkinter.NORMAL)

        self._white_list.configure(state="normal")

        self._black_list.configure(state="normal")

        self._delete_button.configure(state="normal")

    def _deactivate_editing(self):
        # Deleting all information in the editing buttons/text-boxes etc.
        # And also disabling them, so they can't be edited anymore
        # Only the create new button and the drop-down menu stay active!

        # For the DropDown Menu it will only be set to an empty string, if there are Categories in this Menu
        # It should be still possible to select them, but if selected category is None,
        # Then there is probably no category at all
        self._category_drop_down_menu.set("")

        self._category_name_entry.delete(0, tkinter.END)
        self._category_name_entry.configure(state="disabled")

        self._category_checkbox.deselect()
        self._category_checkbox.configure(state=tkinter.DISABLED)

        self._override_white_list([""])
        self._white_list.configure(state="disabled")

        self._override_black_list([""])
        self._black_list.configure(state="disabled")

        button: customtkinter.CTkButton
        for button in self._recommender_frame_button_list:
            button.destroy()
        self._recommender_frame_button_list = []

        self._delete_button.configure(state="disabled")

    def _override_white_list(self, tags: List[str]):
        self._white_list.delete(1.0, "end-1c")
        whole_tag_list: str = ""
        tag: str
        for tag in tags:
            whole_tag_list = whole_tag_list + tag + "\n"
        self._white_list.insert(1.0, whole_tag_list)

    def _override_black_list(self, tags: List[str]):
        self._black_list.delete(1.0, "end-1c")
        whole_tag_list: str = ""
        tag: str
        for tag in tags:
            whole_tag_list = whole_tag_list + tag + "\n"
        self._black_list.insert(1.0, whole_tag_list)

    def _set_category_drop_down_menu(self, category_list: List[category_i.Category],
                                     active_category: category_i.Category | None):

        # Getting all category Names
        category_names: List[str] = []
        category: category_i.Category
        for category in category_list:
            category_names.append(category.get_category_name())

        self._category_drop_down_menu.configure(values=category_names)

        if active_category is None:
            self._category_drop_down_menu.set("")
        else:
            self._category_drop_down_menu.set(active_category.get_category_name())

    def _pop_up_answer(self, answer: bool):
        self._state_manager.unfreeze_state()
        if answer:
            self._delete_category()

    def _delete_category(self):
        if not self._category_controller.delete_category(self._selected_category):
            alert_pop_up_i.AlertPopUp("Could not delete Category!\nFrame has been refreshed!")
        else:
            # Doing activate after category got deleted, to refresh frame and select automatically another category
            self.activate()

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        if not self._frozen:
            self._category_drop_down_menu.configure(state="disabled")
            self._category_name_entry.configure(state="disabled")
            self._white_list.configure(state="disabled")
            self._black_list.configure(state="disabled")
            self._create_button.configure(state="disabled")
            self._delete_button.configure(state="disabled")
            self._category_checkbox.configure(state=tkinter.DISABLED)

            button: customtkinter.CTkButton
            for button in self._recommender_frame_button_list:
                button.configure(state="disabled")

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        if self._frozen:
            self._category_drop_down_menu.configure(state="normal")
            self._category_name_entry.configure(state="normal")
            self._white_list.configure(state="normal")
            self._black_list.configure(state="normal")
            self._create_button.configure(state="normal")
            self._delete_button.configure(state="normal")
            self._category_checkbox.configure(state=tkinter.NORMAL)

            button: customtkinter.CTkButton
            for button in self._recommender_frame_button_list:
                button.configure(state="normal")

            # If no category is selected, return to a defined state
            if self._selected_category is None:
                self._deactivate_editing()

            self._frozen: bool = False
