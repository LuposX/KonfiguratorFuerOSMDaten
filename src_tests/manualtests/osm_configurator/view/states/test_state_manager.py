import pytest

from src_tests.manualtests.osm_configurator.view.controller_stub.export_controller_stub import ExportControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub import CategoryControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.project_controller_stub import ProjectControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.settings_controller_stub import SettingsControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.aggregation_controller_stub import \
    AggregationControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.cut_out_controller_stub import CutOutControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.data_visualization_controller_stub import \
    DataVisualizationControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.osm_data_controller_stub import OSMDataControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.calculation_controller_stub import \
    CalculationControllerStub

from src.osm_configurator.view.states.main_window import MainWindow
from src.osm_configurator.view.states.state_name_enum import StateName

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager


def test_innit():
    # Making a mainWindow, since stateManager needs one and the main window will create our stateManager directly
    main_window: MainWindow = MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                             SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                             CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())
    state_manager: StateManager = main_window._state_manager

    assert state_manager.get_state().get_state_name() == StateName.MAIN_MENU

    # Previous as well as current state are the MainMenu state
    assert state_manager._previous_state.get_state_name() == StateName.MAIN_MENU

    assert state_manager._current_state.get_state_name() == StateName.MAIN_MENU

@pytest.fixture
def main_window():
    """Returns a legit MainWindow, which contains a legit StateManager"""
    return MainWindow(ExportControllerStub(), CategoryControllerStub(), ProjectControllerStub(),
                      SettingsControllerStub(), AggregationControllerStub(), CalculationControllerStub(),
                      CutOutControllerStub(), DataVisualizationControllerStub(), OSMDataControllerStub())

# Testing StateChange itself

def test_state_change_to_main_menu(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.MAIN_MENU)

    assert state_manager.get_state().get_state_name() == StateName.MAIN_MENU

def test_state_change_to_create_project(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.CREATE_PROJECT)

    assert state_manager.get_state().get_state_name() == StateName.CREATE_PROJECT

def test_state_change_to_data(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.DATA)

    assert state_manager.get_state().get_state_name() == StateName.DATA

def test_state_change_to_category(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.CATEGORY)

    assert state_manager.get_state().get_state_name() == StateName.CATEGORY

def test_state_change_to_reduction(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.REDUCTION)

    assert state_manager.get_state().get_state_name() == StateName.REDUCTION

def test_state_change_to_attractivity_edit(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.ATTRACTIVITY_EDIT)

    assert state_manager.get_state().get_state_name() == StateName.ATTRACTIVITY_EDIT

def test_state_change_to_attractivity_view(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.ATTRACTIVITY_VIEW)

    assert state_manager.get_state().get_state_name() == StateName.ATTRACTIVITY_VIEW

def test_state_change_to_aggregation(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.AGGREGATION)

    assert state_manager.get_state().get_state_name() == StateName.AGGREGATION

def test_state_change_to_calculation(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.CALCULATION)

    assert state_manager.get_state().get_state_name() == StateName.CALCULATION

def test_state_change_to_settings(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.SETTINGS)

    assert state_manager.get_state().get_state_name() == StateName.SETTINGS

# Testing default go left

def test_data_to_none(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.DATA)

    assert state_manager.get_state().get_state_name() == StateName.DATA

    assert not state_manager.default_go_left()

def test_category_to_data(main_window):
    state_manager: StateManager = main_window._state_manager

    state_manager.change_state(StateName.CATEGORY)

    assert state_manager.get_state().get_state_name() == StateName.CATEGORY

    assert state_manager.default_go_left()

    assert state_manager._previous_state.get_state_name() == StateName.CATEGORY

    assert state_manager._current_state.get_state_name() == StateName.DATA
    assert state_manager.get_state().get_state_name() == StateName.DATA