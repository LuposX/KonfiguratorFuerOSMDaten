import pythoncode.src.osm_configurator.model.project.configuration.category


class CategoryManager:
    """
    Category Manager holds a list of categories and changes them according to the given needs

    """

    categories = [] # List of categories

    def __init__(self, categories):
        """
        Constructor of the class

        Args:
            categories (Category): Starting list of categories
        """
        self.categories = categories

    def get_category(self, index):
        """

        Args:
            index (int): Index in the categories-list, that will be returned

        Returns:
            Index of the element, if index is correct, else -1
        """
        if index < 0 or index > len(self.categories):
            return -1
        return self.categories[index]

    def get_categories(self):
        """

        Returns:
            List<Category>: List of the chosen categories
        """
        return self.categories

    def create_category(self, new_category):
        """
        Adds a new category to the list of categories, if element does not exist already

        Args:
            new_category (Category): Category, that will be added to the list

        Returns:
            bool: True, if the category was added successfully, else False
        """
        if new_category not in self.categories:
            self.categories.append(new_category)
            return True
        return False

    def remove_category(self, category):
        """
        Removes the given category from the categories list, if element already exists

        Args:
            category (Category): Category that will be removed

        Returns:
            bool: True, if the element was removed correctly, else false
        """
        if category in self.categories:
            self.categories.remove(category)
            return True
        return False

    def override_categories(self, new_category_list):
        """
        Overwrites the list of categories with the given list, if both lists are not identical

        Args:
            new_category_list (List<Categories>): List of categories, that will overwrite the already existing list

        Returns:
            bool: True, if the replacement was successful, else False
        """
        if self.categories != new_category_list:
            self.categories = new_category_list
            return True
        return False

    def merge_categories(self, category_input_list):
        """
        Merges the existing category list with the given list if both lists are not identical

        Args:
            category_input_list (List<Category>): New list of categories that will be merged into the existing list

        Returns:
            bool: True, if the merging was successful, else False
        """
        if self.categories == category_input_list:
            return False

        for category in category_input_list:
            if category not in self.categories:
                self.categories.append(category)
        return True
