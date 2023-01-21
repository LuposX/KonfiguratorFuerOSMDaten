import osmium as osm


class LessDataOSMHandler(osm.SimpleHandler):
    """
    This class is responsible for parsing osm data files into a dataframe format.
    """
    def __init__(self, category_whitelist, Attribute: ):
        osm.SimpleHandler.__init__(self)

        # This will be the list in which we save the output
        self.osm_data = []

        # this is a temporary list that is used to save the tags for one osm element
        self.tmp_tag_list = []

        self.category_whitelist = category_whitelist

    def tag_inventory(self, elem, elem_type, categories_of_osm_element):
        self.tmp_tag_list = []
        for tag in elem.tags:
            self.tmp_tag_list.append((tag.k, tag.v))

        if (elem_type == "node"):
            self.osm_data.append([elem_type,
                                  len(self.tmp_tag_list),
                                  np.asarray(self.tmp_tag_list, dtype=str),
                                  np.asarray(categories_of_osm_element, dtype=np.uint16)])
        elif (elem_type == "way"):
            self.osm_data.append([elem_type,
                                  len(self.tmp_tag_list),
                                  np.asarray(self.tmp_tag_list, dtype=str),
                                  np.asarray(categories_of_osm_element, dtype=np.uint16)])
        else:
            self.osm_data.append([elem_type,
                                  len(self.tmp_tag_list),
                                  np.asarray(self.tmp_tag_list, dtype=str),
                                  np.asarray(categories_of_osm_element, dtype=np.uint16)])

    def node(self, n):
        categories_of_osm_element = []

        # check if the osm_element applies to a category
        for category in self.category_whitelist:
            name = category[0]
            whitelist = category[1]

            if n.tags.get(whitelist[0]) == whitelist[1]:
                categories_of_osm_element.append(name)

        if categories_of_osm_element:
            self.tag_inventory(n, "node", categories_of_osm_element)

        del n

    def way(self, w):
        categories_of_osm_element = []

        # check if the osm_element applies to a category
        for category in self.category_whitelist:
            name = category[0]
            whitelist = category[1]

            if w.tags.get(whitelist[0]) == whitelist[1]:
                categories_of_osm_element.append(name)

        if categories_of_osm_element:
            self.tag_inventory(w, "way", categories_of_osm_element)

    # its really hard to get the location out of relations
    def relation(self, r):
        categories_of_osm_element = []

        # check if the osm_element applies to a category
        for category in self.category_whitelist:
            name = category[0]
            whitelist = category[1]

            if r.tags.get(whitelist[0]) == whitelist[1]:
                categories_of_osm_element.append(name)

        if categories_of_osm_element:
            self.tag_inventory(r, "relation", categories_of_osm_element)
