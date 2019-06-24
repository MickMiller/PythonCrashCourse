"""
File: car.py Purpose: Contains class Car
"""

import unittest


class Car(unittest.TestCase):
    """ A simple attempt to represent a car. """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        super().__init__()
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name_get(self):
        """ Return a neatly formatted descriptive name. """
        long_name = (str(self.year) + ' ' + str(self.make) + ' ' +
                     str(self.model))
        return long_name.title()

    def odometer_get(self):
        """ Print car's mileage """
        current_odometer = self.odometer_reading
        return current_odometer

    def odometer_set(self, mileage):
        """ Sets odometer - reject change if roll odometer back attempt """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            ret_val = self.odometer_get()
        else:
            ret_val = "You can't roll back an odometer!"

        return ret_val

    def odometer_add(self, mileage):
        """ Adds to odometer reading
          Reject change if attempt to roll odometer back
        """
        if mileage >= 0:
            self.odometer_reading = mileage
            ret_val = self.odometer_get()
        else:
            ret_val = "You can't roll back an odometer!"
        return ret_val

