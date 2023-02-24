from src.osm_configurator.model.project.configuration.category import Category


class TestCategory:
    def test_is_active(self):
        self.category: Category = Category("TestName")
        assert self.category.is_active()

    def test_activate(self):
        self.category: Category = Category("TestName")
        assert self.category.is_active()