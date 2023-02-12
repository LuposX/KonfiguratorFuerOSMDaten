from pathlib import Path
from src.osm_configurator.model.project.active_project import ActiveProject


class TestExport:
    def test_build(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject1", "Das sollte funktionieren")
        self.active_project.get_export_manager().export_project(Path("data/"))