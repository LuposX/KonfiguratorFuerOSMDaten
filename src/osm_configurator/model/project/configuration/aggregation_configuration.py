from __future__ import annotations

import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum_i

from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod


class AggregationConfiguration:
    """
    This class manages the different aggregation methods stored in an enum. Therefore, it activates and deactivates
    those methods. Activating means that this aggregation methods should be used during the aggregation phase in the
    calculation. Deactivating means the opposite.
    """

    def __init__(self):
        """
        Creates a new instance of the AggregationConfiguration.
        """

        self._aggregation_method_state: Dict = {}
        all_aggregation_methods = [member.name for member in aggregation_method_enum_i]
        for enum_name in all_aggregation_methods:
            self._aggregation_method_state.update({enum_name: False})

    def get_all_aggregation_methods(self):
        """
        Gives back a List of all possible aggregation methods.

        Returns:
            list[aggregation_method_enum.AggregationMethod]: A list containing all aggregation methods.
        """
        _all_methods = []

        for method in AggregationMethod:
            _all_methods.append(method)
        return _all_methods

    def is_aggregation_method_active(self, method):
        """
        Checks, if a given aggregation method is active.

        Args:
            method (aggregation_method_enum.AggregationMethod): The method, which is to be checked.

        Returns:
            bool: True if the aggregation method is active, otherwise false.
        """

        return self._aggregation_method_state.get(method)

    def set_aggregation_method_active(self, method, active):
        """
        Changes the aggregation method from active to inactive and vice versa. If an already active aggregation
        method should be activated, it stays active. The same applies to inactive aggregation methods, which should be deactivated.

        Args:
            method (aggregation_method_enum.AggregationMethod): The method, which state should be changed.
            active (bool): This is the new state of the aggregation method.

        Returns:
            bool: True if changing the state works, otherwise false.
        """

        if method in aggregation_method_enum_i:
            self._aggregation_method_state.update({method: active})
            return True
        return False
