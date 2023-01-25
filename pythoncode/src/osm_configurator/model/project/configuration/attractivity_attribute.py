from __future__ import annotations

import src.osm_configurator.model.project.configuration.attribute_enum


class AttractivityAttribute:
    """
    AttractivityAttribute models a single Attractivity Attributes to its factors.
    Each AttractivityAttribute consists of the following elements:
    - A name, which describes the AttractivityAttribute
    - A List of attributes factor pairs, which describe the attractivity attribute
    - A base factor
    """

    _attractivity_attribute_name = ""
    attractivity_attribute_list = []
    base_attractivity = 0

    def __init__(self, attractivity_attribute_name, attractivity_attribute_list, base_attractivity):
        """
        Creates a new instance of a "AttractivityAttribute" class.

        Args:
            attractivity_attribute_name (str): The name of the Attractivity Attributes
            attractivity_attribute_list (List[(attribute_enum.Attribute, float)]): A list of attributes each having its
            own factor.
            base_attractivity (float): The base attractivity value.

        Examples:
            An example for attractivity_attribute_list: [(AREA, 1.0), (NUMER_OF_FLOOR, 2.0), (GROUND_AREA, 6.9)]
        """
        self._attractivity_attribute_name = attractivity_attribute_name
        self.attractivity_attribute_list = attractivity_attribute_list
        self.base_attractivity = base_attractivity

    def get_attractivity_attribute_name(self):
        """
        Getter for attractivity attribute name.

        Returns:
            str: The attractivity attribute name.
        """
        return self._attractivity_attribute_name

    def set_attractivity_attribute_name(self, new_name):
        """
        Setter for the attractivity attribute name.

        Args:
            new_name (str): name of the attractivity attribute.

        Returns:
            bool: true, if the name was successfully set, false otherwise
        """
        self._attractivity_attribute_name = new_name
        return True

    def get_attractivity_attribute_list(self):
        """
        Getter for the list of attributes and factors.

        Returns:
            list[(attribute_enum.Attribute, float)]: The list of attribute factor pairs.
        """
        return self.attractivity_attribute_list

    def set_attractivity_attribute_list(self, new_attractivity_attribute_list):
        """
         Setter for the list of attributes and factors.

        Args:
            new_attractivity_attribute_list (list[(attribute_enum.Attribute, float)]): A list of attribute factor pairs
            we want to set as the new list of attributes and factors.
        """
        self._attractivity_attribute_name = new_attractivity_attribute_list
        return True

    def get_base_factor(self):
        """
        Getter for the base factor.

        Returns:
             float: the base factor
        """
        return self.base_attractivity

    def set_base_factor(self, new_base_factor):
        """
        Setter for the base factor.

        Args:
            new_base_factor (float): New value for the base factor

        Returns:
            bool: true if the base factor eas successful set, false else
        """
        self.base_attractivity = new_base_factor
        return True
