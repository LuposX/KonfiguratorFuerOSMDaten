import pytest

import src.osm_configurator.view.states.main_window as main_window_i

import src_tests.manualtests.osm_configurator.view.controller_stub.export_controller_stub as exportcontroller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub as category_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.project_controller_stub as project_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.settings_controller_stub as settings_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.aggregation_controller_stub as aggregation_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.calculation_controller_stub as calculation_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.cut_out_controller_stub as cut_out_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.data_visualization_controller_stub as data_visualization_controller_stub_i
import src_tests.manualtests.osm_configurator.view.controller_stub.osm_data_controller_stub as osm_data_controller_stub_i

export_controller = exportcontroller_stub_i.ExportControllerStub()
category_controller = category_controller_stub_i.CategoryControllerStub()
project_controller = project_controller_stub_i.ProjectControllerStub()
settings_controller = settings_controller_stub_i.SettingsControllerStub()
aggregation_controller = aggregation_controller_stub_i.AggregationControllerStub()
calculation_controller = calculation_controller_stub_i.CalculationControllerStub()
cut_out_controller = cut_out_controller_stub_i.CutOutControllerStub()
data_visualization_controller = data_visualization_controller_stub_i.DataVisualizationControllerStub()
osm_data_controller = osm_data_controller_stub_i.OSMDataControllerStub()


def test_innit():
    main_window = main_window_i.MainWindow(export_controller=export_controller, category_controller=category_controller,
                                           project_controller=project_controller, settings_controller=settings_controller,
                                           aggregation_controller=aggregation_controller, calculation_controller=calculation_controller,
                                           cut_out_controller=cut_out_controller, data_visualization_controller=data_visualization_controller,
                                           osm_data_controller=osm_data_controller)
    # if didn't crash, shit is fine
    assert True
