from __future__ import annotations

import os

from src.osm_configurator.control.application_controller import ApplicationController

if __name__ == '__main__':
    application_controller: ApplicationController = ApplicationController(os.path.dirname(os.path.abspath(__file__)))
    application_controller.start()

