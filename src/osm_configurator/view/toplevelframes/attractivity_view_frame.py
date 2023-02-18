from __future__ import annotations

from functools import partial

import customtkinter

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.category_controller_interface

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.scrollbar_constants as scrollbar_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.attractivity_attribute as attractivity_attribute_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i

import src.osm_configurator.view.states.state_name_enum as state_name_enum_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.category_controller_interface import ICategoryController

# Finals
SCROLLABLE_FRAME_FG_COLOR: Final = scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value

ELEMENT_BORDER_DISTANCE: Final = 20
CATEGORY_BUTTON_HEIGHT: Final = 42

PADY: Final = 2
PADX: Final = 2


class AttractivityViewFrame(TopLevelFrame):
    """
    This frame shows a list with all categories, their attractivity attributes and how they are calculated.
    This is only a visualisation and therefore a non-edit Frame.
    """

    def __init__(self, state_manager: StateManager, category_controller: ICategoryController):
        """
        This method creates an AttractivityViewFrame showing a lList of containing all categories,
        their according attractivity attributes and how they are calculated.

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

        # Setting private Attributes
        self._state_manager: StateManager = state_manager
        self._category_controller: ICategoryController = category_controller

        self._categories: [category_i.Category] = []
        self._selected_category: category_i.Category = None

        self._category_button_list: [customtkinter.CTkButton] = []

        self._attractivity_name_labels: [customtkinter.CTkLabel] = []
        self._area_factor_labels: [customtkinter.CTkLabel] = []
        self._floors_factor_labels: [customtkinter.CTkLabel] = []
        self._ground_area_factor_labels: [customtkinter.CTkLabel] = []
        self._base_attractivity_labels: [customtkinter.CTkLabel] = []

        # Making the grid
        # it is a 9x3 grid
        # it has 9 columns, because we need to display, categories, attratcivity-attribute and 4 factors +
        # we want to have space on the left and right  and between
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, weight=2)
        self.grid_columnconfigure(5, weight=2)
        self.grid_columnconfigure(6, weight=2)
        self.grid_columnconfigure(7, weight=2)
        self.grid_columnconfigure(8, weight=1)

        # The middle row is heavier weighted, because that is where the scrollable frames will be
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_rowconfigure(2, weight=1)

        # Making the scrollabel Frame that holds the Category Buttons
        self._category_scrollable_frame: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(
            master=self,
            width=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (3 / 16)),
            height=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (6 / 8)),
            corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
            fg_color=SCROLLABLE_FRAME_FG_COLOR,
            scrollbar_fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value,
            scrollbar_button_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_COLOR.value,
            scrollbar_button_hover_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_HOVER_COLOR.value)
        self._category_scrollable_frame.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="NSEW")

        # Making the Scrollable Frame that holds the Attractivity-Attribute information
        self._attractivity_scrollable_frame: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(
            master=self,
            width=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (10 / 16)),
            height=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (6 / 8)),
            corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
            fg_color=SCROLLABLE_FRAME_FG_COLOR,
            scrollbar_fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value,
            scrollbar_button_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_COLOR.value,
            scrollbar_button_hover_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_HOVER_COLOR.value)
        self._attractivity_scrollable_frame.grid(row=1, column=3, rowspan=1, columnspan=5, sticky="NSEW")
        # This frame has 5 columns, where the labels will be placed
        self._attractivity_scrollable_frame.grid_columnconfigure(0, weight=1)
        self._attractivity_scrollable_frame.grid_columnconfigure(1, weight=1)
        self._attractivity_scrollable_frame.grid_columnconfigure(2, weight=1)
        self._attractivity_scrollable_frame.grid_columnconfigure(3, weight=1)
        self._attractivity_scrollable_frame.grid_columnconfigure(4, weight=1)

        # Making all the Labels that will be above tha ScrollabelFrames
        # Labels are choosen, because making a label in the scrollable frame would be just a simple title
        # and here we want especially for the attractiviyt scrollable frame, to have it segmented in different parts,
        # that scale up with the window, so deference the labels shown in the frame and categories them

        # The Categories Label
        self._categories_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                width=int(
                                                                                    frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                3 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                                height=int(
                                                                                    frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                                corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                text="Categories:")
        self._categories_label.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="W")

        # The Attractivity Attribute Label
        self._attractivity_attribute_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                            width=int(
                                                                                                frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                            2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                                            height=int(
                                                                                                frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                            1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                                            corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                            fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                            text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                            anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                            padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                            pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                            text="Attractivity-Attribute:")
        self._attractivity_attribute_label.grid(row=0, column=3, rowspan=1, columnspan=1, sticky="W")

        # The Area Factor Label
        self._area_factor_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                 width=int(
                                                                                     frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                 2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                                 height=int(
                                                                                     frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                 1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                                 corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                 fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                 text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                 anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                 padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                 pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                 text="Area-Factor:")
        self._area_factor_label.grid(row=0, column=4, rowspan=1, columnspan=1, sticky="W")

        # Numbers of Floors Factor
        self._number_of_floors_factor_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                             width=int(
                                                                                       frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                   2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                                             height=int(
                                                                                       frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                   1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                                             corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                             fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                             text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                             anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                             padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                             pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                             text="Numbers-of-Floors-Factor:")
        self._number_of_floors_factor_label.grid(row=0, column=5, rowspan=1, columnspan=1, sticky="W")

        # Floor Area Label
        self._floor_area_factor_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                       width=int(
                                                                                            frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                        2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                                       height=int(
                                                                                            frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                        1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                       fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                       text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                       anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                       padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                       pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                       text="Floor-Area-Factor:")
        self._floor_area_factor_label.grid(row=0, column=6, rowspan=1, columnspan=1, sticky="W")

        # Base Attractivity Label
        self._base_attractivity_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                       width=int(
                                                                                           frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                       2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                                       height=int(
                                                                                           frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                       1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                                       corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                       fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                       text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                       anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                       padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value,
                                                                                       pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                                                       text="Base-Attractivity-Factor:")
        self._base_attractivity_label.grid(row=0, column=6, rowspan=1, columnspan=1, sticky="W")

        # The Button to go back to edit the attractivities
        self._edit_attractivity_button: customtkinter.CTkButton = customtkinter.CTkButton(
            master=self,
            width=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (2 / 16)) - ELEMENT_BORDER_DISTANCE,
            height=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (1 / 8)) - ELEMENT_BORDER_DISTANCE,
            corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
            text="Edit Attractivity",
            command=self._edit_attractivity_button_pressed)
        self._edit_attractivity_button.grid(row=2, column=4, rowspan=1, columnspan=1)

    def activate(self):
        # First getting all the active categories
        all_categories: [category_i.Category] = self._category_controller.get_list_of_categories()

        self._categories: [category_i.Category] = []

        category: category_i.Category
        for category in all_categories:
            if category.is_active():
                self._categories.append(category)

        # Deleting everything on the scrollable Frame for categories
        button: customtkinter.CTkButton
        for button in self._category_button_list:
            button.destroy()
        self._category_button_list: [customtkinter.CTkButton] = []

        # Selecting a category
        if len(self._categories) == 0:
            self._selected_category: category_i.Category = None
        else:
            self._selected_category: category_i.Category = self._categories[0]

        # Adding all categories to the category scrollable frame
        button_id: int = 0
        active_category: category_i.Category
        for active_category in self._categories:
            new_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self._category_scrollable_frame,
                                                                          width=int(
                                                                              frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                          3 / 16) - ELEMENT_BORDER_DISTANCE),
                                                                          height=CATEGORY_BUTTON_HEIGHT,
                                                                          corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                          border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                          fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                          hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                          border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                          text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                          text=active_category.get_category_name(),
                                                                          pady=PADY,
                                                                          command=partial(self._category_button_pressed,
                                                                                          button_id))
            new_button.grid(row=button_id, column=0, rowspan=1, columnspan=1)
            button_id += 1
            self._category_button_list.append(new_button)

        # Loading a Category
        self._load_category(self._selected_category)

    def _load_category(self, category: category_i.Category):

        # First deleting all labels on the attractivity scrollable frame, to make room for new ones
        self._delete_attractivity_scrollable_frame()

        if category is not None:
            all_attractivities: [
                attractivity_attribute_i.AttractivityAttribute] = category.get_attractivity_attributes()

            row_for_tuple: int = 0
            attractivity: attractivity_attribute_i.AttractivityAttribute
            for attractivity in all_attractivities:
                # This tuple has:
                # name of Attractivity,
                # Area Factor,
                # Number of Floors Factor,
                # Floor Area Factor,
                # Base Factor
                # In that specific order!
                label_name_tuple = (attractivity.get_attractivity_attribute_name(),
                                    attractivity.get_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA),
                                    attractivity.get_attribute_factor(attribute_enum_i.Attribute.NUMER_OF_FLOOR),
                                    attractivity.get_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA),
                                    attractivity.get_base_factor())
                self._add_attractivity_to_scrollable_frame(label_name_tuple, row_for_tuple)
                row_for_tuple += 1

    def _delete_attractivity_scrollable_frame(self):
        # Deleting all labels in every list
        name_label: customtkinter.CTkLabel
        for name_label in self._attractivity_name_labels:
            name_label.destroy()
        self._attractivity_name_labels: [customtkinter.CTkLabel] = []

        area_label: customtkinter.CTkLabel
        for area_label in self._area_factor_labels:
            area_label.destroy()
        self._area_factor_labels: [customtkinter.CTkLabel] = []

        floors_label: customtkinter.CTkLabel
        for floors_label in self._floors_factor_labels:
            floors_label.destroy()
        self._floors_factor_labels: [customtkinter.CTkLabel] = []

        ground_area_label: customtkinter.CTkLabel
        for ground_area_label in self._ground_area_factor_labels:
            ground_area_label.destroy()
        self._ground_area_factor_labels: [customtkinter.CTkLabel] = []

        base_label: customtkinter.CTkLabel
        for base_label in self._base_attractivity_labels:
            base_label.destroy()
        self._base_attractivity_labels: [customtkinter.CTkLabel] = []

    def _add_attractivity_to_scrollable_frame(self, attractivity_tuple, row: int):
        name_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self._attractivity_scrollable_frame,
                                                                    width=int(
                                                                        frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                    2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                    height=int(
                                                                        frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                    1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                    corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                    fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                    text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                    anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                    padx=PADX,
                                                                    pady=PADY,
                                                                    text=attractivity_tuple[0])
        name_label.grid(row=row, column=0, rowspan=1, columnspan=1)
        self._attractivity_name_labels.append(name_label)

        area_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self._attractivity_scrollable_frame,
                                                                    width=int(
                                                                        frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                    2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                    height=int(
                                                                        frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                    1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                    corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                    fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                    text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                    anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                    padx=PADX,
                                                                    pady=PADY,
                                                                    text=attractivity_tuple[1])
        area_label.grid(row=row, column=1, rowspan=1, columnspan=1)
        self._area_factor_labels.append(area_label)

        floor_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self._attractivity_scrollable_frame,
                                                                     width=int(
                                                                         frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                     2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                     height=int(
                                                                         frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                     1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                     corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                     fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                     text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                     anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                     padx=PADX,
                                                                     pady=PADY,
                                                                     text=attractivity_tuple[2])
        floor_label.grid(row=row, column=2, rowspan=1, columnspan=1)
        self._floors_factor_labels.append(floor_label)

        ground_area_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self._attractivity_scrollable_frame,
                                                                           width=int(
                                                                               frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                           2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                           height=int(
                                                                               frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                           1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                           corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                           fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                           text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                           anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                           padx=PADX,
                                                                           pady=PADY,
                                                                           text=attractivity_tuple[3])
        ground_area_label.grid(row=row, column=3, rowspan=1, columnspan=1)
        self._ground_area_factor_labels.append(ground_area_label)

        base_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self._attractivity_scrollable_frame,
                                                                    width=int(
                                                                        frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                    2 / 16)) - ELEMENT_BORDER_DISTANCE,
                                                                    height=int(
                                                                        frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                    1 / 8)) - ELEMENT_BORDER_DISTANCE,
                                                                    corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                    fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                    text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                    anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                    padx=PADX,
                                                                    pady=PADY,
                                                                    text=attractivity_tuple[4])
        base_label.grid(row=row, column=4, rowspan=1, columnspan=1)
        self._base_attractivity_labels.append(base_label)

    def _category_button_pressed(self, button_id):

        # First activating all buttons, to make sure that not all end up disabled
        button: customtkinter.CTkButton
        for button in self._category_button_list:
            button.configure(state="normal",
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value)

        # Disabling pressed button, to show what is selected and so it can't be pressed twice
        # (pressing twice wouldn't really be an issue but would serve no purpose)
        pressed_button: customtkinter.CTkButton = self._category_button_list[button_id]
        pressed_button.configure(state="disabled",
                                 fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value,
                                 text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED)

        self._load_category(self._categories[button_id])

    def _edit_attractivity_button_pressed(self):
        if not self._state_manager.change_state(state_name_enum_i.StateName.ATTRACTIVITY_EDIT):
            alert_pop_up_i.AlertPopUp("Changing to edit Attractivity Failed!")
