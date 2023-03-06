from __future__ import annotations


import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.settings_controller as settings_controller

import src.osm_configurator.model.application.application as application

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.settings_controller_interface import ISettingsController

    from src.osm_configurator.model.application.application_interface import IApplication


class TestUseCase05:
    def test_edt_settings(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        settings_ctrl: ISettingsController = settings_controller.SettingsController(model)

        # Test Changing Settings
        assert not project_ctrl.is_project_loaded()
        assert settings_ctrl.get_project_default_folder() is not None
        assert settings_ctrl.set_project_default_folder(settings_ctrl.get_project_default_folder())
