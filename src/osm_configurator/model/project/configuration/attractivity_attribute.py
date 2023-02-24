from __future__ import annotations

import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum
from typing import TYPE_CHECKING, Final

from src.osm_configurator.model.parser.custom_exceptions.not_valid_name_Exception import NotValidName

if TYPE_CHECKING:
    from typing import Dict
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute

DEFAULT_VALUE: float = 0.0  # The default value of every attribute set at the beginning.


class AttractivityAttribute:
    """
    AttractivityAttribute models a single Attractivity Attributes to its factors.
    Each AttractivityAttribute consists of the following elements:
    - A name, which describes the AttractivityAttribute
    - A dictionary of factors with attribute-keys pairs, which describe the attractivity attribute
    - A base factor
    """

    def __init__(self, attractivity_attribute_name: str):
        """
        Creates a new instance of a "AttractivityAttribute" class.
        Args:
            attractivity_attribute_name (str): The name of the Attractivity Attributes
        """
        if not attractivity_attribute_name.isascii():
            raise NotValidName("A Name is not allowed to have a umlaut or special characters.")

        self._attractivity_attribute_name: str = attractivity_attribute_name
        self._base_attractivity: float = DEFAULT_VALUE
        self._attribute_factors: Dict[Attribute, float] = {}

        for attribute in attribute_enum.Attribute:
            self._attribute_factors[attribute] = DEFAULT_VALUE

    def get_attractivity_attribute_name(self) -> str:
        """
        Getter for attractivity attribute name.
        Returns:
            str: The attractivity attribute name.
        """
        return self._attractivity_attribute_name

    def set_attractivity_attribute_name(self, new_name: str) -> bool:
        """
        Setter for the attractivity attribute name.
        Args:
            new_name (str): name of the attractivity attribute.

        Returns:
            bool: True, on success
        """
        if new_name != "":
            self._attractivity_attribute_name = new_name
            return True
        return False

    def get_attribute_factor(self, attribute: Attribute) -> float:
        """
        Getter for the list of attributes and factors.
        Args:
            attribute: The attribute we want to read the factor from
        Returns:
            float: The value of the factor to the given attribute
        """
        return self._attribute_factors[attribute]

    def set_attribute_factor(self, attribute: Attribute, factor: float):
        """
         Setter for the list of attributes and factors.
        Args:
            attribute: The attribute we for which we want to set the factor.
            factor: The factor we want to set
        """
        self._attribute_factors[attribute] = factor

    def get_base_factor(self) -> float:
        """
        Getter for the base factor.
        Returns:
             float: the base factor
        """
        return self._base_attractivity

    def set_base_factor(self, new_base_factor):
        """
        Setter for the base factor.
        Args:
            new_base_factor (float): New value for the base factor
        """
        self._base_attractivity = new_base_factor
