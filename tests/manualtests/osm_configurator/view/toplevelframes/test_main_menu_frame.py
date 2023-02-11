from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
from src.osm_configurator.control.calculation_controller_interface import ICalculationController
from src.osm_configurator.control.category_controller_interface import ICategoryController
from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController
from src.osm_configurator.control.export_controller_interface import IExportController
from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
from src.osm_configurator.control.project_controller_interface import IProjectController
from src.osm_configurator.control.settings_controller_interface import ISettingsController
import src.osm_configurator.view.states.main_window as mw

# This Test will perform manual tests on the main window
export_controller = IExportController()
category_controller = ICategoryController()
project_controller = IProjectController()
settings_controller = ISettingsController()
aggregation_controller = IAggregationController()
calculation_controller = ICalculationController()
cut_out_controller = ICutOutController()
data_visualization_controller = IDataVisualizationController()
osm_data_controller = IOSMDataController()


def test_display_main_window():
    main_window = mw.MainWindow(export_controller=export_controller,
                                category_controller=category_controller,
                                project_controller=project_controller,
                                settings_controller=settings_controller,
                                aggregation_controller=aggregation_controller,
                                calculation_controller=calculation_controller,
                                cut_out_controller=cut_out_controller,
                                data_visualization_controller=data_visualization_controller,
                                osm_data_controller=osm_data_controller,
                                )
