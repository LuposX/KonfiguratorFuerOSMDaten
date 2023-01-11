import src.osm_configurator.model.project.configuration.attribute_enum


class AttractivityAttribute:
    """
    AttractivityAttribute models a single Attractivity Attributes to its factors.
    Each AttractivityAttribute consists of the following elements:
    - A name, which describes the AttractivityAttribute
    - A List of attributes factor pairs, which describe the attractivity attribute
    - A base factor
    """

    def __init__(self, attractivity_attribute_name, attractivity_attribute_list, base_attractivity):
        """
        Creates a new instance of a "AttractivityAttribute" class.

        Args:
            attractivity_attribute_name (str): The name of the Attractivity Attributes
            attractivity_attribute_list (List[(attribute_enum.Attribute, float)]): A list of attributes each having its own factor.
            base_attractivity (float): The base attractivity value.

        Examples:
            An example for attractivity_attribute_list: [(AREA, 1.0), (NUMER_OF_FLOOR, 2.0), (GROUND_AREA, 6.9)]
        """
        pass

    def get_attractivity_attribute_name(self):
        """
        Getter for attractivity attribute name.

        Returns:
            str: The attractivity attribute name.
        """
        pass

    def set_attractivity_attribute_name(self, name):
        """
        Setter for the attractivity attribute name.

        Args:
            name (str): name of the attractivity attribute.

        Returns:
            bool: true, if the name was successfully set, false otherwise
        """
        pass

    def get_attractivity_attribute_list(self):
        """
        Getter for the list of attributes and factors.

        Returns:
            List[(attribute_enum.Attribute, float)]: The list of attribute factor pairs.
        """
        pass

    def set_attractivity_attribute_list(self, attractivity_attribute_list):
        """
         Setter for the list of attributes and factors.

        Args:
            attractivity_attribute_list (List[(attribute_enum.Attribute, float)]): A list of attribute factor pairs we want to set as the new list of attributes and factors.
        """
        pass

    def get_base_factor(self):
        """
        Getter for the base factor.

        Returns:
             float: the base factor
        """
        pass

    def set_base_factor(self, new_base_factor):
        """
        Setter for the base factor.

        Args:
            new_base_factor (float): New value for the base factor

        Returns:
            bool: true if the base factor eas successful set, false else
        """
        pass
