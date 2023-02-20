from __future__ import annotations

from functools import partial

import customtkinter

import tkinter

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.aggregation_controller_interface
import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum_i

import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.scrollbar_constants as scrollbar_constants_i
import src.osm_configurator.view.constants.check_box_constants as check_box_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
    from customtkinter import CTkCheckBox

# Finals
SCROLLABLE_FRAME_FG_COLOR: Final = scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value
LABEL_TEXT_COLOR: Final = label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value
# Checkboxes are squared!
CHECKBOX_WIDTH_AND_HEIGHT: Final = 69


class AggregationFrame(TopLevelFrame):
    """
    This frame shows the aggregation page the user will interact on.
    This window provides the checkboxes to choose calculation methods and methods on how the aggregation will be calculated.
    """

    def __init__(self, state_manager: StateManager, aggregation_controller: IAggregationController):
        """
        This method creates an AggregationFrame that will be used to edit the aggregation method.

        Args:
            state_manager (state_manager.StateManager): The StateManager, the frame will call, when it wants to change to another state.
           aggregation_controller (aggregation_controller.AggregationController): Respective controller
        """
        # Starting with no master
        # Also setting other settings
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value)

        # Setting Attributes
        self._state_manager: StateManager = state_manager
        self._aggregation_controller: IAggregationController = aggregation_controller

        self._frozen: bool = False

        # Making the Grid
        # The grid is a 3x3 grid, with the middle cell beeing the biggest
        # This is done, so the frame, placed in the middle will grow in size, if the window gets resized
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=6)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_rowconfigure(2, weight=1)

        # Making the scrollable Frame in the middle
        self._aggregation_scrollable_frame: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(
            master=self,
            width=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value * (6 / 8)),
            height=int(frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value * (6 / 8)),
            corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
            fg_color=SCROLLABLE_FRAME_FG_COLOR,
            scrollbar_fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value,
            scrollbar_button_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_COLOR.value,
            scrollbar_button_hover_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_BUTTON_HOVER_COLOR.value,
            label_text="Aggregation Methods:",
            label_text_color=LABEL_TEXT_COLOR)
        self._aggregation_scrollable_frame.grid(row=1, column=1, rowspan=1, columnspan=1, sticky="NSEW")

        # Making all the checkboxes for all Aggregation Methods

        self._aggregation_methods: List[
            aggregation_method_enum_i.AggregationMethod] = self._aggregation_controller.get_aggregation_methods()
        self._aggregation_checkboxes: List[CTkCheckBox] = []

        method: aggregation_method_enum_i.AggregationMethod
        checkbox_id: int = 0
        for method in self._aggregation_methods:
            checkbox: CTkCheckBox = customtkinter.CTkCheckBox(master=self._aggregation_scrollable_frame,
                                     width=CHECKBOX_WIDTH_AND_HEIGHT,
                                     height=CHECKBOX_WIDTH_AND_HEIGHT,
                                     corner_radius=check_box_constants_i.CheckBoxConstants.CHECK_BOX_CORNER_RADIUS.value,
                                     border_width=check_box_constants_i.CheckBoxConstants.CHECK_BOX_BORDER_WIDTH.value,
                                     fg_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_FG_COLOR.value,
                                     hover_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_HOVER_COLOR.value,
                                     text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value,
                                     text=method.get_name(),
                                     command=partial(self._checkbox_edited, checkbox_id))

            # This will be overriden when activate() is called, but it is here do make sure, that checkboxes start defined
            if self._aggregation_controller.is_aggregation_method_active(method):
                checkbox.select()
                checkbox.configure(text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value)
            else:
                checkbox.deselect()
                checkbox.configure(
                    text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR_DISABLED.value)

            self._aggregation_checkboxes.append(checkbox)
            checkbox.grid(row=checkbox_id, column=0, rowspan=1, columnspan=1)
            checkbox_id += 1

    def activate(self):

        method: aggregation_method_enum_i.AggregationMethod
        checkbox_id: int = 0
        for method in self._aggregation_methods:
            if self._aggregation_controller.is_aggregation_method_active(method):
                self._aggregation_checkboxes[checkbox_id].select()
                self._aggregation_checkboxes[checkbox_id].configure(
                    text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value)
            else:
                self._aggregation_checkboxes[checkbox_id].deselect()
                self._aggregation_checkboxes[checkbox_id].configure(
                    text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR_DISABLED.value)
            checkbox_id += 1

    def _checkbox_edited(self, checkbox_id: int):
        aggregation_method: aggregation_method_enum_i.AggregationMethod = self._aggregation_methods[checkbox_id]

        active: bool = self._aggregation_checkboxes[checkbox_id].get() == 1

        if not self._aggregation_controller.set_aggregation_method_active(aggregation_method, active):
            alert_pop_up_i.AlertPopUp("Activating/Deactivating Aggregation Failed!")

        # Changing the Text Color and selecting or deselecting
        # Selecting and deseletcing might sound weird, since the suer does that
        # This is done bacause, if the setting or disbling failed, wen want to return to the previous value
        # If the setting was successfull, nothing will change
        # this ist just a fail save
        if active:
            self._aggregation_checkboxes[checkbox_id].select()
            self._aggregation_checkboxes[checkbox_id].configure(
                text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value)
        else:
            self._aggregation_checkboxes[checkbox_id].deselect()
            self._aggregation_checkboxes[checkbox_id].configure(
                text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR_DISABLED.value)

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """

        if not self._frozen:
            checkbox: CTkCheckBox
            for checkbox in self._aggregation_checkboxes:
                checkbox.configure(state=tkinter.DISABLED)

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """

        if self._frozen:
            checkbox: CTkCheckBox
            for checkbox in self._aggregation_checkboxes:
                checkbox.configure(state=tkinter.NORMAL)

            self._frozen: bool = False

