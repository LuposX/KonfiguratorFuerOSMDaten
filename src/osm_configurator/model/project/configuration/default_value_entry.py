from __future__ import annotations

from src.osm_configurator.model.project.configuration.attribute_enum import Attribute


class DefaultValueEntry:
    """
    DefaultValueEntry stores a default value for every attribute.
    Default values can be set and read.
    """

    def __init__(self, tag):
        """
        Constructor of the class.
        Creates an empty DefaultValueEntry with 0 for all the factor values.
        """
        self._tag = tag
        self._length = 3
        self._attribute_default_values = [[] for x in range(self._length)]
        self._attribute_default_values[0] = [Attribute.PROPERTY_AREA, 0]
        self._attribute_default_values[0] = [Attribute.NUMER_OF_FLOOR, 0]
        self._attribute_default_values[0] = [Attribute.FIRST_FLOOR_AREA, 0]

    def get_default_value_entry_tag(self):
        """
        Returns the tag associated with this default value entry
        Returns:
            str: The tag of this entry
        """
        return self._tag

    def set_tag(self, new_tag):
        """
        Sets a new value for a given tag

        Args:
            new_tag (str): value for overwriting the current tag, must be a valid OSM-tag

        Returns:
            bool: true if the overwriting process was successful, else false
        """
        self._tag = new_tag
        return True

    def set_attribute_default(self, attribute, value):
        """
        Sets the default value of an attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value will be overwritten
            value (float): new default value

        Returns:
            bool: True, if overwriting process was successful, else false
        """
        for item in range(self._length):
            if self._attribute_default_values[item][0] == attribute:
                self._attribute_default_values[item][1] = [item, value]
                return True
        return False

    def get_attribute_default(self, attribute):
        """
        Gets the default value of a certain attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value is searched for

        Returns:
            float: The default value of the attribute
        """
        for item in range(self._length):
            if self._attribute_default_values[item][0] == attribute:
                return self._attribute_default_values[item][1]
