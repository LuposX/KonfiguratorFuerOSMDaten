from abc import ABC
from src.osm_configurator.model.application.application_interface import IApplication


class Application(IApplication, ABC):
    __doc__ = IApplication.__doc__

    def __init__(self):
        """
        Creates a new instance of the Application.
        """
        pass

