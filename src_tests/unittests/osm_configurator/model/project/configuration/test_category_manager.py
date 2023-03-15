from typing import List

from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute



class TestCategoryManager:
    def test_get_activated_attribute(self):
        category_manager: CategoryManager = CategoryManager()
        activated_attributes: List[Attribute] = category_manager.get_activated_attribute()
        assert len(activated_attributes) == 0

    def test_get_activated_attribute_with_attributes(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category = Category("Test Category")
        category.set_attribute(Attribute.NUMBER_OF_FLOOR, True)
        category_manager.create_category(category)
        activated_attributes: List[Attribute] = category_manager.get_activated_attribute()
        assert len(activated_attributes) == 1

    def test_get_category(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category | None = category_manager.get_category("Building")
        assert category.get_category_name() == "Building"

    def test_get_category_with_not_existing_category(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category | None = category_manager.get_category("not_existing_category")
        assert category is None

    def test_get_category_with_empty_string(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category | None = category_manager.get_category("")
        assert category is None

    def test_create_category(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category = Category("Test Category")
        assert category_manager.create_category(category)

    def test_create_category_with_empty_string(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category = Category("")
        assert not category_manager.create_category(category)

    def test_create_category_with_existing_category(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category = Category("Test Category")
        assert category_manager.create_category(category)
        assert not category_manager.create_category(category)

    def test_remove_category(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category = Category("Test Category")
        category_manager.create_category(category)
        assert category_manager.remove_category(category)

    def test_remove_category_with_not_existing_category(self):
        category_manager: CategoryManager = CategoryManager()
        category: Category = Category("Test Category")
        assert not category_manager.remove_category(category)