import pytest

import src.osm_configurator.view.states.state as state_i
import src.osm_configurator.view.states.positioned_frame as positioned_frame_i
import src.osm_configurator.view.states.state_manager as state_manager_i
import src.osm_configurator.view.states.state_name_enum as state_name_enum_i

import src_tests.unittests.osm_configurator.view.states.top_level_frame_stub as top_level_frame_stub_i


# There to get a Positioned Frame, to minimize code duplication
@pytest.fixture
def positioned_frame():
    """Returns a legit positioned_frame"""
    return positioned_frame_i.PositionedFrame(top_level_frame_stub_i.TopLevelFrameStub(None), 0, 0, 0, 0,
                                              state_manager_i.FRAME_STICKY_WHOLE_CELL)


# Testing if te innit works properly, basicly if it doesn't crash it is fine
def test_correct_innit(positioned_frame):
    state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION, state_name_enum_i.StateName.REDUCTION,
                  state_name_enum_i.StateName.CALCULATION)

    state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION, None, None)
    # If it doesn't crash, then the innit is fine
    # No assert, since there is no logic value to test for, we just look if the innit works


# Testing if only correct types are accepted by the innit
def test_type_errors(positioned_frame):
    with pytest.raises(TypeError):
        state_i.State(positioned_frame, state_name_enum_i.StateName.AGGREGATION, state_name_enum_i.StateName.REDUCTION,
                      state_name_enum_i.StateName.CALCULATION)

    with pytest.raises(TypeError):
        state_i.State([positioned_frame], None, state_name_enum_i.StateName.REDUCTION,
                      state_name_enum_i.StateName.CALCULATION)

    with pytest.raises(TypeError):
        state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION, "haha funny",
                      state_name_enum_i.StateName.CALCULATION)

    with pytest.raises(TypeError):
        state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION,
                      state_name_enum_i.StateName.REDUCTION,
                      "haha funny")


# Testing if attributes get set properly
@pytest.mark.parametrize("own_state_name,default_left,default_right",
                         [(state_name_enum_i.StateName.AGGREGATION,
                           state_name_enum_i.StateName.REDUCTION, state_name_enum_i.StateName.CALCULATION),
                          (state_name_enum_i.StateName.AGGREGATION,
                           state_name_enum_i.StateName.REDUCTION, state_name_enum_i.StateName.CALCULATION),
                          (state_name_enum_i.StateName.AGGREGATION,
                           None, None),
                          (state_name_enum_i.StateName.CATEGORY,
                           state_name_enum_i.StateName.DATA, state_name_enum_i.StateName.REDUCTION)])
def test_attributes(positioned_frame, own_state_name, default_left, default_right):
    state: state_i.State = state_i.State([positioned_frame], own_state_name, default_left, default_right)

    assert state.get_active_frames() == [positioned_frame]
    assert state.get_state_name() == own_state_name
    assert state.get_default_left() == default_left
    assert state.get_default_right() == default_right

    state2: state_i.State = state_i.State([positioned_frame, positioned_frame], own_state_name, default_left,
                                          default_right)

    assert state2.get_active_frames() == [positioned_frame, positioned_frame]
    assert state2.get_state_name() == own_state_name
    assert state2.get_default_left() == default_left
    assert state2.get_default_right() == default_right


# Testing if the __eq__ method works as intended
def test_equals(positioned_frame):
    # Making two truly equal states
    state1: state_i.State = state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION, None, None)
    state2: state_i.State = state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION, None, None)

    assert state1.__eq__(state2)

    # Testing if only own_state Name is enough for equal
    state3: state_i.State = state_i.State([positioned_frame], state_name_enum_i.StateName.AGGREGATION,
                           state_name_enum_i.StateName.CALCULATION, state_name_enum_i.StateName.SETTINGS_PROJECT)

    assert state1.__eq__(state3)

    # Testing for inequality
    state4: state_i.State = state_i.State([positioned_frame], state_name_enum_i.StateName.CALCULATION, None, None)

    assert not state1.__eq__(state4)
