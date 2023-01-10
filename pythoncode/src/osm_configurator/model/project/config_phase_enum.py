from enum import Enum, unique

def _data_config_phase():
    pass

def _category_config_phase():
    pass

def _reduction_config_phase():
    pass

def _attractivity_config_phase():
    pass

def _aggregation_config_phase():
    pass

def _calculation_config_phase():
    pass


@unique
class ConfigPhase(Enum):
    """
    This enum stores the different phases of the configuration and is used to restores the last step the user
    was working on.
    """
    pass