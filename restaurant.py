""" File: restaurant.py aka class Restaurant """

import unittest


class Restaurant(unittest.TestCase):
    """" A restaurant example. """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, name, cuisine, rest_open=False, rest_patron=0):
        """ Initialize name and age attributes """
        super().__init__()
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.rest_open = rest_open
        self.patron = rest_patron
        self.ice_cream_stand = IceCreamStand()

    def restaurant_describe(self):
        """ Prints restaurant info """
        return self.cuisine_type

    def restaurant_name_get(self):
        """ Prints restaurant info """
        return self.restaurant_name

    def restaurant_open(self):
        """ Prints msg that restaurant is open. """
        return self.rest_open

    def restaurant_patron_get(self):
        """ Returns number of restaurant patron """
        return self.patron

    def restaurant_patron_set(self, patron_num):
        """ Sets number of restaurant patron """
        self.patron = patron_num
        return self.patron


class IceCreamStand(unittest.TestCase):
    """" Inherits from Restaurant """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, flavor="Chocolate"):
        """ Initialize """
        super().__init__()
        self.flavor = flavor

    def flavor_list(self):
        """ Prints all flavors """
        return self.flavor
