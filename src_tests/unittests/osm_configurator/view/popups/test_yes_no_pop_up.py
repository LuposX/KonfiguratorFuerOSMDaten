import os.path

import src.osm_configurator.view.popups.yes_no_pop_up as ynpu


def _prepare(target_path):
    result_folder = os.path.dirname(target_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    if os.path.exists(target_path):
        os.remove(target_path)


@pytest.mark.skip(reason="pytest not supported yet")
@pytest.mark.parametrize(["Ich Kek", "Du Kek", "Er sie es Kek", "Wir Kek", "Ihr Kek", "Sie Kek"], lambda x: print(x))
def test_correct_init(message, func):
    popup = ynpu.YesNoPopUp(message=message, func=func)
    popup.destroy()
