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
            attractivity_attribute_list (List[(attribute_enum.Attribute, int)]): A list of attributes each having its own factor.
            base_attractivity (int) The base attractivity value.

        Examples:
            An example for attractivity_attribute_list: [(AREA, 1), (NUMER_OF_FLOOR, 2), (GROUND_AREA, 3)]
        """
        pass

    def get_attractivity_attribute_name(self):
        """
        Getter for attractivity attribute name.

        Returns:
            attribute_enum.Attribute: The attractivity attribute name.
        """
        pass

    def set_attractivity_attribute_name(self, name):
        """
        Setter for the attractivity attribute name.

        Args:
            name (str): name of the attractivity attribute.
        """
        pass

    def get_attractivity_attribute_list(self):
        """
        Getter for the attractivity attribute name.

        Returns:
            List[(attribute_enum.Attribute, int)]: The list of attractivity attribute factor pairs.
        """
        pass

    def set_attractivity_attribute_list(self, attractivity_attribute_list):
        """
         Setter for the attractivity attribute name.

        Args:
            attractivity_attribute_list (List[(attribute_enum.Attribute, int)]): A list of ttractivity attribute factor pairs we want to set as the new attractivity attribute list.
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
            new_base_factor (float): new value for the already existing base factor
        """
        pass
