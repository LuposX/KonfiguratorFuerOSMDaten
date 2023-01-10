class AggregationConfiguration:

    """
    This class manages the different aggregation methods stored in an enum. Therefore, it activates and deactivates
    those methods. Activating means that this aggregation methods should be used during the aggregation phase in the
    calculation. Deactivating means the opposite.
    To do this the class holds a complete list of aggregation methods and assigns a bool to each of it.
    """

    def __init__(self):
        """
        Creates a new instance of the AggregationConfiguration.
        """
        pass

    def get_all_aggregation_methods(self):
        """
        Gives back a List of all possible aggregation methods.

        Returns:
            List<AggregationMethod>: A list containing all aggregation methods.
        """
        pass

    def is_aggregation_method_active(self, method):
        """
        Checks, if a given aggregation method is active.

        Args:
            method (AggregationMethod): The new method, which is to be checked.

        Returns:
            bool: True if the aggregation method is active, otherwise false.
        """
        pass

    def set_aggregation_method_active(self, method, active):
        """
        Changes the aggregation method from active to inactive and vice versa. If an already active aggregation
        method should be activated, it stays active. The same applies to inactive aggregation methods, which should be deactivated.

        Args:
            method (AggregationMethod): The method, which state should be changed.
            active (bool): This is the new state of the aggregation method.

        Returns:
            bool: True if changing the state works, otherwise false.
        """
        pass