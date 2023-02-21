from __future__ import annotations

from src.osm_configurator.control.application_controller import ApplicationController

if __name__ == '__main__':
    application_controller: ApplicationController = ApplicationController()
    application_controller.start()

