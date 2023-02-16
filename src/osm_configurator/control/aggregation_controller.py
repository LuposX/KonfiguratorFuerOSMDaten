from src.osm_configurator.control.aggregation_controller_interface import IAggregationController

from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod


class AggregationController(IAggregationController):
    __doc__ = IAggregationController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the AggregationController with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._aggregation_configurator: AggregationConfiguration = model.get_active_project().get_config_manager().get_aggregation_configuration()

    def get_aggregation_methods(self) -> list[AggregationMethod]:
        return self._aggregation_configurator.get_all_aggregation_methods()

    def is_aggregation_method_active(self, method: AggregationMethod) -> bool:
        return self._aggregation_configurator.is_aggregation_method_active(method)

    def set_aggregation_method_active(self, method: AggregationMethod, active: bool) -> bool:
        return self._aggregation_configurator.set_aggregation_method_active(method, active)
