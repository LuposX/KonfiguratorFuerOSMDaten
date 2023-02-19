from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod


class AggregationControllerStub(IAggregationController):
    def get_aggregation_methods(self) -> list[AggregationMethod]:
        return [AggregationMethod.AVERAGE, AggregationMethod.LOWER_QUARTILE, AggregationMethod.MAXIMUM]

    def is_aggregation_method_active(self, method: AggregationMethod) -> bool:
        return True

    def set_aggregation_method_active(self, method: AggregationMethod, active: bool) -> bool:
        return True
