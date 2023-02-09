from __future__ import annotations

from typing import Callable
from typing import Tuple


class Work:
    """
    A work object consists out of a target function, a function for appoximating the data usage of the task
    and corresponding arguments.
    """
    def __init__(self, target: Callable, mem_usage: Callable, args: Tuple):
        """
        Creates a new work-object (a new task).
        Args:
            target (Callable): The actual task. Executing this target-function is the task of the work object
            mem_usage (Callable): A function which preacceses and approximates the amount of data that needs to be loaded in memory to fulfill the task. Returns the number of bytes needed.
            args (Tuple): The Argumnts that are passed to the target function, aswell as the mem_usage function
        """
        self._target: Callable = target
        self._args: Tuple = args
        self._mem_usage = mem_usage

    def get_target_function(self) -> Callable:
        """
        returns the target function of the Work object
        """
        return self._target

    def get_mem_usage_function(self) -> Callable:
        """
        Returns the mem_usage function of the Work object. It is a function which preacceses and approximates the
        amount of data that needs to be loaded in memory to fulfill the task. The function returns the number of
        bytes needed.
        """
        return self._target

    def get_args(self) -> Tuple:
        """
        Gets the arguments of the work object: The Argumnts that are passed to the target function, aswell
        as the mem_usage function
        """
        return self._args