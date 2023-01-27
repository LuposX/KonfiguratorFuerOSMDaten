from __future__ import annotations

import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum

from typing import TYPE_CHECKING

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
        self._length = 2
        self._number_of_methods = 0
        self._aggregation_methods_status = [[] for x in range(self._length)]

        for method in aggregation_method_enum.AggregationMethod:
            self._aggregation_methods_status.append([method, False])
            self._number_of_methods = self._number_of_methods + 1

    def get_all_aggregation_methods(self):
        """
        Gives back a List of all possible aggregation methods.

        Returns:
            list[aggregation_method_enum.AggregationMethod]: A list containing all aggregation methods.
        """
        _all_methods = []

        for method in aggregation_method_enum.AggregationMethod:
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
        for item in range(self._number_of_methods):
            if self._aggregation_methods_status[item][0] == method:
                return self._aggregation_methods_status[item][1]

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
        for item in range(self._number_of_methods):
            if self._aggregation_methods_status[item][0] == method:
                self._aggregation_methods_status[item][1] = active
                return True
        return False
