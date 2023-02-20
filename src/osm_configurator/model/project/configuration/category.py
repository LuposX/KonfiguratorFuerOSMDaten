from __future__ import annotations

import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum
import src.osm_configurator.model.project.configuration.attractivity_attribute
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i
import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum as calculation_method_of_area_enum_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i

import src.osm_configurator.model.model_constants as model_constants_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Dict
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute


class Category:
    """
    Represents a category. A category is a collection of configurations for the calculation process. A category defines
    which OSM-elements are contained by it with a white- and a blacklist. All configurations of the category do only
    affect does OSM-elements.
    """

    def __init__(self, category_name: str):
        """
        Creates a new instance of a "Category" class.
        Args:
            category_name (str): The name of the newly created category.
        """
        self._active: bool = True
        self._whitelist: List[str] = []
        self._blacklist: List[str] = []
        self._category_name: str = category_name
        self._calculation_method_of_area: CalculationMethodOfArea = calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_BUILDING_AREA
        self._attractivity_attributes: List[AttractivityAttribute] = []
        self._default_value_list: List[DefaultValueEntry] = []
        self._strictly_use_default_values: bool = False

        # Adds DEFAULT-Tag to the tag-list
        self._default_tag: DefaultValueEntry = default_value_entry_i.DefaultValueEntry(model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG)
        self._default_value_list.append(self._default_tag)

        self._strictly_use_default_values: bool = False

        # Create the Attribute dictionary
        self._attributes: Dict[Attribute, bool] = {}
        for attribute in attribute_enum_i.Attribute:
            self._attributes.update({attribute: False})

    def is_active(self) -> bool:
        """
        Checks if value "active" is set.
        Returns:
            bool: True if active, false if inactive.
        """
        return self._active

    def activate(self) -> bool:
        """
        Sets the active-value to True.
        """
        self._active = True
        return True

    def deactivate(self) -> bool:
        """
        Sets the active-value to False.
        """
        self._active = False
        return True

    def get_whitelist(self) -> List[str]:
        """
        Getter for the whitelist of the category.
        Returns:
            list[str]: List containing all tags in the form of key,value pairs.
        """
        return self._whitelist

    def set_whitelist(self, new_whitelist: List[str]) -> bool:
        """
        Changes the old whitelist to a new one.
        Args:
            new_whitelist (List[str]): value for the new whitelist.
        """
        self._whitelist = new_whitelist

    def get_blacklist(self) -> List[str]:
        """
        Getter for the blacklist of the category.
        Returns
           List[str]: List containing all tags in the form of key,value pairs.
        """
        return self._blacklist

    def set_blacklist(self, new_blacklist: List[str]) -> bool:
        """
        Overwrites the old Blacklist with a new value.
        Args:
            new_blacklist (List[str]): new value for the blacklist.
        """
        self._blacklist = new_blacklist

    def get_category_name(self) -> str:
        """
        Getter for the category name.
        Returns:
             str: name of the category.
        """
        return self._category_name

    def set_category_name(self, new_category_name: str) -> bool:
        """
        Overwrites the old category_name.
        Args:
            new_category_name (str): new value for the category_name.
        """
        self._category_name = new_category_name
        return True

    def get_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all used attributes, of the categories.
        This is used to know which tags we need to save.
        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        activated: List[Attribute] = []
        for enum in self._attributes:
            if self._attributes.get(enum):
                activated.append(enum)
        return activated

    def get_not_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all attributes, that are not activated.
        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        not_activated: List[Attribute] = []
        for enum in self._attributes:
            if not self._attributes.get(enum):
                not_activated.append(enum)
        return not_activated

    def get_attribute(self, attribute: Attribute) -> bool:
        """
        Returns if a given attribute is activated or not.
        Args:
            attribute (Attribute): The attribute which is inspected.
        Returns:
            bool: True when the attribute is active, otherwise false.
        """
        return self._attributes.get(attribute)

    def set_attribute(self, attribute: Attribute, boolean: bool) -> bool:
        """
        Activates and deactivates a given attribute .
        Args:
            attribute (Attribute): The attribute which should be activated or deactivated.
            boolean (bool): The new value.
        Returns:
            bool: True when it works, otherwise false.
        """
        if attribute in attribute_enum_i.Attribute:
            self._attributes[attribute] = boolean
            return True
        else:
            return False

    def get_strictly_use_default_values(self) -> bool:
        """
        Getter for _strictly_use_default_values.
        Returns:
            bool: True when the default values should be used strictly.
        """
        return self._strictly_use_default_values

    def set_strictly_use_default_values(self, boolean: bool):
        """
        Setter for _strictly_use_default_values.
        Args:
            boolean (bool): The new value _strictly_use_default_values should be set to.
        """
        self._strictly_use_default_values = boolean

    def get_calculation_method_of_area(self) -> CalculationMethodOfArea:
        """
        Getter for the calculated area method.
        Returns:
             calculation_method_of_area_enum.CalculationMethodOfArea: The method with which we calculate the area.
        """
        return self._calculation_method_of_area

    def set_calculation_method_of_area(self, new_calculation_method_of_area: CalculationMethodOfArea) -> bool:
        """
        Overwrites current calculate_area with the given value.
        Args:
            new_calculation_method_of_area (bool): new value that will overwrite the existing value.
        """
        self._calculation_method_of_area = new_calculation_method_of_area
        return True

    def get_attractivity_attributes(self) -> List[AttractivityAttribute]:
        """
        Getter for the AttractivityAttributes of the category.
        Returns:
            List[attractivity_attribute.AttractivityAttribute]: List of all used attractivity attributes
        """
        return self._attractivity_attributes

    def add_attractivity_attribute(self, new_attractivity_attribute: AttractivityAttribute) -> bool:
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

    def remove_attractivity_attribute(self, attractivity_attribute: AttractivityAttribute) -> bool:
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

    def get_default_value_list(self) -> list[DefaultValueEntry]:
        """
        Getter for the default values of the category.
        Returns:
            list[DefaultValueEntry]: List of all used default values.
        """
        return self._default_value_list

    def add_default_value_entry(self, new_default_value_entry: DefaultValueEntry) -> bool:
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

    def remove_default_value_entry(self, default_value_entry: DefaultValueEntry) -> bool:
        """
        Removes an already existing element from the default_value_entry list.
        Args:
            default_value_entry (default_value_entry.DefaultValueEntry): value that will be removed.
        Returns:
            bool: True, if the element was removed successfully, else False.
        """
        if default_value_entry in self._default_value_list:
            if default_value_entry == model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG:
                return False
            self._default_value_list.remove(default_value_entry)
            return True
        return False

    def move_default_value_entry_up(self, moved_default_value_entry: DefaultValueEntry) -> bool:
        """
        Moves an already existing default value from the list one element up.
        Args:
            moved_default_value_entry (default_value_entry.DefaultValueEntry): element from the list, that will be
            incremented by one.
        Returns:
            bool: True, if the change was successful, else False.
        """
        if moved_default_value_entry not in self._default_value_list:
            return False
        # To make sure that "default" is always at the bottom, you cant move the last item up
        if self._default_value_list.index(moved_default_value_entry) <= 0:
            return False
        index = self._default_value_list.index(moved_default_value_entry)
        self._default_value_list[index - 1], self._default_value_list[index] \
            = self._default_value_list[index], self._default_value_list[index - 1]
        return True

    def move_default_value_entry_down(self, moved_default_value_entry: DefaultValueEntry) -> bool:
        """
        Moves an already existing default value from list one element down.
        Args:
            moved_default_value_entry (default_value_entry.DefaultValueEntry): element from the list, that will be
            decremented by one.
        Returns:
            bool: True, if the change was successful, else false.
        """
        if moved_default_value_entry not in self._default_value_list:
            return False
        # To make sure that "default" is always at the bottom, you cant move the second last item down
        if self._default_value_list.index(moved_default_value_entry) <= 1:
            return False
        index = self._default_value_list.index(moved_default_value_entry)
        self._default_value_list[index + 1], self._default_value_list[index] \
            = self._default_value_list[index], self._default_value_list[index + 1]
        return True
