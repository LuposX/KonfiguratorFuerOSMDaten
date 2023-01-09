import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.state


class MainWindow:
    """
    This Class provides the GUI, the User will be working on.
    It is made dynamic and can change between different Frames, to show different Information and Buttons to the User.
    Its Job is to just show the Frames of different States and create the Window the GUI will be used on.
    """

    def __init__(self, control):
        """
        This Method creates a MainWindow with a connection to the given Control.

        Args:
            control (control_interface.IControl): The Control the GUI shall be working with, to get access to Information on the Model.
        """
        pass

    def change_state(self, last_state, new_state):
        """
        This Method changes from an old given State to a new given State to show on the MainWindow.

        Args:
            last_state (state.State): The State that needs to me removed from the MainWindow
            new_state (state.State): The State that shall be shown by the MainWindow

        Returns:
            bool: true, if the state change was succsessfull, false if not.
        """
        pass

    def _make_visible(self, state):
        """
        This Method makes the given State visible on the MainWindow.

        Args:
            state (state.State): The state that shall be made visible.

        Returns:
            bool: true if the state could be made visible, false if not.
        """
        pass

    def _make_invisible(self, state):
        """
        This Method removes a given State from the MainWindo, so it cant be seen or interacted with anymore.

        Args:
            state (state.State): The state that shall not be visible anymore.

        Returns:
            bool: true, if the given state could be made invisible, false if not.
        """
        pass
