""" A class that can be used to represent a car."""


import unittest


class Car(unittest.TestCase):
    """ A simple attempt to represent a car. """

    def __init__(self, manufacturer, model, year):  # call constructor for Car
        """ Initialize attributes to describe a car. """
        super().__init__()  # call constructor to init parent class
        self.manufacturer = manufacturer  # attribute made in this class
        self.model = model
        self.year = year
        self.odometer_reading = 0  # sets default value

    def class_get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def class_read_odometer(self):
        """ Print a statement showing the car's mileage. """
        # print("This car has " + str(self.odometer_reading) + " miles on it.")
        return "This car has " + str(self.odometer_reading) + " miles on it."

    def class_fill_gas_tank(self):
        """ See title. """
        # self.class_get_description prevents (no-self_use) error
        return "Gas tank filled. " + self.class_get_descriptive_name()

    def class_increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        return self.odometer_reading
