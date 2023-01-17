from abc import ABC, abstractmethod

import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.state_manager


class TopLevelFrame(ABC):
    """
    This class describes a frame that has a fully developed functionality and that can be placed on a window.
    A TopLevelFrame might have manageable frames below him.
    """
    pass

