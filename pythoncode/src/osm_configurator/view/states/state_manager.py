import src.osm_configurator.view.states.state_enum
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.main_window


class StateManager:
    """
    This Class manages the different States, that can be shown on a Window.
    It knows what State is currently active and provides Methods to change the State.
    """

    def __init__(self, control, main_window):
        """
        This Method creates a StateManager, that will control what State is currently active and manages
        the changes between States.

        Args:
            control (control_interface.IControl): The connection to the control, so the Frames of each
            state can access the Model.
            main_window (main_window.MainWindow): The MainWindow, where the Frames of the State shall be shown on.
        """
        pass

    def default_go_right(self):
        """
        This Method changes to the State that is the default_right State of the current one.

        Returns:
            bool: true, if a Statechange was successfully made, false if there was no state change or something
            went wrong
        """
        pass

    def default_go_left(self):
        """
        This Method changes to the State that is the default_left State of the current one.

        Returns:
            bool: true, if a Statechange was successfully made, false if there was no state change or something
            went wrong
        """
        pass

    def change_state(self, new_state):
        """
        This Method changes to the given State and deactivate the old one.

        Args:
            new_state (state.State): The State that shall be activated.

        Returns:
            bool: true if state change was succsessfull, false if not.
        """
        pass

    def get_state(self):
        """
        This Method returns the currently active State.

        Returns:
            state.State: the currently active State.
        """
        pass

    def close_program(self):
        """
        This Method closes the Program and shuts the whole Application down.
        """
        pass
