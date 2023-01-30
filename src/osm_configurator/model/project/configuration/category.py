from __future__ import annotations

import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum
import src.osm_configurator.model.project.configuration.attractivity_attribute
import src.osm_configurator.model.project.configuration.default_value_entry
import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum as calculation_method_of_area_enum_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from typing import Dict
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea


class Category:
    """
    Represents a category. A category is a collection of configurations for the calculation process. A category defines
    which OSM-elements are contained by it with a white- and a blacklist. All configurations of the category do only
    affect does OSM-elements.
    """

    def __init__(self):
        """
        Creates a new instance of a "Category" class.
        """
        self._active: bool = False
        self._whitelist = []
        self._blacklist = []
        self._category_name = "Category Name"
        self._calculation_method_of_area = calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_SITE_AREA
        self._attractivity_attributes = []
        self._default_value_list = []
        self._length = 3

        self._strictly_use_default_values: bool = False

        # Create the Attribute dictionary
        self._attributes: Dict = {}
        all_enums_names = [member.name for member in attribute_enum_i.Attribute]
        for enum_name in all_enums_names:
            self._attributes.update({enum_name: False})

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
        if new_category_name:
            self._category_name = new_category_name
            return True
        return False

    def get_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all used attributes, of the categories.
        This is used to know which tags we need to save.

        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        _activated = []

        for enum_name in self._attributes:
            if self._attributes.get(enum_name) == True:
                _activated.append(enum_name)

        return _activated

    def get_not_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all attributes, that are not activated.

        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        _activated = []

        for enum_name in self._attributes:
            if self._attributes.get(enum_name) == False:
                _activated.append(enum_name)

        return _activated

    def get_attribute(self, attribute) -> bool:
        """
        Returns if a given attribute is activated or not.

        Args:
            attribute (Attribute): The attribute which is inspected.

        Returns:
            bool: True when the attribute is active, otherwise false.
        """
        if self._attributes.get(attribute.name):
            return True
        else:
            return False

    def set_attribute(self, attribute, boolean):
        """
        Activates and deactivates a given attribute .

        Args:
            attribute (Attribute): The attribute which should be activated or deactivated.
            boolean (bool): The new value.

        Returns:
            bool: True when it works, otherwise false.
        """
        self._attributes[attribute.name] = boolean
        return True

    def get_calculation_method_of_area(self):
        """
        Getter for the calculated area method.

        Returns:
             calculation_method_of_area_enum.CalculationMethodOfArea: The method with which we calculate the area.
        """
        return self._calculation_method_of_area

    def set_calculation_method_of_area(self, new_calculation_method_of_area):
        """
        Overwrites current calculate_area with the given value.

        Args:
            new_calculation_method_of_area (bool): new value that will overwrite the existing value.
        """
        self._calculation_method_of_area = new_calculation_method_of_area

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
            new_attractivity_attribute (attractivity_attribute.AttractivityAttribute): new attractivityAttribute that
            will be added.

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
            attractivity_attribute (attractivity_attribute.AttractivityAttribute): attractivity attribute that will be
            removed from the list.

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
            default_value_entry (default_value_entry.DefaultValueEntry): element from the list, that will be
            incremented by one.

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
            default_value_entry (default_value_entry.DefaultValueEntry): element from the list, that will be
            decremented by one.

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

    def get_strictly_use_default_values(self) -> bool:
        return self._strictly_use_default_values
