import os.path

import src.osm_configurator.view.popups.alert_pop_up as apu


def _prepare(target_path):
    result_folder = os.path.dirname(target_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    if os.path.exists(target_path):
        os.remove(target_path)


@pytest.mark.skip(reason="pytest not supported yet")
@pytest.mark.parametrize(["Ich Kek", "Du Kek", "Er sie es Kek", "Wir Kek", "Ihr Kek", "Sie Kek"])
def test_correct_creation(message):
    popup = apu.AlertPopUp(message)
    popup.destroy()
