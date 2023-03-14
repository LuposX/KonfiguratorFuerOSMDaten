from __future__ import annotations
from multiprocessing import freeze_support

import os

from src.osm_configurator.control.application_controller import ApplicationController

if __name__ == '__main__':
    freeze_support()
    application_controller: ApplicationController = ApplicationController(os.path.dirname(os.path.abspath(__file__)))
    application_controller.start()

