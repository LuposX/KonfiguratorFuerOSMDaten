import pytest

import src_tests.unittests.osm_configurator.view.states.top_level_frame_stub as top_level_frame_stub_i
import src.osm_configurator.view.states.positioned_frame as positioned_frame_i


@pytest.mark.parametrize("top_level_frame,colum,row,colum_span,row_span,sticky",
                         [(top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE - 1,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE - 1,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE - 1,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE - 1,
                           "NSEW")
                          ])
def test_value_error(top_level_frame, colum, row, colum_span, row_span, sticky):
    with pytest.raises(ValueError):
        positioned_frame: positioned_frame_i.PositionedFrame = positioned_frame_i.PositionedFrame(
            frame=top_level_frame, colum=colum, row=row, colum_span=colum_span, row_span=row_span, sticky=sticky)


@pytest.mark.parametrize("top_level_frame,colum,row,colum_span,row_span,sticky",
                         [(top_level_frame_stub_i.TopLevelFrameStub(None),
                           "Something",
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           "Something",
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           "Something",
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "Something",
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           69)
                          ])
def test_type_error(top_level_frame, colum, row, colum_span, row_span, sticky):
    with pytest.raises(TypeError):
        positioned_frame: positioned_frame_i.PositionedFrame = positioned_frame_i.PositionedFrame(
            frame=top_level_frame, colum=colum, row=row, colum_span=colum_span, row_span=row_span, sticky=sticky)


@pytest.mark.parametrize("top_level_frame,colum,row,colum_span,row_span,sticky",
                         [(top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE,
                           "NSEW"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           420,
                           69,
                           42,
                           3,
                           "W"),
                          (top_level_frame_stub_i.TopLevelFrameStub(None),
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE + 1,
                           positioned_frame_i.SMALLEST_COLUM_AND_ROW_VALUE + 1,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE + 1,
                           positioned_frame_i.SMALLEST_COLUM_SPAN_AND_ROW_SPAN_VALUE + 1,
                           "NSEW")
                          ])
def test_getter(top_level_frame, colum, row, colum_span, row_span, sticky):
    positioned_frame: positioned_frame_i.PositionedFrame = positioned_frame_i.PositionedFrame(
        frame=top_level_frame, colum=colum, row=row, colum_span=colum_span, row_span=row_span, sticky=sticky)

    assert positioned_frame.get_frame() == top_level_frame
    assert positioned_frame.get_column() == colum
    assert positioned_frame.get_row() == row
    assert positioned_frame.get_colum_span() == colum_span
    assert positioned_frame.get_row_span() == row_span
    assert positioned_frame.get_sticky() == sticky
