from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from typing import Final

SMALLEST_COLUM_AND_ROW_VALUE: Final = 0
SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE: Final = 0


class PositionedFrame:
    """
    This Class gives a Frame a position, via Coordinates, to tell in what position the Frame wants to be in, when
    it is shown on a Window.
    """

    def __init__(self, frame: TopLevelFrame, colum: int, row: int, colum_span: int, row_span: int, sticky: str):
        """
        This method creates a PositionedFrame, which is a Frame and coordinates to its Position.

        Args:
            frame (top_level_frame.TopLevelFrame): The frame you want to give a position
            colum (int): The Colum the Frame shall be placed in, can't be negative
            row (int): The Line the Frame shall be placed in, can't be negative
            colum_span (int): The colum span the frame shall have
            row_span (int): The row span the frame shall have
            sticky (str): The stick Type of how the frame is placed in a grid
        """

        # Testing for correct Types, except for the frame, because Python is a little bitch
        if not isinstance(colum, int):
            raise TypeError("The given colum is not an Integer!")
        elif not isinstance(row, int):
            raise TypeError("The given row is not an Integer!")
        elif not isinstance(colum_span, int):
            raise TypeError("The given colum span is not an Integer!")
        elif not isinstance(row_span, int):
            raise TypeError("The given row span is not an Integer!")
        elif not isinstance(sticky, str):
            raise TypeError("The attribute sticky is not a String!")
        elif colum_span < SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE or row_span < SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE:
            raise ValueError("The Value of colum span and row span can't negative!")
        elif colum < SMALLEST_COLUM_AND_ROW_VALUE or row < SMALLEST_COLUM_AND_ROW_VALUE:
            raise ValueError("The Value of colum or row can't negative!")
        else:
            self._frame = frame
            self._colum = colum
            self._row = row
            self._colum_span = colum_span
            self._row_span = row_span
            self._sticky = sticky

    def get_frame(self) -> TopLevelFrame:
        """
        This method returns the frame this PositionedFrame holds.

        Returns:
            top_level_frame.TopLevelFrame: The Frame this PositionedFrame holds
        """
        return self._frame

    def get_column(self) -> int:
        """
        This method Returns the column the frame is placed in.

        Returns:
            int: The Column the Frame is placed in.
        """
        return self._colum

    def get_row(self) -> int:
        """
        This method returns the line the frame is placed in.

        Returns:
            int: The Line the frame is placed in
        """
        return self._row

    def get_row_span(self) -> int:
        """
        This method returns the row span of the frame.

        Returns:
            int: The row span of the frame
        """
        return self._row_span

    def get_colum_span(self) -> int:
        """
        This method returns the colum span of the frame.

        Returns:
            int: The colum span of the frame
        """
        return self._colum_span

    def get_sticky(self) -> str:
        """
        This method returns the sticky Type of how the frame is placed in a grid.

        Returns:
            str: The sticky Type of the frame
        """
        return self._sticky
