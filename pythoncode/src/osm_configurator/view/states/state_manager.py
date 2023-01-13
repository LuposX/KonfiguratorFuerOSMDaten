import src.osm_configurator.view.states.state_name_enum
import src.osm_configurator.view.states.state
import src.osm_configurator.view.states.positioned_frame
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.main_window


class StateManager:
    """
    This class manages the different states, that can be shown on a window.
    It knows what state is currently active and provides methods to change the state.
    """

    def __init__(self, control, main_window):
        """
        This method creates a StateManager, that will control what state is currently active and manages
        the changes between states.
        It will create all states, as well all the frames that exist and put them in the state they belong.

        Args:
            control (control_interface.IControl): The connection to the control so the frames of each state can access the model.
            main_window (main_window.MainWindow): The MainWindow where the frames of the state shall be shown on.
        """
        pass

    def default_go_right(self):
        """
        This method changes to the State that is the default_right state of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        pass

    def default_go_left(self):
        """
        This method changes to the state that is the default_left State of the current one.

        Returns:
            bool: True, if a state change was successfully made, false if there was no state change or something
            went wrong.
        """
        pass

    def change_state(self, new_state):
        """
        This method changes to the given state and deactivate the old one.

        Args:
            new_state (state_name_enum.StateName): The id of the new state that shall be activated.

        Returns:
            bool: True if state change was successful, false if not.
        """
        pass

    def get_state(self):
        """
        This method returns the currently active state.

        Returns:
            state.State: The currently active state.
        """
        pass

    def close_program(self):
        """
        This method closes the program and shuts the whole application down.
        """
        pass
