from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod


class AggreationControllerStub(IAggregationController):
    def get_aggregation_methods(self) -> list[AggregationMethod]:
        pass

    def is_aggregation_method_active(self, method: AggregationMethod) -> bool:
        pass

    def set_aggregation_method_active(self, method: AggregationMethod, active: bool) -> bool:
        pass