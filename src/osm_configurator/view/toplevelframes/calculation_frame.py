from __future__ import annotations

import tkinter

import customtkinter
from typing import TYPE_CHECKING

from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.popups.yes_no_pop_up import YesNoPopUp
from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.calculation_controller_interface import ICalculationController
from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.progress_bar_constants as progress_bar_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.calculation_controller_interface import ICalculationController
    from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CalculationFrame(TopLevelFrame):
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
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
                         )

        self._starting_point = CalculationPhase.NONE
        self._state_manager = state_manager
        self._calculation_controller = calculation_controller
        self._data_visualization_controller = data_visualization_controller

        self._frozen: bool = False  # indicates whether the window is frozen or not

        # Configuring the rows and columns

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)

        #  Creating the entries on the left

        self.buttons = [
            customtkinter.CTkButton(master=self,
                                    text="Data Input and Geofilter",
                                    command=self.__data_and_geofilter_pressed),
            customtkinter.CTkButton(master=self,
                                    text="Tag-Filter",
                                    command=self.__tag_filter_pressed),
            customtkinter.CTkButton(master=self,
                                    text="Reduction",
                                    command=self.__reduction_pressed),
            customtkinter.CTkButton(master=self,
                                    text="Attractivity",
                                    command=self.__attractivity_pressed),
            customtkinter.CTkButton(master=self,
                                    text="Aggregation",
                                    command=self.__aggregation_pressed)
        ]

        self.choose_starting_point_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(master=self,
                                   text="Choose Starting-Point",
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value,
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   )
        self.choose_starting_point_label.grid(row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10)

        # Aligning and configuring the buttons with standard-attributes
        for i, button in enumerate(self.buttons):
            button.configure(
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value)
            button.grid(row=i + 1, column=0, rowspan=1, columnspan=1, padx=10, pady=30)

    def activate(self):
        pass

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
        if checker != CalculationState.RUNNING:
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
        if checker != CalculationState.RUNNING:  # Check, if changing states is possible
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
        if checker != CalculationState.RUNNING:  # Check, if changing states is possible
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
        if checker != CalculationState.RUNNING:  # Check, if changing states is possible
            # Interrupt calculation start
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
        if checker != CalculationState.RUNNING:  # Check, if changing states is possible
            # Interrupt calculation start
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
        starting_index = self._starting_point.get_order() - 1

        for i, button in enumerate(self.buttons):
            button.configure(state="disabled",
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_DISABLED.value,
                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value,
                             )

            if i == starting_index:
                button.configure(fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_YELLOW.value)
            elif i < starting_index:
                button.configure(fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_GREEN.value)

    def __activate_buttons(self):
        """
        Reactivates the buttons of the class and makes them clickable again
        """
        for button in self.buttons:
            button.configure(state=tkinter.NORMAL,
                             fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                             text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                             )

    def __stop_calculation_init(self):
        """
        Initializes the cancel process to make the process communicate with the yes-no-popup
        """
        self._state_manager.freeze_state()
        YesNoPopUp(func=self.__stop_calculation, message="Do You really want to cancel the Calculation?")

    def __stop_calculation(self, cancel: bool):
        """
        Stops the already running calculation process.
        If the process isn't started yet, nothing will happen.
        If the process is started, the following sequence will be started
        Sequence:
            - Show popup, asking if user wants to stop the calculation
            - Yes: Calculation is stopped
            - No: Nothing happens, calculations continues
        Args:
            cancel (bool): True, if the calculation will be canceled, false else (value from the popup)
        """
        self._state_manager.unfreeze_state()
        if cancel:
            self._state_manager.unlock_state()
            self._calculation_controller.cancel_calculations()
            self.__activate_buttons()
            AlertPopUp(message="Calculation has stopped successfully")

            # Destroying the progressbar and the cancel button
            self.progressbar.destroy()
            self.cancel_button.destroy()
        else:
            AlertPopUp(message="Calculation will continue")

    def __show_calculation_utilities(self):
        """
        Starts the calculation:
            Adds the progressbar and the button to stop the calculation to the window
            Calls the according controller
        """
        self._state_manager.lock_state()
        self.progressbar = \
            customtkinter.CTkProgressBar(master=self,
                                         progress_color=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_PROGRESS_COLOR.value,
                                         width=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_WIDTH.value,
                                         orientation=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_ORIENTATION.value,
                                         mode=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_MODE.value,
                                         indeterminate_speed=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_INDETERMINATE_SPEED.value,
                                         border_width=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_BORDER_WITH.value,
                                         corner_radius=progress_bar_constants_i.ProgressBarConstants.PROGRESS_BAR_CONSTANTS_CORNER_RADIUS.value)
        self.progressbar.grid(column=1, row=2, rowspan=1, columnspan=1, padx=10, pady=10)

        self.cancel_button = \
            customtkinter.CTkButton(master=self,
                                    text="Cancel",
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_RED.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                    command=self.__stop_calculation_init)
        self.cancel_button.grid(column=1, row=3, rowspan=1, columnspan=1, padx=10, pady=10)

        self.progressbar_label = \
            customtkinter.CTkLabel(master=self,
                                   text="Calculation started")
        self.progressbar_label.grid(column=2, row=1, rowspan=1, columnspace=1, padx=30, pady=10)

        self.buttons.append(self.cancel_button)  # Add cancel button to buttons-list

        self._calculation_controller.start_calculations(
            self._starting_point)  # starts the calculation from the chosen starting point

        self.after(30000, self.__update_progressbar)  # keeps the progressbar up-to-date

    def __update_progressbar(self) -> None:
        """
        Keeps the progressbar up-to-date. calls itself every five seconds if the calculation is not finished
        """
        calculation_state = self._calculation_controller.get_calculation_state()
        calculation_phase = self._calculation_controller.get_current_calculation_phase()
        calculation_process = self._calculation_controller.get_current_calculation_process()

        if calculation_state == CalculationState.RUNNING and calculation_process < 1:
            # Calculation is running and no phase change expected
            self.progressbar.configure(value=calculation_process)
            self.after(30000, self.__update_progressbar)
            return

        if (calculation_state == CalculationState.RUNNING or calculation_state == CalculationState.ENDED_SUCCESSFULLY) \
                and calculation_process == 1:
            #  Phase change expected
            if calculation_phase == CalculationPhase.AGGREGATION_PHASE:
                # Calculation is done
                self.__end_calculation()
                return
            else:
                # State will be switched
                calculation_phase = self.__get_next_phase(calculation_phase)

                self.progressbar.configure(value=0)  # Reset progressbar
                self.progressbar_label.configure(text=calculation_phase.get_name())  # change label to the next phase

                self.after(30000, self.__update_progressbar)
                return

    def __end_calculation(self):
        """
        Function called if calculation finished successfully.
        Configures the shown widgets alerting that the calculation finished successfully
        """
        self.progressbar_label.configure(text="Calculation finished successfully")
        visualize_button = \
            customtkinter.CTkButton(master=self,
                                    text="Visualize Results",
                                    command=self.__visualize_results,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
                                    )
        visualize_button.grid(column=3, row=1, rowspan=1, columnspan=1, padx=10, pady=10)
        self.buttons.append(visualize_button)

    def __get_next_phase(self, current_phase: CalculationPhase) -> CalculationPhase:
        """
        Iterates the CalculationPhase-Enum and returns the next element to the given
        Args:
            current_phase (CalculationPhase): value of the given calculation-phase
        Returns:
            CalculationPhase: Value of the next calculation-phase
        """
        take_next = False
        for element in CalculationPhase:
            if take_next:
                return element
            if element == current_phase:
                take_next = True
        return CalculationPhase.NONE

    def __calculation_start_interrupted(self):
        """
        Shown if an error occurs while starting the calculation.
        Creates a popup and reloads the calculation-window
        """
        AlertPopUp("Calculation couldn't be started, please try again!")

    def __visualize_results(self):
        """
        Gets called if the "Visualize Results" Button is pressed. Calls the according function from the controller to
        initialise the visualization process
        """
        self._data_visualization_controller.get_calculation_visualization()
        # TODO: finish implementation

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        for button in self.buttons:
            button.configure(state=tkinter.DISABLED)

        self._frozen = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        for button in self.buttons:
            button.configure(state=tkinter.NORMAL)

        self._frozen = False
