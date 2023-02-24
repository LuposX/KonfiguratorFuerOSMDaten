from __future__ import annotations

from typing import List

from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration


class TestAggregationConfiguration:
    def test_get_all_aggregation_methods(self):
        self.aggregation_configurator: AggregationConfiguration = AggregationConfiguration()
        all_methods: List[AggregationMethod] = []
        for method in AggregationMethod:
            all_methods.append(method)
        assert self.aggregation_configurator.get_all_aggregation_methods() == all_methods

    def test_is_aggregation_method_active(self):
        self.aggregation_configurator: AggregationConfiguration = AggregationConfiguration()
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.SUM, True)
        assert self.aggregation_configurator.is_aggregation_method_active(AggregationMethod.SUM)
        assert not self.aggregation_configurator.is_aggregation_method_active(AggregationMethod.MEDIAN)

    def test_set_aggregation_method_active(self):
        self.aggregation_configurator: AggregationConfiguration = AggregationConfiguration()
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.SUM, True)
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.MEAN, True)
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.SUM, False)
        assert not self.aggregation_configurator.is_aggregation_method_active(AggregationMethod.SUM)
        assert self.aggregation_configurator.is_aggregation_method_active(AggregationMethod.MEAN)

    def test_get_all_active_aggregation_methods(self):
        self.aggregation_configurator: AggregationConfiguration = AggregationConfiguration()
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.SUM, True)
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.MEAN, True)
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.QUANTILE_25, True)
        self.aggregation_configurator.set_aggregation_method_active(AggregationMethod.MEAN, False)
        all_active_methods: List[AggregationMethod] = [AggregationMethod.SUM, AggregationMethod.QUANTILE_25]
        assert self.aggregation_configurator.get_all_active_aggregation_methods() == all_active_methods