from __future__ import annotations

import os

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

PROJECT_DIR: Final = os.path.dirname(os.path.abspath(__file__))