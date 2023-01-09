from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
from src.osm_configurator.view.states.state_manager import StateManager


class PositionedFrame:
    """
    This Class gives a Frame a position, via Coordinates, to tell in what position the Frame wants to be in, when
    it is shown on a Window.
    """

    def __init__(self, frame, colum, line, state_manager):
        """
        This Method Creates a Positioned Frame, which is a Frame and Coordinates to its Position.

        Args:
            frame (TopLevelFrame): The Frame you want to give a Position
            colum (int): The Colum the Frame shall be placed in
            line (int): The Line the Frame shall be placed in
            state_manager (StateManager): The StateManager the Frame will use to change States if needed
        """
        pass

    def get_frame(self):
        """
        This Method Returns the Frame this PositionedFrame holds.

        Returns:
            (TopLevelFrame): The Frame this PositionedFrame holds
        """
        pass

    def get_colum(self):
        """
        This Method Returns the Colum the Frame is placed in.

        Returns:
            (int): The Colum the Frame is placed in.
        """
        pass

    def get_line(self):
        """
        This Method Returns the Line the Frame is placed in.

        Returns:
            (int): The Line the Frame is placed in
        """
        pass
