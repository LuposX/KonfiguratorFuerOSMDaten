from __future__ import annotations

from typing import TYPE_CHECKING
from tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.file_deletion as fd
from pathlib import Path
import os

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


def test_correct_reset_folder1():
    deleter: FileDeletion = fd.FileDeletion()
    path: Path = Path(os.path.join(TEST_DIR, "build/file_deletion/folder"))
    file_path: Path = Path(os.path.join(path, "hello.txt"))

    assert deleter.reset_folder(path)
    assert os.path.exists(path)

    f = open(file_path, "x")
    f.close()

    assert os.path.exists(file_path)

    assert deleter.reset_folder(path)
    assert os.path.exists(path)
    assert not os.path.exists(file_path)
