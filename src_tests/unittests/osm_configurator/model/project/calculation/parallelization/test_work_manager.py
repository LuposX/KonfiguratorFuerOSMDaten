from __future__ import annotations

import src.osm_configurator.model.project.calculation.paralellization.work as work
import src.osm_configurator.model.project.calculation.paralellization.work_manager as work_manager

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from src.osm_configurator.model.project.calculation.paralellization.work import Work
    from src.osm_configurator.model.project.calculation.paralellization.work_manager import WorkManager


def _task(x: int, y: int):
    return x * y


def test_successful():
    work_mgr: WorkManager = work_manager.WorkManager(4)

    for i in range(100):
        next_work: Work = work.Work(_task, (i, i+1,))
        work_mgr.append_work(next_work)

    result_mp: List = work_mgr.do_all_work()
    result_mp.sort()

    result_single: List = []
    for i in range(100):
        result_single.append(_task(i, i+1))

    assert result_single == result_mp
