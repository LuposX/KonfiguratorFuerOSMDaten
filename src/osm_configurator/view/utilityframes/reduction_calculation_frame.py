from __future__ import annotations

import tkinter

import customtkinter

import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.category_controller_interface

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.check_box_constants as check_box_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.switch_constants as switch_constants_i
import \
    src.osm_configurator.model.project.configuration.calculation_method_of_area_enum as calculation_method_of_area_enum_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

from src.osm_configurator.view.freezable import Freezable

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typing import Final
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.control.category_controller_interface import ICategoryController

# Finals
ELEMENT_BORDER_DISTANCE: Final = 20


class ReductionCalculationFrame(customtkinter.CTkFrame, Freezable):
    """
    This frame provides the ability to the user to set how the calculation of the reduction of a category
    will be done.
    This is a subframe from the ReductionFrame.
    """

    def __init__(self, parent: TopLevelFrame, width: int, height: int):
        """
        This method creates a ReductionCalculationFrame that lets the user edit the calculation of the reduction of
        Categories.
        Args:
            parent (top_level_frame.TopLevelFrame): This is the parent frame of this frame. The frame will be located here.
            width (int): The width, this frame shall have
            height (int): The height, this frame shall have
        """
        super().__init__(master=parent,
                         width=width,
                         height=height,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.SUB_FRAME_FG_COLOR.value)

        self._parent: TopLevelFrame = parent
        self._width: int = width
        self._height: int = height
        # At the beginning, no Category is loaded
        self._selected_category: category_i.Category = None

        # starts unfrozen
        self._frozen: bool = False

        # Making the grid
        # It is a 4x3 grid, with equal weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # The calculate Area Checkbox
        self._calculate_area_checkbox: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(master=self,
                                                                                             width=self._width - ELEMENT_BORDER_DISTANCE,
                                                                                             height=int(
                                                                                                 self._height / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                             corner_radius=check_box_constants_i.CheckBoxConstants.CHECK_BOX_CORNER_RADIUS.value,
                                                                                             border_width=check_box_constants_i.CheckBoxConstants.CHECK_BOX_BORDER_WIDTH.value,
                                                                                             fg_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_FG_COLOR.value,
                                                                                             hover_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_HOVER_COLOR.value,
                                                                                             text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value,
                                                                                             text="Calculate Area")
        self._calculate_area_checkbox.grid(row=2, column=0, rowspan=1, columnspan=3)

        # The switch between Calculate site Area and Calculate Building Area
        # Labels
        self._calculate_site_area_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                         width=int(
                                                                                             self._width / 3 - ELEMENT_BORDER_DISTANCE),
                                                                                         height=int(
                                                                                             self._height / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                         corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                         fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                         text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                         anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                         text="Calculate\nsite Area")
        self._calculate_site_area_label.grid(row=3, column=0, rowspan=1, columnspan=1, pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                             padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value)

        self._calculate_building_area_label: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self,
                                                                                             width=int(
                                                                                                 self._width / 3 - ELEMENT_BORDER_DISTANCE),
                                                                                             height=int(
                                                                                                 self._height / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                             corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                                                                             fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                                                                             text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                                                                             anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                                                                             text="Calculate\nBuilding Area")
        self._calculate_building_area_label.grid(row=3, column=2, rowspan=1, columnspan=1, pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADY.value,
                                                 padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PADX.value)

        # The switch inbetween
        self._site_building_switch: customtkinter.CTkSwitch = customtkinter.CTkSwitch(master=self,
                                                                                      width=int(
                                                                                          self._width / 3 - ELEMENT_BORDER_DISTANCE),
                                                                                      height=int(
                                                                                          self._height / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                      corner_radius=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_CORNER_RADIUS.value,
                                                                                      border_width=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_BORDER_WIDTH.value,
                                                                                      fg_color=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_FG_COLOR.value,
                                                                                      border_color=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_BORDER_COLOR.value,
                                                                                      progress_color=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_PROGRESS_COLOR.value,
                                                                                      button_color=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_BUTTON_COLOR.value,
                                                                                      button_hover_color=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_BUTTON_HOVER_COLOR.value,
                                                                                      text_color=switch_constants_i.SwitchConstants.SWITCH_CONSTANTS_TEXT_COLOR.value,
                                                                                      state="normal",
                                                                                      text="")
        self._site_building_switch.grid(row=3, column=1, rowspan=1, columnspan=1)

        # The Checkbox for Calculate Floor Area
        self._calculate_floor_area_checkbox: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(master=self,
                                                                                                   width=self._width - ELEMENT_BORDER_DISTANCE,
                                                                                                   height=int(
                                                                                                       self._height / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                                   corner_radius=check_box_constants_i.CheckBoxConstants.CHECK_BOX_CORNER_RADIUS.value,
                                                                                                   border_width=check_box_constants_i.CheckBoxConstants.CHECK_BOX_BORDER_WIDTH.value,
                                                                                                   fg_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_FG_COLOR.value,
                                                                                                   hover_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_HOVER_COLOR.value,
                                                                                                   text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value,
                                                                                                   text="Calculate Floor Area")
        self._calculate_floor_area_checkbox.grid(row=1, column=0, rowspan=1, columnspan=3)

        # The Checkbox for Strictly Use Default Values
        self._strictly_use_default_values_checkbox = customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(master=self,
                                                                                                           width=self._width - ELEMENT_BORDER_DISTANCE,
                                                                                                           height=int(
                                                                                                               self._height / 4 - ELEMENT_BORDER_DISTANCE),
                                                                                                           corner_radius=check_box_constants_i.CheckBoxConstants.CHECK_BOX_CORNER_RADIUS.value,
                                                                                                           border_width=check_box_constants_i.CheckBoxConstants.CHECK_BOX_BORDER_WIDTH.value,
                                                                                                           fg_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_FG_COLOR.value,
                                                                                                           hover_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_HOVER_COLOR.value,
                                                                                                           text_color=check_box_constants_i.CheckBoxConstants.CHECK_BOX_TEXT_COLOR.value,
                                                                                                           text="Strictly use default values")
        self._strictly_use_default_values_checkbox.grid(row=0, column=0, rowspan=1, columnspan=3)

    def load_category(self, category: category_i.Category) -> bool:
        """
        Loads in the given Category, so this category can be edited.

        Args:
            category (category.Category): The Category that shall be loaded

        Returns:
            bool: True if category was successfully loaded, False else
        """

        self._selected_category: category_i.Category = category

        if self._selected_category is None:
            self._deactivate_editing()
        else:
            self._activate_editing()

            # Setting all the checkboxes, and maybe deactivating settings if needed
            if self._selected_category.get_strictly_use_default_values():
                self._strictly_use_default_values_checkbox.select()
            else:
                self._deactivate_below_strictly_use_default_values()
                self._strictly_use_default_values_checkbox.deselect()

            if self._selected_category.get_attribute(attribute_enum_i.Attribute.FLOOR_AREA):
                self._calculate_floor_area_checkbox.select()
            else:
                self._calculate_floor_area_checkbox.deselect()

            if self._selected_category.get_attribute(attribute_enum_i.Attribute.PROPERTY_AREA):
                self._calculate_area_checkbox.select()
            else:
                self._deactivate_switch()
                self._calculate_area_checkbox.deselect()

            method: calculation_method_of_area_enum_i.CalculationMethodOfArea = category.get_calculation_method_of_area()

            if method == calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_SITE_AREA:
                self._site_building_switch.deselect()
            elif method == calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_BUILDING_AREA:
                self._site_building_switch.select()
            else:
                raise ValueError("Category has to be either one of the calculation Methods!")

            # Category loaded, so return True
            return True

    def _calculate_area_checkbox_edited(self):
        if self._calculate_area_checkbox.get() == 1:
            self._activate_switch()

            if not self._selected_category.set_attribute(attribute_enum_i.Attribute.PROPERTY_AREA, True):
                alert_pop_up_i.AlertPopUp("Could not activate calculation of area!")
                # reloading the category to make the switch go back, to what is actually set
                self.load_category(self._selected_category)

        else:
            self._deactivate_switch()

            if not self._selected_category.set_attribute(attribute_enum_i.Attribute.PROPERTY_AREA, False):
                alert_pop_up_i.AlertPopUp("Could not deactivate calculation of area!")
                # reloading the category to make the switch go back, to what is actually set
                self.load_category(self._selected_category)

    def _site_building_switch_edited(self):
        if self._site_building_switch.get() == 1:
            if not self._selected_category.set_calculation_method_of_area(
                    calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_BUILDING_AREA):
                alert_pop_up_i.AlertPopUp("Could not switch calculation Method!")
                # reloading frame
                self.load_category(self._selected_category)
        else:
            if not self._selected_category.set_calculation_method_of_area(
                    calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_SITE_AREA):
                alert_pop_up_i.AlertPopUp("Could not switch calculation Method!")
                # reloading frame
                self.load_category(self._selected_category)

    def _calculate_floor_area_checkbox_edited(self):
        if self._calculate_floor_area_checkbox.get() == 1:
            if not self._selected_category.set_attribute(attribute_enum_i.Attribute.FLOOR_AREA, True):
                alert_pop_up_i.AlertPopUp("Could not activate calculation of floor area!")
                # reloading frame
                self.load_category(self._selected_category)
        else:
            if not self._selected_category.set_attribute(attribute_enum_i.Attribute.FLOOR_AREA, False):
                alert_pop_up_i.AlertPopUp("Could not deactivate calculation of floor area!")
                # reloading frame
                self.load_category(self._selected_category)

    def _strictly_use_default_values_checkbox_edited(self):
        if self._strictly_use_default_values_checkbox.get() == 1:
            self._activate_below_strictly_use_default_values()
            if not self._selected_category.set_strictly_use_default_values(True):
                alert_pop_up_i.AlertPopUp("Could not activate strictly using default values!")
                # refreshing frame
                self.load_category(self._selected_category)
        else:
            if not self._selected_category.set_strictly_use_default_values(False):
                alert_pop_up_i.AlertPopUp("Could not deactivate strictly using default values!")
                # refreshing frame
                self.load_category(self._selected_category)

    def _deactivate_editing(self):
        # Deactivates the WHOLE Editing
        self._strictly_use_default_values_checkbox.configure(state=tkinter.DISABLED)

        self._deactivate_below_strictly_use_default_values()

    def _activate_editing(self):
        # Activating all Checkboxes and switches, so they can be edited
        self._strictly_use_default_values_checkbox.configure(state=tkinter.NORMAL)

        self._activate_below_strictly_use_default_values()

    def _deactivate_below_strictly_use_default_values(self):
        # If strictly use default Values is off, the rest is irrelevant
        self._calculate_floor_area_checkbox.configure(state=tkinter.DISABLED)

        self._calculate_area_checkbox.configure(state=tkinter.DISABLED)

        self._deactivate_switch()

    def _activate_below_strictly_use_default_values(self):
        self._calculate_floor_area_checkbox.configure(state=tkinter.NORMAL)

        self._calculate_area_checkbox.configure(state=tkinter.NORMAL)

        self._activate_switch()

    def _deactivate_switch(self):
        self._site_building_switch.configure(state="disabled")

    def _activate_switch(self):
        self._site_building_switch.configure(state="normal")

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        if not self._frozen:
            self._strictly_use_default_values_checkbox.configure(state=tkinter.DISABLED)
            self._calculate_floor_area_checkbox.configure(state=tkinter.DISABLED)
            self._calculate_area_checkbox.configure(state=tkinter.DISABLED)
            self._site_building_switch.configure(state="disabled")

            self._frozen: bool = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        if self._frozen:
            self._strictly_use_default_values_checkbox.configure(state=tkinter.NORMAL)
            self._calculate_floor_area_checkbox.configure(state=tkinter.NORMAL)
            self._calculate_area_checkbox.configure(state=tkinter.NORMAL)
            self._site_building_switch.configure(state="normal")

            # Deactivating checkboxes again, depending on what is checked and loaded
            if self._selected_category is None:
                self._deactivate_editing()
            elif self._strictly_use_default_values_checkbox.get() == 0:
                self._deactivate_below_strictly_use_default_values()
            elif self._calculate_area_checkbox.get() == 0:
                self._deactivate_switch()

            self._frozen: bool = False
