import os.path

import pytest


import src.osm_configurator.view.popups.alert_pop_up as apu


def _prepare(target_path):
    result_folder = os.path.dirname(target_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    if os.path.exists(target_path):
        os.remove(target_path)


def test_correct_creation():
    popup = apu.AlertPopUp("Ich Kek")
    popup.destroy()
