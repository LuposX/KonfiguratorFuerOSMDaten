from __future__ import annotations

import customtkinter

from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.popups.yes_no_pop_up import YesNoPopUp
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

        counter = 0  # helps to align the buttons
        for button in self.buttons:
            button.grid(row=counter, line=0, padx=40, pady=40)
            counter += 1

    def activate(self):
        self.__activate_buttons()
        #  TODO: Keep the progressbar up-to-date
        #  self._calculation_controller.get_current_calculation_process() gibt aktuellen Stand an

        #  TODO: Prüfen, ob Berechnung bereits fertig ist

    def __tag_filter_pressed(self):
        """
        Starts the calculation-routine, if the Tag-Filter-button ist pressed
        Routine:
            - Check, if calculation is possible
            - Set starting point
            - Color the buttons accordingly
            - Start calculation:
                - Show progress-bar
                - Start calculation
        """
        checker = self._calculation_controller.start_calculations(CalculationPhase.TAG_FILTER_PHASE)
        if checker != CalculationPhase.RUNNING:
            self.__calculation_start_interrupted()
            self.activate()
            return

        self._starting_point = CalculationPhase.TAG_FILTER_PHASE
        self.__disable_buttons()
        self.__show_calculation_utilities()

    def __data_and_geofilter_pressed(self):
        """
        Starts the calculation-routine, if the Geofilter-button ist pressed
        Routine:
            - Check, if calculation is possible
            - Set starting point
            - Color the buttons accordingly
            - Start calculation:
                - Show progress-bar
                - Start calculation
        """
        checker = self._calculation_controller.start_calculations(CalculationPhase.GEO_DATA_PHASE)
        if checker != CalculationPhase.RUNNING:  # Check, if changing states is possible
            self.__calculation_start_interrupted()
            self.activate()
            return

        #  Calculation in possible => Start sequence
        self._starting_point = CalculationPhase.GEO_DATA_PHASE
        self.__disable_buttons()
        self.__show_calculation_utilities()

    def __reduction_pressed(self):
        """
        Starts the calculation-routine, if the Reduction-button ist pressed
        Routine:
            - Check, if calculation is possible
            - Set starting point
            - Color the buttons accordingly
            - Start calculation:
                - Show progress-bar
                - Start calculation
        """
        checker = self._calculation_controller.start_calculations(CalculationPhase.REDUCTION_PHASE)
        if checker != CalculationPhase.RUNNING:  # Check, if changing states is possible
            self.__calculation_start_interrupted()
            self.activate()
            return

        self._starting_point = CalculationPhase.REDUCTION_PHASE
        self.__disable_buttons()
        self.__show_calculation_utilities()

    def __attractivity_pressed(self):
        """
        Starts the calculation-routine, if the Attractivity-button ist pressed
        Routine:
            - Check, if calculation is possible
            - Set starting point
            - Color the buttons accordingly
            - Start calculation:
                - Show progress-bar
                - Start calculation
        """
        checker = self._calculation_controller.start_calculations(CalculationPhase.ATTRACTIVITY_PHASE)
        if checker != CalculationPhase.RUNNING:  # Check, if changing states is possible
            self.__calculation_start_interrupted()
            self.activate()
            return

        self._starting_point = CalculationPhase.ATTRACTIVITY_PHASE
        self.__disable_buttons()
        self.__show_calculation_utilities()

    def __aggregation_pressed(self):
        """
        Starts the calculation-routine, if the Aggregation-button ist pressed
        Routine:
            - Check, if calculation is possible
            - Set starting point
            - Color the buttons accordingly
            - Start calculation:
                - Show progress-bar
                - Start calculation
        """
        checker = self._calculation_controller.start_calculations(CalculationPhase.AGGREGATION_PHASE)
        if checker != CalculationPhase.RUNNING:  # Check, if changing states is possible
            self.__calculation_start_interrupted()
            self.activate()
            return

        self._starting_point = CalculationPhase.AGGREGATION_PHASE
        self.__disable_buttons()
        self.__show_calculation_utilities()

    def __disable_buttons(self):
        """
        Makes a list of buttons non-clickable
        Colors the clicked button yellow, the lower buttons are colored green.
        All other buttons keep their original color
        """
        counter = 0
        starting_index = self._starting_point.get_order()

        for button in self.buttons:
            button.config(state="disable")
            if counter == starting_index:
                button.configure(bg_color="yellow")
            elif counter < starting_index:
                button.configure(bg_color="green")
            counter += 1

    def __activate_buttons(self):
        """
        Reactivates the buttons of the class and makes them clickable again
        """
        for button in self.buttons:
            button.configure(state="enable")

    def __stop_calculation(self):
        """
        Stops the already running calculation process.
        If the process isn't started yet, nothing will happen.
        If the process is started, the following sequence will be started
        Sequence:
            - Show popup, asking if user wants to stop the calculation
            - Yes: Calculation is stopped
            - No: Nothing happens, calculations continues
        """
        popup = YesNoPopUp("Do you really want to cancel the calculation process?", self.__receive_pop_up)
        #  TODO: Implement PopUp Communication => Call new function receiving the values

    def __show_calculation_utilities(self):
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
            customtkinter.CTkButton(master=self.window, text="Cancel", bg_color="red", command=self.__stop_calculation) \
            .pack(side="right", padx=40, pady=40)

        self.buttons.append(cancel_button)

        self._calculation_controller.start_calculations(self._starting_point)

    def __calculation_start_interrupted(self):
        """
        Shown if an error occurs while starting the calculation.
        Creates a popup and reloads the calculation-window
        """
        AlertPopUp("Calculation couldn't be started, please try again!") \
            .mainloop()

    def __receive_pop_up(self, pop_up_value: bool):
        """
        Func given to a popup to receive the returned value
        Args:
            pop_up_value (bool): value the popup returns
        """
        return pop_up_value
