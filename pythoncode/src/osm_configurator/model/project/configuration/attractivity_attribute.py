import attractivity_attribute_enum


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
        :param attractivity_attributes: list of the enum-elements
        :param attribute_factor: list of the factors used for calculation
        :param base_factor: factor used for calculation if the given attribute has no factor
        """
        self.attractivity_attributes = attractivity_attributes
        self.attribute_factor = attribute_factor
        self.base_factor = base_factor

    def get_attractivity_attribute(self):
        """
        :return: list of attractivity_attributes
        """
        return self.attractivity_attributes

    def set_attractivity_attribute(self, name):
        """
        Adds a new attractivity attribute with the given base factor to the list of attributes
        :param name: name of the attribute that will be added
        :return: true, if adding was successful, else false
        """

        if name not in self.attractivity_attributes:
            self.attractivity_attributes.append(name)
            return True
        return False

    def get_attribute_factor(self, attribute):
        """
        Returns the factor of a given attribute
        :param attribute: defines the attribute whose factor will be searched for
        :return: the given factor if the attribute exists, else -1
        """
        if attribute in self.attribute_factor and attribute in self.attractivity_attributes:
            return self.base_factor
        elif attribute in self.attribute_factor:
            return self.attribute_factor[attribute]
        return -1

    def set_attribute_factor(self, attribute, factor):
        """
        Changes the factor of the given attribute
        :param attribute: is the attribute whose factor will be changed
        :param factor: is the new factor
        :return: true, if changing was successful, else false
        """
        if attribute in self.attractivity_attributes and attribute in self.attribute_factor:
            # TODO update entry in dictionary
            return True
        if attribute in self.attractivity_attributes:
            # TODO add entry to dictionary
            return True
        return False

    def get_base_factor(self):
        """
        :return: the base factor
        """
        return self.base_factor

    def set_base_factor(self, new_base_factor):
        """
        :param new_base_factor: new value for the already existing base factor
        """
        self.base_factor = new_base_factor
        return
