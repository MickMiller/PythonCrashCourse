"""
File: my_car.py Purpose: Creates instance of class Car
"""

from car import Car


def test_my_car(self):
    """ Runs code to test class in file car.py """
    my_new_car = Car('Saab', '900', 1984)
    self.assertEqual(0, my_new_car.odometer_get())
    my_new_car.odometer_set(281790)
    self.assertEqual(281790, my_new_car.odometer_get())
    print("In test_my_car")
