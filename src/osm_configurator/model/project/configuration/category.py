from __future__ import annotations

import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum
import src.osm_configurator.model.project.configuration.attractivity_attribute
import src.osm_configurator.model.project.configuration.default_value_entry
import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute


class Category:
    """
    Represents a category. A category is a collection of configurations for the calculation process. A category defines which OSM-elements are contained by it with a white- and a blacklist. All configurations of the category do only affect does OSM-elements.
    """

    _active = False
    _whitelist = [] # this should be List[Tuple[str, str]], a list of key,value pairs
    _blacklist = []
    _category_name = "Category Name"
    _calculate_area = False
    _calculate_floor_area = False
    # _calculation_method_of_area = CMA.CalculationMethodOfArea  # TODO: Vervollständigen durch Methoden im Enum
    _strictly_use_default_values = False
    _attractivity_attributes = []
    _default_value_list = []

    def __init__(self):
        """
        Creates a new instance of a "Category" class.
        """
        pass

    def get_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all used attributes, of the categories.
        This is used to know which tags we need to save.

        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        pass

    def is_active(self):
        """
        Checks if value "active" is set.

        Returns:
            bool: True if active, false if inactive.
        """
        return self._active

    def activate(self):
        """
        Sets the active-value to True.

        Returns:
             bool: True, if value was set correctly, False if value was already True.
        """
        if not self._active:
            self._active = True
            return True
        return False

    def deactivate(self):
        """
        Sets the active-value to False.

        Returns:
            bool: True, if value was set correctly, False if value was already False.
        """
        if self._active:
            self._active = False
            return True
        return False

    def get_whitelist(self):
        """
        Getter for the whitelist of the category.

        Returns:
            List[Tuple[str, str]]: List containing all tags in the form of key,value pairs.
        """
        return self._whitelist

    def set_whitelist(self, new_whitelist):
        """
        Changes the old whitelist to a new one.

        Args:
            new_whitelist (list[str]): value for the new whitelist.

        Returns:
             bool: True, if the whitelist was overwritten successfully, else False.
        """
        if self._whitelist != new_whitelist:
            self._whitelist = new_whitelist
            return True
        return False

    def get_blacklist(self) -> List[str]:
        """
        Getter for the blacklist of the category.

        Returns
           List[Tuple[str, str]]: List containing all tags in the form of key,value pairs.
        """
        return self._blacklist

    def set_blacklist(self, new_blacklist):
        """
        Overwrites the old Blacklist with a new value.

        Args:
            new_blacklist (list[str]): new value for the blacklist.

        Returns:
            bool: True, if the blacklist was overwritten successfully, else False.
        """
        if self._blacklist != new_blacklist:
            self._blacklist = new_blacklist
            return True
        return False

    def get_category_name(self):
        """
        Getter for the category name.

        Returns:
             str: name of the category.
        """
        return self._category_name

    def set_category_name(self, new_category_name):
        """
        Overwrites the old category_name.

        Args:
            new_category_name (str): new value for the category_name.

        Returns:
            bool: True, if the overwriting process concluded successfully, else False.
        """
        if self._category_name != new_category_name:
            self._category_name = new_category_name
            return True
        return False

    def get_calculate_area(self):
        """
        This says if the area of the category should be calculated or not.

        Returns:
            bool:  true if it should get calculated, false if not.
        """
        pass

    def get_calculation_method_of_area(self):
        """
        Getter for the calculated area method.

        Returns:
             calculation_method_of_area_enum.CalculationMethodOfArea: The method with which we calculate the area.
        """
        return self._calculate_area

    def set_calculation_method_of_area(self, new_calculate_area):
        """
        Overwrites current calculate_area with the given value.

        Args:
            new_calculate_area (bool): new value that will overwrite the existing value.
        """
        self._calculate_area = new_calculate_area

    def get_calculate_floor_area(self):
        """
        This says if  the floor area should be calculated or not.

        Returns:
             bool: true if the floor are should be calculated, otherwise false.
        """
        return self._calculate_floor_area

    def set_calculate_floor_area(self, new_calculate_floor_area):
        """
        Overwrites the existing instance of calculate_floor_area.

        Args:
            new_calculate_floor_area (bool): new value for calculate_floor_are.

        Returns:
            bool: True, if the overwriting process was successful, else false.
        """
        if self._calculate_floor_area != new_calculate_floor_area:
            self._calculate_floor_area = new_calculate_floor_area
            return True
        return False

    def get_strictly_use_default_values(self):
        """
        This says if in the calculation we should strictly use the default values.

        Returns:
             bool: value of strictly_use_default_values.
        """
        return self._strictly_use_default_values

    def set_strictly_use_default_values(self, new_strictly_use_default_values):
        """
        Overwrites the already existing value of strictly_use_default_values.

        Args:
            new_strictly_use_default_values (bool): new value for strictly_use_default_values.

        Return:
            True if the overwriting process was successful, else False.
        """
        if self._strictly_use_default_values != new_strictly_use_default_values:
            self._strictly_use_default_values = new_strictly_use_default_values
            return True
        return False

    def get_attractivity_attributes(self):
        """
        Getter for the AttractivityAttributes of the category.

        Returns:
            list[attractivity_attribute.AttractivityAttribute]: List of all used attractivity attributes
        """
        return self._attractivity_attributes

    def add_attractivity_attribute(self, new_attractivity_attribute):
        """
        Adds a new attractivity attribute to the list.

        Args:
            new_attractivity_attribute (attractivity_attribute.AttractivityAttribute): new attractivityAttribute that will be added.

        Returns:
            bool: True, if the attribute was added successfully, else False.
        """
        if new_attractivity_attribute not in self._attractivity_attributes:
            self._attractivity_attributes.append(new_attractivity_attribute)
            return True
        return False

    def remove_attractivity_attribute(self, attractivity_attribute):
        """
        Removes an already existing attribute from the list.

        Args:
            attractivity_attribute (attractivity_attribute.AttractivityAttribute): attractivity attribute that will be removed from the list.

        Returns:
            True, if the element was removed, else False.
        """
        if attractivity_attribute in self._attractivity_attributes:
            self._attractivity_attributes.remove(attractivity_attribute)
            return True
        return False

    def get_default_value_list(self):
        """
        Getter for the default values of the category.

        Returns:
            list[DefaultValueEntry]: List of all used default values.
        """
        return self._default_value_list

    def add_default_value_entry(self, new_default_value_entry):
        """
        Adds a new value to the default_value_entry list.

        Args:
            new_default_value_entry (DefaultValueEntry): element to add.

        Returns:
            bool: True, if element was added successfully, else False
        """
        if new_default_value_entry not in self._default_value_list:
            self._default_value_list.append(new_default_value_entry)
            return True
        return False

    def remove_default_value_entry(self, default_value_entry):
        """
        Removes an already existing element from the default_value_entry list.

        Args:
            default_value_entry (default_value_entry.DefaultValueEntry): value that will be removed.

        Returns:
            bool: True, if the element was removed successfully, else False.
        """
        if default_value_entry in self._default_value_list:
            self._default_value_list.remove(default_value_entry)
            return True
        return False

    def move_default_value_entry_up(self, default_value_entry):
        """
        Moves an already existing default value from the list one element up.

        Args:
            default_value_entry (default_value_entry.DefaultValueEntry): element from the list, that will be incremented by one.

        Returns:
            bool: True, if the change was successful, else False.
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
        Moves an already existing default value from list one element down.

        Args:
            default_value_entry (default_value_entry.DefaultValueEntry): element from the list, that will be decremented by one.

        Returns:
            bool: True, if the change was successful, else false.
        """
        if (default_value_entry not in self._default_value_list) \
                or self._default_value_list.index(default_value_entry) <= 0:
            return False
        index = self._default_value_list.index(default_value_entry)
        self._default_value_list[index + 1], self._default_value_list[index] \
            = self._default_value_list[index], self._default_value_list[index + 1]
        return True
