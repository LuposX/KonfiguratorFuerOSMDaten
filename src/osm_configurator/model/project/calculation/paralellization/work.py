from __future__ import annotations

from typing import Callable
from typing import Tuple


class Work:
    """
    A work object consists out of a target function and corresponding arguments.
    """
    def __init__(self, target: Callable, args: Tuple):
        """
        Creates a new work-object (a new task).
        Args:
            target (Callable): The actual task. Executing this target-function is the task of the work object
            args (Tuple): The Argumnts that are passed to the target function
        """
        self._target: Callable = target
        self._args: Tuple = args

    def get_target_function(self) -> Callable:
        """
        returns the target function of the Work object
        """
        return self._target

    def get_args(self) -> Tuple:
        """
        Gets the arguments of the work object: The Argumnts that are passed to the target function
        """
        return self._args
