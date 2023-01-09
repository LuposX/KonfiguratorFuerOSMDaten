from abc import ABC
from src.osm_configurator.model.application.application_interface import ApplicationInterface


class Application(ApplicationInterface, ABC):
    __doc__ = ApplicationInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the Application.
        """
        pass

