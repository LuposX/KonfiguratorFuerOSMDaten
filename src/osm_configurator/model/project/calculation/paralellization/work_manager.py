from __future__ import annotations

import multiprocessing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing import List
    from typing import Tuple
    from typing import Callable
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
                self._do_work(self._work_to_do.pop())

    def _can_do_more_work(self) -> bool:
        pass

    def _do_work(self, work: Work):
        usage_queue: SimpleQueue = multiprocessing.SimpleQueue()
        process: Process = multiprocessing.Process(target=self._worker_entry_point,
                                                   args=(work, self._return_queue, usage_queue,))

        self._workers.append(process)
        process.start()

        while usage_queue.empty():
            pass  # Maybe sleep a little

        data_needed: int


    def _worker_entry_point(self, work: Work, return_queue: SimpleQueue, usage_queue: SimpleQueue):
        """
        This function is the point, where the starting processes start working
        """
        # Calculate data needed
        arguments: Tuple = work.get_args()
        mem_usage: Callable = work.get_mem_usage_function()
        data_needed: int = mem_usage(arguments)

        # send the approximated data needed back to the calling process
        usage_queue.put(data_needed)

        # Execute task and send the return value back to the calling process

        target: Callable = work.get_target_function()
        return_value: Any = target(arguments)

        return_queue.put(return_value)
