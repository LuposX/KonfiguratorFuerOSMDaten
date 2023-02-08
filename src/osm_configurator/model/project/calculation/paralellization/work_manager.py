from __future__ import annotations

import multiprocessing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from src.osm_configurator.model.project.calculation.paralellization.work import Work
    from multiprocessing import Process
    from multiprocessing import SimpleQueue


class WorkManager:
    """
    The WorkManager allow a parallelization of work via multiprocessing.
    """
    def __init__(self, max_processes: int):
        """
        Creates an empty work manager.
        Args:
            max_processes (int): The maximal number of processes that might be run at the same time
        """
        self._max_workers = max_processes
        self._work_to_do: List[Work] = []
        self._workers: List[Process] = []
        self._return_queue: SimpleQueue = multiprocessing.SimpleQueue()

    def append_work(self, work: Work):
        """
        Adds a piece of work to the manager
        """
        self._work_to_do.append(work)

    def do_all_work(self) -> List:
        """
        Executes all work that has been append till now.

        Returns:
            List: A list of the return-values of all the work.
        """
        while len(self._work_to_do) > 0:
            if self._can_do_more_work():
                self._add_worker(self._work_to_do.pop())


    def _can_do_more_work(self) -> bool:
        pass

    def _add_worker(self, work: Work):
        pass