from __future__ import annotations

import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum_i
import pandas as pd
import numpy as np


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pandas import Series


class TestAggregationMethod:
    def test_sum(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, 4, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])
        data4: Series = pd.Series([-1, -1, 1, 2, np.nan])

        assert aggregation_method_enum_i.AggregationMethod.SUM.calculate_aggregation(data1) == 10
        assert aggregation_method_enum_i.AggregationMethod.SUM.calculate_aggregation(data2) == 1
        assert aggregation_method_enum_i.AggregationMethod.SUM.calculate_aggregation(data3) == 0
        assert aggregation_method_enum_i.AggregationMethod.SUM.calculate_aggregation(data4) == 1

    def test_mean(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, 4, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])

        assert aggregation_method_enum_i.AggregationMethod.MEAN.calculate_aggregation(data1) == 2.5
        assert aggregation_method_enum_i.AggregationMethod.MEAN.calculate_aggregation(data2) == 1
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.MEAN.calculate_aggregation(data3))

    def test_median(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, 4, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])

        assert aggregation_method_enum_i.AggregationMethod.MEDIAN.calculate_aggregation(data1) == 2.5
        assert aggregation_method_enum_i.AggregationMethod.MEDIAN.calculate_aggregation(data2) == 1
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.MEDIAN.calculate_aggregation(data3))

    def test_maximum(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, 4, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])

        assert aggregation_method_enum_i.AggregationMethod.MAXIMUM.calculate_aggregation(data1) == 4
        assert aggregation_method_enum_i.AggregationMethod.MAXIMUM.calculate_aggregation(data2) == 1
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.MAXIMUM.calculate_aggregation(data3))

    def test_minimum(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, 4, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])

        assert aggregation_method_enum_i.AggregationMethod.MINIMUM.calculate_aggregation(data1) == 1
        assert aggregation_method_enum_i.AggregationMethod.MINIMUM.calculate_aggregation(data2) == 1
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.MINIMUM.calculate_aggregation(data3))

    def test_25_quartile(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, 4, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])

        assert aggregation_method_enum_i.AggregationMethod.QUANTILE_25.calculate_aggregation(data1) == 1.75
        assert aggregation_method_enum_i.AggregationMethod.QUANTILE_25.calculate_aggregation(data2) == 1
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.QUANTILE_25.calculate_aggregation(data3))

    def test_variance(self):
        # create testing data
        data1: Series = pd.Series([1, 2, 3, np.nan])
        data2: Series = pd.Series([1])
        data3: Series = pd.Series([np.nan])

        assert aggregation_method_enum_i.AggregationMethod.VARIANCE.calculate_aggregation(data1) == 1
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.VARIANCE.calculate_aggregation(data2))
        assert pd.isna(aggregation_method_enum_i.AggregationMethod.VARIANCE.calculate_aggregation(data3))