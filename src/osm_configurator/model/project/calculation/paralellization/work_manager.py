from __future__ import annotations

import multiprocessing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing import List
    from typing import Tuple
    from typing import Callable
    from src.osm_configurator.model.project.calculation.paralellization.work import Work
    from multiprocessing import Pool


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
        self._max_workers = int(max_processes)
        self._work_to_do: List[Work] = []

    def append_work(self, work: Work):
        """
        Adds a piece of work to the manager

        Args:
            work (Work): The work/task that is added to the task manager
        """
        self._work_to_do.append(work)

    def do_all_work(self) -> List:
        """
        Executes all work that has been appended till now.

        Returns:
            List: A list of the return-values of all the work.
        """
        pool: Pool
        with multiprocessing.Pool(processes=self._max_workers) as pool:
            result = pool.map(self._worker_entry_point, self._work_to_do)
            pool.terminate()
            pool.join()
            return result

    @staticmethod
    def _worker_entry_point(work: Work):
        """
        This function is the point, where the starting processes start working
        """
        arguments: Tuple = work.get_args()
        target: Callable = work.get_target_function()

        return_value: Any = target(*arguments)
        return return_value
