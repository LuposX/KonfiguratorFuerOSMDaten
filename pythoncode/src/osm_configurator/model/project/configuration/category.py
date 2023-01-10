class Category:
    """
    Models a category containing all its values and attributes
    TODO: document more clearly
    """

    active = False
    whitelist = []
    blacklist = []
    category_name = "Category Name"

    def __init__(self, whitelist, blacklist, category_name):
        """
        Constructor of the class

        Args:
            whitelist ([str]): list of the whitelist attributes
            blacklist ([str]): list of the blacklist attributes
            category_name (str): name of the category
        """
        self.activate()
        self.whitelist = whitelist
        self.blacklist = blacklist
        self.category_name = category_name

    def is_active(self):
        """
        Checks if value "active" is set

        Returns:
            Value of self.active
        """
        return self.active

    def activate(self):
        """
        Sets the active-value to True

        Returns:
             bool: True, if value was set correctly, False if value was already True
        """
        if not self.active:
            self.active = True
            return True
        return False

    def deactivate(self):
        """
        Sets the active-value to False

        Returns:
            bool: True, if value was set correctly, False if value was already False
        """
        if self.active:
            self.active = False
            return True
        return False

    def get_whitelist(self):
        """

        Returns:
            [str]: List containing all whitelist values of the class
        """
        return self.whitelist

    def set_whitelist(self, new_whitelist):
        """
        Changes the old whitelist to a new one

        Args:
            new_whitelist ([str]): value for the new whitelist

        Returns:
             bool: True, if the whitelist was overwritten successfully, else False
        """
        if self.whitelist != new_whitelist:
            self.whitelist = new_whitelist
            return True
        return False

    def get_blacklist(self):
        """

        Returns
            [str]: list containing all blacklist attributes of the class
        """
        return self.blacklist

    def set_blacklist(self, new_blacklist):
        """
        Overwrites the old Blacklist with a new value

        Args:
            new_blacklist ([str]): new value for the blacklist

        Returns:
            bool: True, if the blacklist was overwritten successfully, else False
        """
        if self.blacklist != new_blacklist:
            self.blacklist = new_blacklist
            return True
        return False

    def get_category_name(self):
        """

        Returns:
             str: name of the category
        """
        return self.category_name

    def set_category_name(self, new_category_name):
        """
        Overwrites the old category_name

        Args:
            new_category_name (str): new value for the category_name

        Returns:
            bool: True, if the overwriting process concluded successfully, else False
        """
        if self.category_name != new_category_name:
            self.category_name = new_category_name
            return True
        return False

