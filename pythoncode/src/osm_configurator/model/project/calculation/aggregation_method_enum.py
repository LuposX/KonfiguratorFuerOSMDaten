from __future__ import annotations

from enum import Enum, unique
from typing import Tuple, Callable
from geopandas import GeoDataFrame


def _sum(data, attractivity_name):
    pass


def _average(data, attractivity_name):
    pass


def _mean(data, attractivity_name):
    pass


def _upper_quartile(data, attractivity_name):
    pass


def _lower_quartile(data, attractivity_name):
    pass


def _maximum(data, attractivity_name):
    pass


def _minimum(data, attractivity_name):
    pass


@unique
class AggregationMethod(Enum):
    """
    This enum describes all the available aggregation methods that are possible to use.
    Whereby an aggregation methods is a method, that takes in data and an attractivity attribute. Finally, it outputs
    and calculates a function on these parameters.
    The first argument points towards the function, while the second argument is the name of the method.
    """
    # Attributes are from the type (Tuple[Callable, str])
    SUM = (_sum, "sum")  #: Calculates the sum of the attractivity attribute over all osm elements from the data.
    AVERAGE = (_average, "average")  #: Calculates the average of the attractivity attribute over all osm elements from the data.
    MEAN = (_mean, "mean")  #: Calculates the mean of the attractivity attribute over all osm elements from the data.
    UPPER_QUARTILE = (_upper_quartile, "upper quartile")  #: Calculates the upper_quartile of the attractivity attribute over all osm elements from the data.
    LOWER_QUARTILE = (_lower_quartile, "lower quartile")  #: Calculates the lower quartile of the attractivity attribute over all osm elements from the data.
    MAXIMUM = (_maximum, "maximum")  #: Calculates the maximum of the attractivity attribute over all osm elements from the data.
    MINIMUM = (_minimum, "minimum")  #: Calculates the minimum of the attractivity attribute over all osm elements from the data.

    def calculate_aggregation(self, data, attractivity_name):
        """
        Executes the aggregation method of the called enum type.

        Args:
            data (geopandas.GeoDataFrame): The data on which we want to execute the function on, should be a GeoDataFrame containing osm elements.
            attractivity_name (str): This is the name of the attractivity through which we want to call the function,
                                        the attractivity_name should be the name of a column in the data GeoDataFrame.

        Returns:
            float: The aggregated value of the attractivity values from all osm elements.
        """
        return self.value[0](data, attractivity_name)

    def get_name(self):
        """
        Getter for the name of the enum type.

        Returns:
            str: Name of the enum type
        """
        return self.value[1]
