import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.state_name_enum


class MainWindow:
    """
    This class provides the GUI, the user will be working on.
    It is made dynamic and can change between different frames, to show different information and buttons to the user.
    Its job is to just show the frames of different states and create the window the GUI will be used on.
    """

    def __init__(self, control):
        """
        This method creates a MainWindow with a connection to the given control.

        Args:
            control (control_interface.IControl): The control the GUI shall be working with, to get access to information on the model.
        """
        pass

    def change_state(self, last_state, new_state):
        """
        This method changes from an old given state to a new given state to show on the MainWindow.

        Args:
            last_state (state.State): The state that needs to me removed from the MainWindow
            new_state (state.State): The state that shall be shown by the MainWindow

        Returns:
            bool: true, if the state change was successful, false if not.
        """
        pass

    def _make_visible(self, state):
        """
        This method makes the given State visible on the MainWindow.

        Args:
            state (state.State): The state that shall be made visible.

        Returns:
            bool: true if the state could be made visible, false if not.
        """
        pass

    def _make_invisible(self, state):
        """
        This method removes a given State from the MainWindo, so it cant be seen or interacted with anymore.

        Args:
            state (state.State): The state that shall not be visible anymore.

        Returns:
            bool: true, if the given state could be made invisible, false if not.
        """
        pass
