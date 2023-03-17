from __future__ import annotations

from enum import Enum

import src.osm_configurator.view.constants.frame_constants as frame_constants_i


class PopUpConstants(Enum):
    """
    Constants fpr PopUps
    """
    POPUP_SIZE = "400x200"
    POPUP_FG_COLOR = frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value
