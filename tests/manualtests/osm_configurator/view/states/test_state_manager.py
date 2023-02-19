import pytest

from tests.manualtests.osm_configurator.view.controller_stub.export_controller_stub import ExportControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub import CategoryControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.project_controller_stub import ProjectControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.settings_controller_stub import SettingsControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.aggregation_controller_stub import \
    AggregationControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.cut_out_controller_stub import CutOutControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.data_visualization_controller_stub import \
    DataVisualizationControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.osm_data_controller_stub import OSMDataControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.calculation_controller_stub import \
    CalculationControllerStub

from src.osm_configurator.view.states.main_window import MainWindow
from src.osm_configurator.view.states.state_name_enum import StateName


def test_innit():
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    assert state_manager.get_state().get_state_name() == StateName.MAIN_MENU

    assert state_manager._previous_state is None

    assert state_manager._current_state.get_state_name() == StateName.MAIN_MENU

@pytest.mark.parametrize("state_name,default_right", [(StateName.DATA, StateName.CATEGORY),
                                                      (StateName.CATEGORY, StateName.REDUCTION),
                                                      (StateName.REDUCTION, StateName.ATTRACTIVITY_EDIT),
                                                      (StateName.ATTRACTIVITY_EDIT, StateName.AGGREGATION),
                                                      (StateName.ATTRACTIVITY_VIEW, StateName.AGGREGATION),
                                                      (StateName.AGGREGATION, StateName.CALCULATION)])
def test_default_go_right_no_none(state_name, default_right):
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(state_name)

    assert state_manager.get_state().get_state_name() == state_name

    state_manager.default_go_right()

    assert state_manager.get_state().get_state_name() == default_right

@pytest.mark.parametrize("state_name,default_right", [(StateName.MAIN_MENU, None),
                                                      (StateName.CREATE_PROJECT, None),
                                                      (StateName.CALCULATION, None),
                                                      (StateName.SETTINGS, None)])
def test_default_go_right_none(state_name, default_right):
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(state_name)

    assert state_manager.get_state().get_state_name() == state_name

    assert not state_manager.default_go_right()

@pytest.mark.parametrize("state_name,default_left", [(StateName.CATEGORY, StateName.DATA),
                                                      (StateName.REDUCTION, StateName.CATEGORY),
                                                      (StateName.ATTRACTIVITY_EDIT, StateName.REDUCTION),
                                                      (StateName.ATTRACTIVITY_VIEW, StateName.REDUCTION),
                                                      (StateName.AGGREGATION, StateName.ATTRACTIVITY_EDIT),
                                                     (StateName.CALCULATION, StateName.AGGREGATION)])
def test_default_go_left_not_none(state_name, default_left):
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(state_name)

    assert state_manager.get_state().get_state_name() == state_name

    state_manager.default_go_left()

    assert state_manager.get_state().get_state_name() == default_left

@pytest.mark.parametrize("state_name,default_left", [(StateName.MAIN_MENU, None),
                                                      (StateName.CREATE_PROJECT, None),
                                                      (StateName.SETTINGS, None),
                                                      (StateName.DATA, None)])
def test_default_go_left_none(state_name, default_left):
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(state_name)

    assert state_manager.get_state().get_state_name() == state_name

    assert not state_manager.default_go_left()

@pytest.mark.parametrize("state_name", [(StateName.MAIN_MENU), (StateName.CREATE_PROJECT), (StateName.DATA),
                                        (StateName.CATEGORY), (StateName.REDUCTION), (StateName.ATTRACTIVITY_EDIT),
                                        (StateName.ATTRACTIVITY_VIEW), (StateName.AGGREGATION), (StateName.CALCULATION),
                                        (StateName.SETTINGS)])
def test_change_state(state_name):
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(state_name)

    assert state_manager.get_state().get_state_name() == state_name


# Is the Same as test_change_state
def test_get_state():
    assert True


def test_lock_state():
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(StateName.CATEGORY)

    state_manager.lock_state()

    assert not state_manager.change_state(StateName.MAIN_MENU)

    assert not state_manager.default_go_left()

    assert not state_manager.default_go_right()


def test_unlock_state():
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(StateName.CATEGORY)

    state_manager.lock_state()

    state_manager.unlock_state()

    assert state_manager.change_state(StateName.MAIN_MENU)

    assert state_manager.get_state().get_state_name() == StateName.MAIN_MENU


def test_freeze_frame():
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(StateName.CATEGORY)

    state_manager.freeze_state()

    assert not state_manager.change_state(StateName.MAIN_MENU)

    assert not state_manager.default_go_left()

    assert not state_manager.default_go_right()


def test_unfreeze_frame():
    # Making a mainWindow, since stateManager need sone and the main window will create our stateManager directly
    main_window = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager = main_window._state_manager

    state_manager.change_state(StateName.CATEGORY)

    state_manager.freeze_state()

    assert state_manager.change_state(StateName.MAIN_MENU)

    assert state_manager.get_state().get_state_name() == StateName.MAIN_MENU
