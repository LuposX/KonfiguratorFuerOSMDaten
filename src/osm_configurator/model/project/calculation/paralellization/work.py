from __future__ import annotations

from typing import Callable
from typing import Tuple


class Work:
    """
    A work object consists out of a target function and corresponding arguments
    """
    def __init__(self, target: Callable, args: Tuple):
        self._target: Callable = target
        self._args: Tuple = args

    def get_target(self) -> Callable:
        """
        Sets the target of the Work object
        """
        return self._target

    def get_args(self) -> Tuple:
        """
        Sets the arguments of the work object
        """
        return self._args