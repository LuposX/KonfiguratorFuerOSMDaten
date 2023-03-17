import pytest

import src.osm_configurator.view.states.main_window as main_window_i
import src.osm_configurator.view.states.state_manager as state_manager_i
import src.osm_configurator.view.states.state_name_enum as state_name_enum_i

import src_tests.manualtests.osm_configurator.view.controller_stub.export_controller_stub as \
    exportcontroller_stub_i
import \
    src_tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub as \
        category_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.project_controller_stub as \
    project_controller_stub_i
import \
    src_tests.manualtests.osm_configurator.view.controller_stub.settings_controller_stub as \
        settings_controller_stub_i
import \
    src_tests.manualtests.osm_configurator.view.controller_stub.aggregation_controller_stub as \
        aggregation_controller_stub_i
import \
    src_tests.manualtests.osm_configurator.view.controller_stub.calculation_controller_stub as \
        calculation_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.cut_out_controller_stub as \
    cut_out_controller_stub_i
import \
    src_tests.manualtests.osm_configurator.view.controller_stub.data_visualization_controller_stub as \
        data_visualization_controller_stub_i
import \
    src_tests.manualtests.osm_configurator.view.controller_stub.osm_data_controller_stub as \
        osm_data_controller_stub_i

export_controller = exportcontroller_stub_i.ExportControllerStub()
category_controller = category_controller_stub_i.CategoryControllerStub()
project_controller = project_controller_stub_i.ProjectControllerStub()
settings_controller = settings_controller_stub_i.SettingsControllerStub()
aggregation_controller = aggregation_controller_stub_i.AggregationControllerStub()
calculation_controller = calculation_controller_stub_i.CalculationControllerStub()
cut_out_controller = cut_out_controller_stub_i.CutOutControllerStub()
data_visualization_controller = data_visualization_controller_stub_i.DataVisualizationControllerStub()
osm_data_controller = osm_data_controller_stub_i.OSMDataControllerStub()


@pytest.fixture
def main_window():
    """Returns a legit MainWindow, which contains a legit StateManager"""
    return main_window_i.MainWindow(export_controller=export_controller, category_controller=category_controller,
                                    project_controller=project_controller, settings_controller=settings_controller,
                                    aggregation_controller=aggregation_controller,
                                    calculation_controller=calculation_controller,
                                    cut_out_controller=cut_out_controller,
                                    data_visualization_controller=data_visualization_controller,
                                    osm_data_controller=osm_data_controller)


def test_innit(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.MAIN_MENU


def test_change_state_main_menu(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.MAIN_MENU)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.MAIN_MENU


def test_change_state_create_project(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.CREATE_PROJECT)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.CREATE_PROJECT


def test_change_state_data(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.DATA)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.DATA


def test_change_state_category(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.CATEGORY)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.CATEGORY


def test_change_state_reduction(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.REDUCTION)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.REDUCTION


def test_change_state_attractivity_edit(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.ATTRACTIVITY_EDIT)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.ATTRACTIVITY_EDIT


def test_change_state_attractivity_view(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.ATTRACTIVITY_VIEW)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.ATTRACTIVITY_VIEW


def test_change_state_aggregation(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.AGGREGATION)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.AGGREGATION


def test_change_state_calculation(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.CALCULATION)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.CALCULATION


def test_change_state_settings_project(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.SETTINGS_PROJECT)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.SETTINGS_PROJECT


def test_change_state_settings_no_project(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.SETTINGS_NO_PROJECT)

    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.SETTINGS_NO_PROJECT


def test_default_go_left_and_right_none(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.MAIN_MENU)

    # The MainMenu hast no default left or right

    assert not state_manager.default_go_left()

    assert not state_manager.default_go_right()


def test_default_go_left_and_rigth(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.CATEGORY)

    left: state_name_enum_i.StateName = state_manager.get_state().get_default_left()

    right: state_name_enum_i.StateName = state_manager.get_state().get_default_right()

    state_manager.default_go_left()

    assert state_manager.get_state().get_state_name() == left

    state_manager.change_state(state_name_enum_i.StateName.CATEGORY)

    state_manager.default_go_right()

    assert state_manager.get_state().get_state_name() == right


def test_get_state(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.change_state(state_name_enum_i.StateName.MAIN_MENU)

    # actually this gets tested with all other test always, but well her it is again or something
    assert state_manager.get_state().get_state_name() == state_name_enum_i.StateName.MAIN_MENU


def test_lock_state(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    state_manager.lock_state()

    assert not state_manager.change_state(state_name_enum_i.StateName.MAIN_MENU)

    state_manager.unlock_state()

    assert state_manager.change_state(state_name_enum_i.StateName.MAIN_MENU)


def test_freeze_state(main_window):
    state_manager: state_manager_i.StateManager = main_window._state_manager

    # Those methods are voids, so just testing for crashes
    state_manager.freeze_state()

    state_manager.unfreeze_state()
