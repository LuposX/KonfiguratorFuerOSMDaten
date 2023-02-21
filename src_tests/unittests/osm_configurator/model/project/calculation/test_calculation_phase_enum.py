import src.osm_configurator.model.project.calculation.calculation_phase_enum as cpe
import pytest


@pytest.mark.parametrize("phase", [
    cpe.CalculationPhase.NONE,
    cpe.CalculationPhase.GEO_DATA_PHASE,
    cpe.CalculationPhase.TAG_FILTER_PHASE,
    cpe.CalculationPhase.REDUCTION_PHASE,
    cpe.CalculationPhase.ATTRACTIVITY_PHASE,
    cpe.CalculationPhase.AGGREGATION_PHASE
])
def test_get_correct_getters(phase):
    assert phase.get_name() is not None
    assert phase.get_folder_name_for_results() is not None
    assert phase.get_order() is not None
