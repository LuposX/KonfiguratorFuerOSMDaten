from __future__ import annotations

import customtkinter

from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
from src.osm_configurator.view.activatable import Activatable
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
        self.window = super().__init__()

        self._starting_point = CalculationPhase.NONE
        self._state_manager = state_manager
        self._calculation_controller = calculation_controller
        self._data_visualization_controller = data_visualization_controller

        #  Creating the entries on the left

        self.buttons = [
            customtkinter.CTkButton(master=self.window, text="Data Input and Geofilter", bg_color="grey",
                                    command=self.__data_and_geofilter_pressed),
            customtkinter.CTkButton(master=self.window, text="Tag-Filter", bg_color="grey",
                                    command=self.__tag_filter_pressed),
            customtkinter.CTkButton(master=self.window, text="Reduction", bg_color="grey",
                                    command=self.__reduction_pressed),
            customtkinter.CTkButton(master=self.window, text="Attractivity", bg_color="grey",
                                    command=self.__attractivity_pressed),
            customtkinter.CTkButton(master=self.window, text="Aggregation", bg_color="grey",
                                    command=self.__aggregation_pressed)
        ]

        for button in self.buttons:
            button.pack(side="left", padx=40, pady=40)

    def activate(self):
        self.__activate_buttons()
        #  TODO: Keep the progressbar up-to-date

    def __tag_filter_pressed(self):
        self._starting_point = CalculationPhase.TAG_FILTER_PHASE
        self.__disable_buttons()
        self.__start_calculation()

    def __data_and_geofilter_pressed(self):
        self._starting_point = CalculationPhase.GEO_DATA_PHASE
        self.__disable_buttons()
        self.__start_calculation()

    def __reduction_pressed(self):
        self._starting_point = CalculationPhase.REDUCTION_PHASE
        self.__disable_buttons()
        self.__start_calculation()

    def __attractivity_pressed(self):
        self._starting_point = CalculationPhase.ATTRACTIVITY_PHASE
        self.__disable_buttons()
        self.__start_calculation()

    def __aggregation_pressed(self):
        self._starting_point = CalculationPhase.AGGREGATION_PHASE
        self.__disable_buttons()
        self.__start_calculation()

    def __disable_buttons(self):
        """
        Makes a list of buttons non-clickable
        """
        counter = 0
        starting_index = self._starting_point.get_order()

        for button in self.buttons:
            button.config(state="disable")
            if counter == starting_index:
                button['bg_color'] = "yellow"
            elif counter < starting_index:
                button['bg_color'] = "green"
            counter += 1

    def __activate_buttons(self):
        """
        Reactivates the buttons of the class and makes them clickable again
        """
        for button in self.buttons:
            button.config(state="enable")

    def __stop_calculation(self):
        pass

    def __start_calculation(self):
        """
        Starts the calculation:
            Adds the progressbar and the button to stop the calculation to the window
            Calls the according controller
        """
        self.progressbar = \
            customtkinter.CTkProgressBar(master=self.window, progress_color="green", width=400,
                                         orientation="horizontal") \
            .pack(side="right", padx=40, pady=40)

        cancel_button = \
            customtkinter.CTkButton(master=self.window, text="Cancel", bg_color="red", command=self.__stop_calculation)\
            .pack(side="right", padx=40, pady=40)

        self.buttons.append(cancel_button)

        self._calculation_controller.start_calculations(self._starting_point)
