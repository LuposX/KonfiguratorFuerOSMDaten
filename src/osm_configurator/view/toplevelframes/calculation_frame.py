from __future__ import annotations

import customtkinter

from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.states.calculation_states_enum import CalculationStates
from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.calculation_controller_interface import ICalculationController
from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
from src.osm_configurator.view.states.view_constants import ViewConstants

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.calculation_controller_interface import ICalculationController
    from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.states.view_constants import ViewConstants


class CalculationFrame(TopLevelFrame, Activatable, customtkinter.CTkToplevel):
    """
    This frame lets the user start the calculation from a selected phase, indicated by different buttons.
    Once a calculation is started, there will be a progressbar shown, the different buttons will be deactivated
    and the current calculation-phase will be shown.
    A cancel-Button is provided to stop the calculation.
    The CalculationFrame shows popups, if an error occurs in the calculations.
    """

    def __init__(self, state_manager: StateManager, calculation_controller: ICalculationController,
                 data_visualization_controller: IDataVisualizationController):
        """
        This method creates a CalculationFrame that will let the user start the calculation
        and shows the calculation progress.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch to another state.
             calculation_controller (calculation_controller.CalculationController): Respective controller.
             data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller.
        """
        window = super().__init__()

        self._starting_point = 0
        self._state_manager = state_manager
        self._calculation_controller = calculation_controller
        self._data_visualization_controller = data_visualization_controller

        #  Creating the entries on the left

        self.buttons = [
            customtkinter.CTkButton(window, text="Data Input and Geofilter", bg_color="grey",
                                    command=self.__data_and_geofilter_pressed),
            customtkinter.CTkButton(window, text="Tag-Filter", bg_color="grey",
                                    command=self.__tag_filter_pressed),
            customtkinter.CTkButton(window, text="Reduction", bg_color="grey",
                                    command=self.__reduction_pressed),
            customtkinter.CTkButton(window, text="Attractivity", bg_color="grey",
                                    command=self.__attractivity_pressed),
            customtkinter.CTkButton(window, text="Aggregation", bg_color="grey",
                                    command=self.__aggregation_pressed)
        ]

        for button in self.buttons:
            button.pack(side="left", padx=40, pady=40)

    def activate(self):
        self.__activate_buttons()

    def __tag_filter_pressed(self):
        self._starting_point = CalculationStates.TAG_FILTER.value
        self.__disable_buttons()

    def __data_and_geofilter_pressed(self):
        self._starting_point = CalculationStates.DATA_INPUT_AND_GEO_FILTER.value
        self.__disable_buttons()

    def __reduction_pressed(self):
        self._starting_point = CalculationStates.REDUCTION.value
        self.__disable_buttons()

    def __attractivity_pressed(self):
        self._starting_point = CalculationStates.ATTRACTIVITY.value
        self.__disable_buttons()

    def __aggregation_pressed(self):
        self._starting_point = CalculationStates.AGGREGATION.value
        self.__disable_buttons()

    def __disable_buttons(self):
        """
        Makes a list of buttons non-clickable
        """
        counter = 0
        starting_point = self._starting_point

        for button in self.buttons:
            button.config(state="disable")
            if counter == starting_point:
                button['bg'] = "yellow"
            elif counter < starting_point:
                button['bg'] = "green"
            counter += 1

    def __activate_buttons(self):
        """
        Reactivates the buttons of the class and makes them clickable again
        """
        for button in self.buttons:
            button.config(state="enable")
