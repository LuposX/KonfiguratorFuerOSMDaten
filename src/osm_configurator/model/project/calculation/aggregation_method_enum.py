from __future__ import annotations

from enum import Enum, unique

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, Callable
    from pandas import Series


def _sum(df: Series):
    return df.sum()


def _mean(df: Series) -> float:
    return df.mean()


def _maximum(df: Series) -> float:
    return df.max()


def _minimum(df: Series) -> float:
    return df.min()


def _variance(df: Series) -> float:
    return df.var()


def _standard_deviation(df: Series) -> float:
    return df.std()


def _median(df: Series) -> float:
    return df.median()


def _25_quantile(df: Series) -> float:
    return df.quantile(0.25)


def _75_quantile(df: Series) -> float:
    return df.quantile(0.75)


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
    MEAN = (_mean, "mean")  #: Calculates the mean of the attractivity attribute over all osm elements from the data.
    MAXIMUM = (
    _maximum, "maximum")  #: Calculates the maximum of the attractivity attribute over all osm elements from the data.
    MINIMUM = (
    _minimum, "minimum")  #: Calculates the minimum of the attractivity attribute over all osm elements from the data.
    VARIANCE = (_variance, "variance")
    STANDARD_DERIVATIVE = (_standard_deviation, "Standard deviation")
    MEDIAN = (_median, "Median")
    QUANTILE_25 = (_25_quantile, "25_Quantile")
    QUANTILE_75 = (_75_quantile, "75_Quantile")

    def calculate_aggregation(self, data: Series) -> float:
        """
        Executes the aggregation method of the called enum type.

        Args:
            data (Series): The data on which we want to execute the function on, should be a Series containing attractitivity attributes.

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

    def convert_str_to_aggregation_method(mode: str) -> AggregationMethod | None:
        """
        Converts a given string to the associated AggregationMethod.

        Args:
            mode (str): The string.

        Returns:
            AggregationMethod: Associated AggregationMethod.
        """
        for method in AggregationMethod:
            if method.get_name() == mode:
                return method
        return None
