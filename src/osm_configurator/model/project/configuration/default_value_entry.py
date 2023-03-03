from __future__ import annotations

import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute

DEFAULT_VALUE: float = 0.0  # The default value of every attribute set at the beginning.


class DefaultValueEntry:
    """
    DefaultValueEntry stores a default value for every attribute.
    Default values can be set and read.
    """
    def __init__(self, tag: str):
        """
        Constructor of the class.
        Creates an empty DefaultValueEntry with 0 for all the factor values.

        Args:
            tag (str): The initial Tag for this entry
        """
        self._tag: str = tag
        self._all_attribute_default_values: Dict[Attribute, float] = {}
        for attribute in attribute_enum_i.Attribute:
            self._all_attribute_default_values.update({attribute: DEFAULT_VALUE})

    def get_default_value_entry_tag(self) -> str:
        """
        Returns the tag associated with this default value entry
        Returns:
            str: The tag of this entry
        """
        return self._tag

    def set_tag(self, new_tag: str) -> bool:
        """
        Sets a new value for a given tag

        Args:
            new_tag (str): value for overwriting the current tag, must be a valid OSM-tag
        """
        if new_tag != "":
            self._tag = new_tag
            return True
        else:
            return False

    def set_attribute_default(self, attribute: Attribute, value: float) -> bool:
        """
        Sets the default value of an attribute.

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value will be overwritten
            value (float): new default value

        Returns:
            bool: True, if overwriting process was successful, else false
        """
        if attribute in attribute_enum_i.Attribute:
            self._all_attribute_default_values[attribute] = value
            return True
        return False

    def get_attribute_default(self, attribute: Attribute) -> float:
        """
        Gets the default value of a certain attribute

        Args:
            attribute (attribute_enum.Attribute): Attribute whose value is searched for

        Returns:
            float: The default value of the attribute
        """
        if attribute in attribute_enum_i.Attribute:
            return self._all_attribute_default_values[attribute]
