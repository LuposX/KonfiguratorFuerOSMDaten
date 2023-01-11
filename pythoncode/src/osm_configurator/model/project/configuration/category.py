import src.osm_configurator.model.project.configuration.calculation_method_of_area as CMA
import src.osm_configurator.model.project.configuration.attractivity_attribute as AttractivityAttribute
import src.osm_configurator.model.project.configuration.default_value_entry as DefaultValueEntry
import src.osm_configurator.model.project.configuration.calculation_method_of_area


class Category:
    """
    An internal representation of a category containing all its values and attributes
    """

    _active = False
    _whitelist = []
    _blacklist = []
    _category_name = "Category Name"
    _calculate_area = False
    _calculate_floor_area = False
    _calculation_method_of_area = CMA.CalculationMethodOfArea  # TODO: Vervollständigen durch Methoden im Enum
    _strictly_use_default_values = False
    _attractivity_attributes = []
    _default_value_list = []

    def __init__(self, whitelist, blacklist, category_name):
        """
        Creates a new instance of a "Category" class.

        Args:
            whitelist ([str]): list of the whitelist attributes
            blacklist ([str]): list of the blacklist attributes
            category_name (str): name of the category
        """
        self.activate()
        self._whitelist = whitelist
        self._blacklist = blacklist
        self._category_name = category_name

    def is_active(self):
        """
        Checks if value "active" is set

        Returns:
            Value of self.active
        """
        return self._active

    def activate(self):
        """
        Sets the active-value to True

        Returns:
             bool: True, if value was set correctly, False if value was already True
        """
        if not self._active:
            self._active = True
            return True
        return False

    def deactivate(self):
        """
        Sets the active-value to False

        Returns:
            bool: True, if value was set correctly, False if value was already False
        """
        if self._active:
            self._active = False
            return True
        return False

    def get_whitelist(self):
        """

        Returns:
            [str]: List containing all whitelist values of the class
        """
        return self._whitelist

    def set_whitelist(self, new_whitelist):
        """
        Changes the old whitelist to a new one

        Args:
            new_whitelist ([str]): value for the new whitelist

        Returns:
             bool: True, if the whitelist was overwritten successfully, else False
        """
        if self._whitelist != new_whitelist:
            self._whitelist = new_whitelist
            return True
        return False

    def get_blacklist(self):
        """

        Returns
            [str]: list containing all blacklist attributes of the class
        """
        return self._blacklist

    def set_blacklist(self, new_blacklist):
        """
        Overwrites the old Blacklist with a new value

        Args:
            new_blacklist ([str]): new value for the blacklist

        Returns:
            bool: True, if the blacklist was overwritten successfully, else False
        """
        if self._blacklist != new_blacklist:
            self._blacklist = new_blacklist
            return True
        return False

    def get_category_name(self):
        """

        Returns:
             str: name of the category
        """
        return self._category_name

    def set_category_name(self, new_category_name):
        """
        Overwrites the old category_name

        Args:
            new_category_name (str): new value for the category_name

        Returns:
            bool: True, if the overwriting process concluded successfully, else False
        """
        if self._category_name != new_category_name:
            self._category_name = new_category_name
            return True
        return False

    def get_calculate_area(self):
        """

        Returns:
             bool: value of calculate_area
        """
        return self._calculate_area

    def set_calculate_area(self, new_calculate_area):
        """
        Overwrites current calculate_area with the given value

        Args:
            new_calculate_area (bool): new value that will overwrite the existing value
        """
        self._calculate_area = new_calculate_area

    def get_calculation_method_of_area(self):
        """

        Returns:
            CalculationMethodOfArea: the calculation method of the area
        """
        return self._calculation_method_of_area

    def set_calculation_method_of_area(self, new_calculation_method):
        """
        Overwrites the already existing method to calculate the area

        Args
            new_calculation_method (CalculationMethodOfArea): new method that will overwrite the existing method

        Returns:
            calculation_method_of_area.CalculationMethodOfArea: the method with which we calculate the area.
        """
        self._calculation_method_of_area = new_calculation_method
        # TODO: Check if new-calculation-method is actually from CalculationMethodOfArea
        pass

    def get_calculate_floor_area(self):
        """

        Returns:
             bool: Value of calculate_floor_area
        """
        return self._calculate_floor_area

    def set_calculate_floor_area(self, new_calculate_floor_area):
        """
        Overwrites the existing instance of calculate_floor_area

        Args:
            new_calculate_floor_area (bool): new value for calculate_floor_are

        Returns:
            bool: True, if the overwriting process was successful, else false
        """
        if self._calculate_floor_area != new_calculate_floor_area:
            self._calculate_floor_area = new_calculate_floor_area
            return True
        return False

    def get_strictly_use_default_values(self):
        """

        Returns:
             bool: value of strictly_use_default_values
        """
        return self._strictly_use_default_values

    def set_strictly_use_default_values(self, new_strictly_use_default_values):
        """
        Overwrites the already existing value of strictly_use_default_values

        Args:
            new_strictly_use_default_values (bool): new value for strictly_use_default_values

        Return:
            True if the overwriting process was successful, else False
        """
        if self._strictly_use_default_values != new_strictly_use_default_values:
            self._strictly_use_default_values = new_strictly_use_default_values
            return True
        return False

    def get_attractivity_attributes(self):
        """
        Returns:
            List<AttractivityAttributes>: List of all used attractivity attributes
        """
        return self._attractivity_attributes

    def add_attractivity_attribute(self, new_attractivity_attribute):
        """
        Adds a new attractivity attribute to the list

        Args:
            new_attractivity_attribute (AttractivityAttribute): new attractivityAttribute that will be added

        Returns:
            bool: True, if the attribute was added successfully, else False
        """
        if new_attractivity_attribute not in self._attractivity_attributes:
            self._attractivity_attributes.append(new_attractivity_attribute)
            return True
        return False

    def remove_attractivity_attribute(self, attractivity_attribute):
        """
        Removes an already existing attribute from the list

        Args:
            attractivity_attribute (AttractivityAttribute): attractivity attribute that will be removed from the list

        Returns:
            True, if the element was removed, else False
        """
        if attractivity_attribute in self._attractivity_attributes:
            self._attractivity_attributes.remove(attractivity_attribute)
            return True
        return False

    def get_default_value_list(self):
        """

        Returns:
            List<DefaultValueEntry>: List of all used default values
        """
        return self._default_value_list

    def add_default_value_entry(self, new_default_value_entry):
        """
        Adds a new value to the default_value_entry list

        Args:
            new_default_value_entry (DefaultValueEntry): element to add

        Returns:
            bool: True, if element was added successfully, else False
        """
        if new_default_value_entry not in self._default_value_list:
            self._default_value_list.append(new_default_value_entry)
            return True
        return False

    def remove_default_value_entry(self, default_value_entry):
        """
        Removes an already existing element from the default_value_entry list

        Args:
            default_value_entry (DefaultValueEntry): value that will be removed

        Returns:
            bool: True, if the element was removed successfully, else False
        """
        if default_value_entry in self._default_value_list:
            self._default_value_list.remove(default_value_entry)
            return True
        return False

    def move_default_value_entry_up(self, default_value_entry):
        """
        Moves an already existing default value from the list one element up

        Args:
            default_value_entry (DefaultValueEntry): element from the list, that will be incremented by one

        Returns:
            bool: True, if the change was successful, else False
        """
        if (default_value_entry not in self._default_value_list) \
                or self._default_value_list.index(default_value_entry) <= 0:
            return False
        index = self._default_value_list.index(default_value_entry)
        self._default_value_list[index - 1], self._default_value_list[index] \
            = self._default_value_list[index], self._default_value_list[index - 1]
        return True

    def move_default_value_entry_down(self, default_value_entry):
        """
        Moves an already existing default value from list one element down

        Args:
            default_value_entry (DefaultValueEntry): element from the list, that will be decremented by one

        Returns:
            bool: True, if the change was successful, else false
        """
        if (default_value_entry not in self._default_value_list) \
                or self._default_value_list.index(default_value_entry) <= 0:
            return False
        index = self._default_value_list.index(default_value_entry)
        self._default_value_list[index + 1], self._default_value_list[index] \
            = self._default_value_list[index], self._default_value_list[index + 1]
        return True
