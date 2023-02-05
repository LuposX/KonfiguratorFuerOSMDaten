from __future__ import annotations

from enum import Enum, unique

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, Callable
    from geopandas import GeoDataFrame

def _sum(df: GeoDataFrame):
    pass


def _average(df: GeoDataFrame):
    pass


def _mean(df: GeoDataFrame) -> float:
    pass


def _upper_quartile(df: GeoDataFrame) -> float:
    pass


def _lower_quartile(df: GeoDataFrame) -> float:
    pass


def _maximum(df: GeoDataFrame) -> float:
    pass


def _minimum(df: GeoDataFrame) -> float:
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

    def calculate_aggregation(self, data: GeoDataFrame) -> float:
        """
        Executes the aggregation method of the called enum type.

        Args:
            data (geopandas.GeoDataFrame): The data on which we want to execute the function on, should be a GeoDataFrame containing osm elements.

        Returns:
            float: The aggregated value of the attractivity values from all osm elements.
        """
        return self.value[0](data)

    def get_name(self):
        """
        Getter for the name of the enum type.

        Returns:
            str: Name of the enum type
        """
        return self.value[1]
