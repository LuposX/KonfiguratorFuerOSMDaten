from __future__ import annotations

from functools import partial

import customtkinter

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.scrollbar_constants as scrollbar_constants_i
import src.osm_configurator.view.constants.segmented_button_constants as segmented_button_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i

import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

import src.osm_configurator.model.project.configuration.category as category_i

import src.osm_configurator.view.utilityframes.reduction_calculation_frame as reduction_calculation_frame_i
import src.osm_configurator.view.utilityframes.reduction_default_value_frame as reduction_default_value_frame_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.category_controller_interface import ICategoryController

# Finals
CATEGORY_LIST_FG_COLOR: Final = "#FFFFFF"
CATEGORY_LIST_LABEL_COLOR: Final = "#FFFFFF"
ELEMENT_BORDER_DISTANCE: Final = 40

CATEGORY_BUTTON_HEIGHT: Final = 42

PADX: Final = 4
PADY: Final = 4


class ReductionFrame(TopLevelFrame):
    """
    This frame lets the user edit the reduction of all the categories.
    It will consist of a list on the left to choose a category.
    On the right will be two sub-frames to change inbetween.
    On the right are two interchangeable sub-frames: One frame provides the configuration-options on how to
    calculate the Reduction. The other frame provides the default calculation-values.
    """

    def __init__(self, state_manager: StateManager, category_controller: ICategoryController):
        """
        This method creates a ReductionFrame that lets the user edit the reduction of all the categories.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            category_controller (category_controller_interface.ICategoryController): The control the frame will call to get access to the Categories
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

        # starts unfrozen
        self._frozen: bool = False

        # Remembering what category was pressed last
        self._last_pressed_category_button: customtkinter.CTkButton = None

        self._calculation_shown: bool = False
        self._default_values_shown: bool = False

        # Setting up the grid, it is a 2x2 grid, where the second column and row are heavier weighted
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)

        # Making a scrollable Frame for the Categories to be placed on
        self._category_list_frame: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(master=self,
                                                                                                       width=int(
                                                                                                           frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                                       height=int(
                                                                                                           frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value - ELEMENT_BORDER_DISTANCE),
                                                                                                       corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
                                                                                                       fg_color=CATEGORY_LIST_FG_COLOR,
                                                                                                       scrollbar_fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value,
                                                                                                       scrollbar_button_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_COLOR.value,
                                                                                                       scrollbar_button_hover_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_HOVER_COLOR.value,
                                                                                                       label_text="Categories:",
                                                                                                       label_text_color=CATEGORY_LIST_LABEL_COLOR)
        self._category_list_frame.grid(row=0, column=0, rowspan=2, columnspan=1)

        # The Categories displayed on the scrollable Frame
        # Starts empty
        self._category_button_list: [customtkinter.CTkButton] = []

        # The segmented Button, for choosing between calculation or reduction settings
        self._segmented_button_values: List[str] = ["Reduction", "Default Values"]
        self._segmented_button: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self,
                                                                                                    width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (
                                                                                                                3 / 4) - ELEMENT_BORDER_DISTANCE,
                                                                                                    height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (
                                                                                                                1 / 6) - ELEMENT_BORDER_DISTANCE,
                                                                                                    corner_radius=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_CORNER_RADIUS.value,
                                                                                                    fg_color=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_FG_COLOR.value,
                                                                                                    selected_color=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_SELECTED_COLOR.value,
                                                                                                    selected_hover_color=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_SELECTED_HOVER_COLOR.value,
                                                                                                    unselected_color=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_UNSELECTED_COLOR.value,
                                                                                                    unselected_hover_color=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_UNSELECTED_HOVER_COLOR.value,
                                                                                                    text_color=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_TEXT_COLOR.value,
                                                                                                    text_color_disabled=segmented_button_constants_i.SegmentedButtonConstants.SEGMENTED_BUTTON_TEXT_COLOR_DISABLED.value,
                                                                                                    values=self._segmented_button_values,
                                                                                                    dynamic_resizing=True,
                                                                                                    command=self._segmented_button_pressed)
        self._segmented_button.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="NSEW")

        # Making the supFrames used under the segmented Button to edit calculation and reduction
        # They don't get set into the grid directly
        self._reduction_calculation_frame: reduction_calculation_frame_i.ReductionCalculationFrame = reduction_calculation_frame_i.ReductionCalculationFrame(
            self, frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (3 / 4),
            frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (5 / 6))

        self._reduction_default_value_frame: reduction_default_value_frame_i.ReductionDefaultValueFrame = reduction_default_value_frame_i.ReductionDefaultValueFrame(
            self, frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (3 / 4),
            frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (5 / 6),
            self._state_manager)

    def activate(self):
        # There has no button been pressed yet
        self._last_pressed_category_button: customtkinter.CTkButton = None

        # Getting all categories
        all_categories: [category_i.Category] = self._category_controller.get_list_of_categories()

        self._categories: [category_i.Category] = []

        # Only adding active Categories
        category: category_i.Category
        for category in all_categories:
            if category.is_active():
                self._categories.append(category)

        # Deleting all buttons from the category list
        category_button: customtkinter.CTkButton
        for category_button in self._category_button_list:
            category_button.destroy()
        self._category_button_list: [customtkinter.CTkButton] = []

        # now filling the category list
        button_id: int = 0
        active_category: category_i.Category
        for active_category in self._categories:
            button: customtkinter.CTkButton = customtkinter.CTkButton(master=self._category_list_frame,
                                                                      width=int(
                                                                          frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 4 - ELEMENT_BORDER_DISTANCE) - ELEMENT_BORDER_DISTANCE,
                                                                      height=CATEGORY_BUTTON_HEIGHT,
                                                                      corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                                                      border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                                                      fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                                                      hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                                                      border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                                                      text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                                                      text=active_category.get_category_name(),
                                                                      command=partial(self._category_button_pressed,
                                                                                      button_id))
            button.grid(row=button_id, column=0, rowspan=1, columnspan=1, pady=PADY, padx=PADX)
            self._category_button_list.append(button)
            button_id += 1

        if len(self._categories) == 0:
            self._selected_category: category_i.Category = None
        else:
            self._selected_category: category_i.Category = self._categories[0]
            # If category 0 is selected, we also automatically select this one and disable the corrosponding button
            self._category_button_list[0].configure(state="disabled",
                                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
                                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)

        # First showing the calculation frame
        self._reduction_default_value_frame.grid_remove()
        self._reduction_calculation_frame.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="NSEW")
        self._reduction_calculation_frame.load_category(self._selected_category)
        self._calculation_shown: bool = True
        self._default_values_shown: bool = False

        self._segmented_button.set(self._segmented_button_values[0])

    def _segmented_button_pressed(self, value: str):

        if value == self._segmented_button_values[0]:
            self._reduction_default_value_frame.grid_remove()
            self._reduction_calculation_frame.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="NSEW")
            self._reduction_calculation_frame.load_category(self._selected_category)
            self._calculation_shown: bool = True
            self._default_values_shown: bool = False
        elif value == self._segmented_button_values[1]:
            self._reduction_calculation_frame.grid_remove()
            self._reduction_default_value_frame.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="NSEW")
            self._reduction_default_value_frame.load_category(self._selected_category)
            self._calculation_shown: bool = False
            self._default_values_shown: bool = True
        else:
            alert_pop_up_i.AlertPopUp("Could not change to frame '" + value + "'!")

    def _category_button_pressed(self, button_id: int):

        # First activating all buttons, so they don't end up all disabled
        button: customtkinter.CTkButton
        for button in self._category_button_list:
            button.configure(state="normal", text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value)

        # Now disabling selected button
        self._category_button_list[button_id].configure(state="disabled",
                                                        text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
                                                        fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value)

        # Remembering that button
        self._last_pressed_category_button: customtkinter.CTkButton = self._category_button_list[button_id]

        # Selecting the category
        self._selected_category: category_i.Category = self._categories[button_id]

        if self._calculation_shown:
            self._reduction_calculation_frame.load_category(self._selected_category)
        elif self._default_values_shown:
            self._reduction_default_value_frame.load_category(self._selected_category)
        else:
            alert_pop_up_i.AlertPopUp("Could not load category!\nFrame has been refreshed!")
            # Refresh Frame, since something went wrong!
            self.activate()

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        if not self._frozen:
            button: customtkinter.CTkButton
            for button in self._category_button_list:
                button.configure(state="disabled")

            self._segmented_button.configure(state="disabled")

            self._reduction_calculation_frame.freeze()
            self._reduction_default_value_frame.freeze()

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        if self._frozen:
            button: customtkinter.CTkButton
            for button in self._category_button_list:
                button.configure(state="normal")

            # Disabling the last pressed category button again!
            if self._last_pressed_category_button is not None:
                self._last_pressed_category_button.configure(state="disabled",
                                                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value,
                                                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value)

            self._segmented_button.configure(state="normal")

            self._reduction_calculation_frame.freeze()
            self._reduction_default_value_frame.freeze()

            self._frozen: bool = False
