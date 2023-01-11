import src.osm_configurator.view.toplevelframes.top_level_frame
import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface


class PositionedFrame:
    """
    This Class gives a Frame a position, via Coordinates, to tell in what position the Frame wants to be in, when
    it is shown on a Window.
    """

    def __init__(self, frame, colum, line, state_manager, control):
        """
        This method creates a PositionedFrame, which is a Frame and coordinates to its Position.

        Args:
            frame (top_level_frame.TopLevelFrame): The frame you want to give a position
            colum (int): The Colum the Frame shall be placed in
            line (int): The Line the Frame shall be placed in
            state_manager (state_manager.StateManager): The StateManager the frame will use to change states if needed
            control (control_interface.IControl): The control that a frame shall call, if it needs access to the model
        """
        pass

    def get_frame(self):
        """
        This method returns the frame this PositionedFrame holds.

        Returns:
            (top_level_frame.TopLevelFrame): The Frame this PositionedFrame holds
        """
        pass

    def get_column(self):
        """
        This method Returns the column the frame is placed in.

        Returns:
            (int): The Column the Frame is placed in.
        """
        pass

    def get_line(self):
        """
        This method returns the line the frame is placed in.

        Returns:
            (int): The Line the frame is placed in
        """
        pass
