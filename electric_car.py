""" File: electric_car.py """

import unittest
# from car import Car

class ElectricCar(unittest.TestCase):
    """ Represent aspects of a car, specific to electric vehicles """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class
            Then initialize attributes specific to an electric car
        """
        super().__init__()
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()


class Battery(unittest.TestCase):
    """ A simple attempt to model a battery for an electric car"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, battery_size=70, battery_range=240):
        """ Initialize battery's attributes """
        super().__init__()
        self.battery_size = battery_size
        self.battery_range = battery_range
        self.fill_gas_tank_msg = "This car doesn't need a gas tank!"

    def battery_upgrade(self):
        """ See title """
        print("In battery_upgrade - ")
        if self.battery_size < 85:
            self.battery_size = 85
        return self.battery_size

    def fill_gas_tank(self):
        """ Electric cars don't have gas tanks """
        ret_val = self.fill_gas_tank_msg
        return ret_val
