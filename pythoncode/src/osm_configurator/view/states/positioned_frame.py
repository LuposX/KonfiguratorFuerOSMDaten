import pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame
import pythoncode.src.osm_configurator.view.states.state_manager


class PositionedFrame:
    """
    This Class gives a Frame a position via Coordinates, to tell in what position the Frame wants to be in, when
    it is shown on a Window.
    """

    def __init__(self, frame, colum, line, state_manager):
        """
        This Method Creates a Positioned Frame, which is a Frame and Coordinates to its Position.

        Args:
            frame (top_level_frame.TopLevelFrame): Frame that gets the position
            colum (int): The Colum the Frame shall be placed in
            line (int): The Line the Frame shall be placed in
            state_manager (state_manager.StateManager): The StateManager the Frame uses to change States if needed
        """
        pass

    def get_frame(self):
        """
        This Method Returns the Frame the PositionedFrame holds.

        Returns:
            (top_level_frame.TopLevelFrame): The Frame the PositionedFrame holds
        """
        pass

    def get_colum(self):
        """
        This Method returns the Colum the Frame is placed in.

        Returns:
            (int): The Colum the Frame is placed in.
        """
        pass

    def get_line(self):
        """
        This Method returns the Line the Frame is placed in.

        Returns:
            (int): The Line the Frame is placed in
        """
        pass
