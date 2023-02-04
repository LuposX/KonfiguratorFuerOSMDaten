import pytest

import src.osm_configurator.view.states.positioned_frame as positioned_frame_i
import src.osm_configurator.view.toplevelframes.top_level_frame as top_level_frame_i
import src.osm_configurator.view.states.state_manager as state_manager_i


def test_type_errors():
    with pytest.raises(TypeError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), "0", 0, 0, 0,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(TypeError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0, "0", 0, 0,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(TypeError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0, 0, "0", 0,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(TypeError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0, 0, 0, "0",
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(TypeError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 0,
                                           69)


def test_value_errors():
    with pytest.raises(ValueError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None),
                                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE - 1, 0, 0, 0,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(ValueError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0,
                                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE - 1, 0, 0,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(ValueError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0,
                                           0, positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE - 1, 0,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)

    with pytest.raises(ValueError):
        positioned_frame_i.PositionedFrame(top_level_frame_i.TopLevelFrame(None), 0,
                                           0, 0, positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE - 1,
                                           state_manager_i.FRAME_STICKY_WHOLE_CELL)


@pytest.mark.parametrize("frame,column,row,column_span,row_span,sticky",
                         [(top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 0, state_manager_i.FRAME_STICKY_WHOLE_CELL),
                          (top_level_frame_i.TopLevelFrame(None), 1, 0, 0, 0, state_manager_i.FRAME_STICKY_WHOLE_CELL),
                          (top_level_frame_i.TopLevelFrame(None), 0, 1, 0, 0, state_manager_i.FRAME_STICKY_WHOLE_CELL),
                          (top_level_frame_i.TopLevelFrame(None), 0, 0, 1, 0, state_manager_i.FRAME_STICKY_WHOLE_CELL),
                          (top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 1, state_manager_i.FRAME_STICKY_WHOLE_CELL),
                          (top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 0, state_manager_i.FRAME_STICKY_TOP_LEFT),
                          (top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 0, state_manager_i.FRAME_STICKY_TOP_RIGHT),
                          (top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 0, state_manager_i.FRAME_STICKY_BOTTOM_LEFT),
                          (
                          top_level_frame_i.TopLevelFrame(None), 0, 0, 0, 0, state_manager_i.FRAME_STICKY_BOTTOM_RIGHT),
                          (top_level_frame_i.TopLevelFrame(None), 69, 42, 420, 69420,
                           state_manager_i.FRAME_STICKY_WHOLE_CELL),
                          (top_level_frame_i.TopLevelFrame(None), 1, 2, 3, 4, state_manager_i.FRAME_STICKY_TOP_LEFT),
                          (top_level_frame_i.TopLevelFrame(None), 9, 8, 7, 6, state_manager_i.FRAME_STICKY_WHOLE_CELL)])
def test_attributes(frame, column, row, column_span, row_span, sticky):
    positioned_frame = positioned_frame_i.PositionedFrame(frame, column, row, column_span, row_span, sticky)

    assert positioned_frame.get_frame().__eq__(frame)
    assert positioned_frame.get_column() == column
    assert positioned_frame.get_row() == row
    assert positioned_frame.get_colum_span() == column_span
    assert positioned_frame.get_row_span() == row_span
    assert positioned_frame.get_sticky().__eq__(sticky)
