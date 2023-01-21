from __future__ import annotations

import src.osm_configurator.model.application.application_interface
import src.osm_configurator.model.project.calculation.aggregation_method_enum


class AggregationController:
    """
    The AggregationController is responsible for consistently forwarding requests to the model, regarding the aggregation-calculations and the aggregation methods of the currently selected project.
    """

    def __init__(self, model):
        """
        Creates a new instance of the AggregationController with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_aggregation_methods(self):
        """
        Returns a list of all aggregation methods that are available.
        This function returns all available aggregation methods, not just the ones that are active in the current project.

        Returns:
            list[aggregation_method_enum.AggregationMethod]: The list of the available aggregation methods.
        """
        pass

    def is_aggregation_method_active(self, method):
        """
        Checks, whether an aggregation method is active in the currently selected project.

        Args:
            method (aggregation_method_enum.AggregationMethod): The aggregation method that is checked for.

        Returns:
            bool: True, if there is currently a project selected and the given aggregation method is active in it; False otherwise.
        """
        pass

    def set_aggregation_method_active(self, method, active):
        """
        Activates or deactivates an aggregation method (of the currently selected project).
        Activates the given method, if active=True and deactivates it otherwise.

        Args:
            method (aggregation_method_enum.AggregationMethod): The aggregation method we want to deactivate/activate.
            active (bool): True, if we want to activate the given method; False, if we want to deactivate it.

        Returns:
            bool: True, if a project is currently selected and the aggregation method was (de-)activated successfully; False, otherwise.
        """
        pass
