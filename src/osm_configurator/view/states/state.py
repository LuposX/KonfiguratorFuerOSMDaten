from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.states.positioned_frame import PositionedFrame
    from src.osm_configurator.view.states.state_name_enum import StateName


class State:
    """
    This class models a state.
    A State consist of
    - a list of frames, that shall be visible on a window, when this state is active
    - a default state to its right
    - a default state to its left
    All states have one state to their left and to their right, to model the basic state change.
    Those states can be 'none' in order so signify that there is no further right or left.
    """

    def __init__(self, active_frames: list[PositionedFrame], own_state_name: StateName, default_left: StateName, default_right: StateName):
        """
        This method creates a new state, that holds the given frames, has the given state name,
        and has a default left and right.

        Args:
            active_frames (list[positioned_frame.PositionedFrame]): A list of frames, that this state holds
            own_state_name (state_name_enum.StateName): The name that defines this state
            default_left (state_name_enum.StateName): The name of the state on this states left
            default_right (state_name_enum.StateName): The name of the state on this states right
        """

        # Checking if active_frames are a list, and all of its elements are PositionedFrames
        if not isinstance(active_frames, list):
            raise TypeError("active_frames is not a list!")
        else:
            for frame in active_frames:
                if not isinstance(frame, PositionedFrame):
                    raise TypeError("The Frames of the active_frames are no PositionedFrames!")

        # Checking the other Attributes for correct type
        if not isinstance(own_state_name, StateName):
            raise TypeError("own_state_name is no StateName!")
        elif not isinstance(default_right, StateName) and default_right is not None:
            raise TypeError("default_right is no StateName, and not None! "
                            "The default_right, shall be a StateName or None!")
        elif not isinstance(default_left, StateName) and default_left is not None:
            raise TypeError("default_left is no StateName, and not None! "
                            "The default_left, shall be a StateName or None!")
        else:
            self._active_frames = active_frames
            self._own_state_name = own_state_name
            self._default_left = default_left
            self._default_right = default_right

    def get_active_frames(self) -> list[PositionedFrame]:
        """
        The list of frames this state holds and shall be shown on a window, if it is active.

        Returns:
            list[positioned_frame.PositionedFrame]: List of frames this state holds
        """
        return self._active_frames

    def get_default_left(self) -> StateName:
        """
        The name of the state on this states left.

        Returns:
            state_name_enum.StateName: This states left state name
        """
        return self._default_left

    def get_default_right(self) -> StateName:
        """
        The id of the state on this states right.

        Returns:
            state_name_enum.StateName: This states right state name
        """
        return self._default_right

    def get_state_name(self) -> StateName:
        """
        The name of this state.

        Returns:
            state_name_enum.StateName: The name of this state
        """
        return self._own_state_name

    def __eq__(self, other) -> bool:
        """
        Test if a state is equal to a given object.
        Two states are defined as equal, if their name is equal.

        Args:
            other (object): The other object you want to compare to this state

        Returns:
            bool: true if the given state and the other object are equal. false if not
        """

        if not isinstance(other, State):
            return False
        else:
            return self.get_state_name() == other.get_state_name()
