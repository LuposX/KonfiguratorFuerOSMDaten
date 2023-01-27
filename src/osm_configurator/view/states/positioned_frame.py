from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class PositionedFrame:
    """
    This Class gives a Frame a position, via Coordinates, to tell in what position the Frame wants to be in, when
    it is shown on a Window.
    """

    def __init__(self, frame: TopLevelFrame, colum: int, line: int):
        """
        This method creates a PositionedFrame, which is a Frame and coordinates to its Position.

        Args:
            frame (top_level_frame.TopLevelFrame): The frame you want to give a position
            colum (int): The Colum the Frame shall be placed in, can't be negative
            line (int): The Line the Frame shall be placed in, can't be negative
        """
        self.__smallest_colum_and_line_value = 0

        if not isinstance(frame, TopLevelFrame):
            raise TypeError("The given Frame is not a Frame!")
        elif not isinstance(colum, int):
            raise TypeError("The given colum is not an Integer!")
        elif not isinstance(line, int):
            raise TypeError("The given line is not an Integer!")
        elif colum < self.__smallest_colum_and_line_value or line < self.__smallest_colum_and_line_value:
            raise ValueError("The Value of colum or line is negative!")
        else:
            self.__frame = frame
            self.__colum = colum
            self.__line = line

    def get_frame(self) -> TopLevelFrame:
        """
        This method returns the frame this PositionedFrame holds.

        Returns:
            top_level_frame.TopLevelFrame: The Frame this PositionedFrame holds
        """
        return self.__frame

    def get_column(self) -> int:
        """
        This method Returns the column the frame is placed in.

        Returns:
            int: The Column the Frame is placed in.
        """
        return self.__colum

    def get_line(self) -> int:
        """
        This method returns the line the frame is placed in.

        Returns:
            int: The Line the frame is placed in
        """
        return self.__line
