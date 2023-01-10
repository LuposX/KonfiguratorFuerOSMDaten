import pythoncode.src.osm_configurator.model.project.configuration.attractivity_attribute_enum


class AttractivityAttribute:
    """
    AttractivityAttribute models multiple Attractivity Attributes
    and their factors. Each factor is mapped to an according attractivity attribute
    and vice versa.
    """

    attractivity_attributes = []  # list of attractivity attributes (values from attractivity_attribute_enum)
    attribute_factor = {}  # dictionary, that maps each attractivity attribute to its according factor
    base_factor = 1  # base factor, if no factor is given for a certain attribute

    def __init__(self, attractivity_attributes, attribute_factor, base_factor):
        """
        Creates a new instance of "AttractivityAttribute"

        Args:
            attractivity_attributes: list of the enum-elements
            attribute_factor: list of the factors used for calculation
            base_factor: factor used for calculation if the given attribute has no factor
        """
        self.attractivity_attributes = attractivity_attributes
        self.attribute_factor = attribute_factor
        self.base_factor = base_factor

    def get_attractivity_attribute(self):
        """
        Returns:
            list: list of attractivity_attributes
        """
        return self.attractivity_attributes

    def set_attractivity_attribute(self, name):
        """
        Adds a new attractivity attribute with the given base factor to the list of attributes

        Args:
            name (str): name of the attribute that will be added

        Returns:
            bool: true, if adding was successful, else false
        """

        if name not in self.attractivity_attributes:
            self.attractivity_attributes.append(name)
            return True
        return False

    def get_attribute_factor(self, attribute):
        """
        Returns the factor of a given attribute

        Args:
            attribute (attractivity_attribute_enum): attribute whose factor will be searched for

        Returns:
             double: the given factor if the attribute exists, else -1
        """
        if attribute in self.attribute_factor and attribute in self.attractivity_attributes:
            return self.base_factor
        elif attribute in self.attribute_factor:
            return self.attribute_factor[attribute]
        return -1

    def set_attribute_factor(self, attribute, factor):
        """
        Changes the factor of the given attribute

        Args:
            attribute (attractivity_attribute_enum): is the attribute whose factor will be changed
            factor (double) : is the new factor

        Returns:
            bool: true, if changing was successful, else false
        """
        if attribute in self.attractivity_attributes and attribute in self.attribute_factor:
            self.attractivity_attributes[attribute] = factor
            return True
        elif attribute in self.attractivity_attributes:
            self.attractivity_attributes.update(attribute=factor)
            return True
        return False

    def get_base_factor(self):
        """
        Returns:
             double: the base factor
        """
        return self.base_factor

    def set_base_factor(self, new_base_factor):
        """
        Args:
            new_base_factor (double): new value for the already existing base factor

        Returns:
            void
        """
        self.base_factor = new_base_factor
