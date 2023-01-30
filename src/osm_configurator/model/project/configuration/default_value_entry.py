from __future__ import annotations

from src.osm_configurator.model.project.configuration.attribute_enum import Attribute

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, List, Dict


class DefaultValueEntry:
    """
    DefaultValueEntry stores a default value for every attribute.
    Default values can be set and read.
    """

    def __init__(self):
        """
        Constructor of the class.
        Creates an empty DefaultValueEntry with 0 for all the factor values.
        """
        self._tag: str = ""
        self._default_value_per_attribute: Dict[Attribute, float] = {}

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

    def set_attribute_default(self, attribute: Attribute, value) -> bool:
        """
        Sets the default value of an attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value will be overwritten
            value (float): new default value

        Returns:
            bool: True, if overwriting process was successful, else false
        """
        self._default_value_per_attribute[attribute] = value
        return True

    def get_attribute_default(self, attribute: Attribute) -> float:
        """
        Gets the default value of a certain attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value is searched for

        Returns:
            float: The default value of the attribute
        """
        return self._default_value_per_attribute[attribute]
