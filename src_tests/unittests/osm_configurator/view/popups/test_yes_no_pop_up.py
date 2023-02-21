import os.path

import pytest

import src.osm_configurator.view.popups.yes_no_pop_up as ynpu


def _prepare(target_path):
    result_folder = os.path.dirname(target_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    if os.path.exists(target_path):
        os.remove(target_path)


def test_correct_init():
    popup = ynpu.YesNoPopUp(message="Wir Kek", func=print)
    popup.destroy()
