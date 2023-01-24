from __future__ import annotations

import src.osm_configurator.model.project.configuration.attribute_enum


class DefaultValueEntry:
    """
    DefaultValueEntry stores a default value for every attribute.
    Default values can be set and read.
    """

    def __init__(self, tag, attribute_default_values):
        """Constructor of the class,
        creates an empty DefaultValueEntry with 0 for all the factor values.
        """
        pass

    def get_default_value_entry_tag(self):
        """
        Returns the tag associated with this default value entry
        Returns:
            str: The tag of this entry
        """
        pass

    def set_tag(self, new_tag):
        """
        Sets a new value for a given tag

        Args:
            new_tag (str): value for overwriting the current tag, must be a valid OSM-tag

        Returns:
            bool: true if the overwriting process was successful, else false
        """
        pass

    def set_attribute_default(self, attribute, value):
        """
        Sets the default value of an attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value will be overwritten
            value (float): new default value

        Returns:
            bool: true, if overwriting process was successful, else false
        """
        pass

    def get_attribute_default(self, attribute):
        """
        Gets the default value of a certain attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value is searched for

        Returns:
            float: The default value of the attribute
        """
        pass
