from __future__ import annotations

from customtkinter import CTkFrame

from abc import ABC
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.freezable import Freezable


class TopLevelFrame(CTkFrame, Activatable, Freezable, ABC):
    """
    This class describes a frame that has a fully developed functionality and that can be placed on a window.
    A TopLevelFrame might have manageable frames below him.
    """
    pass
