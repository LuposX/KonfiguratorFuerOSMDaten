from src.osm_configurator.control.aggregation_controller_interface import IAggregationController

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
        pass

    def get_aggregation_methods(self) -> list[AggregationMethod]:
        pass

    def is_aggregation_method_active(self, method: AggregationMethod) -> bool:
        pass

    def set_aggregation_method_active(self, method: AggregationMethod, active: bool) -> bool:
        pass
