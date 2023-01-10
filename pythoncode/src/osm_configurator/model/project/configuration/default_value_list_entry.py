import pythoncode.src.osm_configurator.model.project.configuration.attractivity_attribute_enum


class DefaultValueListEntry:
    """
    DefaultValueListEntry holds a dictionary and a tag of the Default Values
    A given Attribute (from the enum) holds a certain default attribute value

    Default Values can be set and read
    """

    tag = "Tag"  # Tag of the list
    attributeDefaultValue = {}  # Dictionary, where each attribute gets mapped to a certain factor

    def get_default_value_entry_tag(self):
        """
        Gives the Tag of the class
        Returns:
            st: tag
        """
        return self.tag

    def set_tag(self, new_tag):
        """
        Sets a new Value for the Tag

        Args:
            new_tag (str): value for overwriting the current tag

        Returns:
            bool: true if the overwriting process was successful, else false
        """
        if self.tag != new_tag:
            self.tag = new_tag
            return True
        return False

    def set_attribute_default(self, attribute, value):
        """
        Sets the attribute for a certain attribute, overwrites if necessary

        Args:
            attribute (attractivity_attribute_enum): Attribute whose value will be overwritten
            value (double): new value

        Returns:
            bool: true, if overwriting process was successful, else false
        """
        if attribute in self.attributeDefaultValue:
            self.attributeDefaultValue[attribute] = value
            return True
        # TODO: Adding new Entries if entry does not exist yet?
        return False

    def get_attribute_default(self, attribute):
        """
        Get Default Value of a certain Attribute

        Args:
            attribute (attractivity_attribute_enum): Attribute whose value is searched for

        Returns:
            double: The value of the attribute, if the attribute exists, else -1
        """
        if attribute in self.attributeDefaultValue:
            return self.attributeDefaultValue[attribute]
        return -1
