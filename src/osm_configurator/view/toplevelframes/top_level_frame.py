from __future__ import annotations

import customtkinter

import src.osm_configurator.view.states.state_manager

from abc import ABC, abstractmethod
from src.osm_configurator.view.activatable import Activatable


class TopLevelFrame(Activatable, customtkinter.CTkFrame):
    """
    This class describes a frame that has a fully developed functionality and that can be placed on a window.
    A TopLevelFrame might have manageable frames below him.
    """
    pass

