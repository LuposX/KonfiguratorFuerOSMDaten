import src.osm_configurator.view.states.positioned_frame
import src.osm_configurator.view.states.state_name_enum


class State:
    """
    This class models a State.
    A State consist of
    - a list of frames, that shall be visible on a window, when this state is active
    - a default state to its right
    - a default state to its left
    All states have one state to their left and to their right, to model the basic state change.
    Those states can be 'none' in order so signify that there is no further right or left.
    """

    def __init__(self, active_frames, own_state_name, default_left, default_right):
        """
        This method creates a new state, that holds the given frames, has the given state id (the own_state_name),
        and has a default left and right.

        Args:
            active_frames list[positioned_frame.PositionedFrame]: A list of frames, that this state holds
            own_state_name (state_name_enum.StateName): The id that defines this state
            default_left (state_name_enum.StateName): The id of the state on this states left
            default_right (state_name_enum.StateName): The id of the state on this states right
        """
        pass

    def get_active_frames(self):
        """
        The list of frames this state holds and shall be shown on a window, if it is active.

        Returns:
            list[positioned_frame.PositionedFrame]: List of frames this state holds
        """
        pass

    def get_default_left(self):
        """
        The id of the state on this states left.

        Returns:
            (state_name_enum.StateName): This states left state id
        """
        pass

    def get_default_right(self):
        """
        The id of the state on this states right.

        Returns:
            (state_name_enum.StateName): This states right state id
        """
        pass

    def get_state_name(self):
        """
        The id of this state.

        Returns:
            (state_name_enum.StateName): The id of this state
        """
        pass

    def equals(self, state):
        """
        Test if two states are equal.
        Two states are defined as equal, if their id is equal.

        Args:
            state (State): The state you want to know if it is equal to this one

        Returns:
            bool: true if the given state and this state ist equal. false if not
        """
        pass
