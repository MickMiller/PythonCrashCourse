""" File: test_ch9.py Purpose: Try It Yourself tests """

import unittest
from collections import OrderedDict
from user import User
import random
from my_dict import ordered_dict
import ch9_tiy
from car import Car
from electric_car import ElectricCar
from restaurant import Restaurant


class TestCh9(unittest.TestCase):
    """ class TestCh9 """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_electric_car_09_09(self):
        """ See title """
        my_car = ElectricCar('Saab', '900', 1984)
        ret_val = ch9_tiy.electric_car(my_car)
        self.assertEqual("Saab, 900, 1984, 70", ret_val)
        self.assertEqual("Battery size: " + str(my_car.battery.battery_size) +
                         ", range: " + str(my_car.battery.battery_range),
                         ch9_tiy.describe_battery(my_car))
        self.assertEqual("This car doesn't need a gas tank!",
                         ch9_tiy.fill_gas_tank_09_09(my_car))

    def test_upgrade(self):
        """ Tests battery upgrade """
        my_car = ElectricCar('Saab', '900', 1984)
        test_val = my_car.battery.battery_size
        self.assertEqual(my_car.battery.battery_size, test_val)
        self.assertEqual(70, test_val)
        ret_val = ch9_tiy.battery_upgrade_09_09(my_car)
        self.assertEqual(my_car.battery.battery_size, ret_val)
        self.assertEqual(85, ret_val)

    def test_patron_served_09_04(self):
        """ Returns number of patron served """
        restaurant_1 = Restaurant("Rosies", "Breakfast", True)
        ret_val = ch9_tiy.patron_served_09_04(restaurant_1)
        self.assertEqual(restaurant_1.restaurant_patron_get(), ret_val)

    def test_patron_served_09_04_02(self):
        """ Returns number of patron served """
        restaurant_1 = Restaurant("Rosies", "Breakfast", True)
        restaurant_1.restaurant_patron_set(1)
        ret_val = ch9_tiy.patron_served_09_04(restaurant_1)
        self.assertEqual(restaurant_1.restaurant_patron_get(), ret_val)

    def test_describe_restaurant_09_01(self):
        """ Simple class creation and invocation without parameters """
        restaurant_1 = Restaurant("Rosies", "Breakfast", True)
        ret_val = ch9_tiy.restaurant_describe_09_01(restaurant_1)
        self.assertEqual("Rosies, Breakfast", ret_val)
        ret_val = ch9_tiy.restaurant_name_get_09_01(restaurant_1)
        self.assertEqual("Rosies", ret_val)
        ret_val = ch9_tiy.restaurant_open_09_01(restaurant_1)
        self.assertEqual(True, ret_val)

    def test_describe_restaurant_09_02(self):
        """ Simple class creation and invocation without parameters """
        restaurant_1 = Restaurant("Rosies", "Breakfast", True)
        ret_val = ch9_tiy.restaurant_describe_09_01(restaurant_1)
        self.assertEqual("Rosies, Breakfast", ret_val)
        restaurant_2 = Restaurant("5 guys", "Burgers", True)
        ret_val = ch9_tiy.restaurant_describe_09_01(restaurant_2)
        self.assertEqual("5 guys, Burgers", ret_val)
        restaurant_3 = Restaurant("Panara", "Healthy", True)
        ret_val = ch9_tiy.restaurant_describe_09_01(restaurant_3)
        self.assertEqual("Panara, Healthy", ret_val)

    def test_user(self):
        """ Create, describe and test User"""
        user_1 = User("Smokey", "Bear", "25", "True")
        ret_val = ch9_tiy.user_describe_09_03(user_1)
        self.assertEqual("Smokey Bear, 25 True", ret_val)
        ret_val = ch9_tiy.user_greet_09_03(user_1)
        self.assertEqual("Hi Smokey to Bruins fan you answered True", ret_val)
        user_2 = User("Winni", "Poo", "13", "True")
        ret_val = ch9_tiy.user_describe_09_03(user_2)
        self.assertEqual("Winni Poo, 13 True", ret_val)
        ret_val = ch9_tiy.user_greet_09_03(user_2)
        self.assertEqual("Hi Winni to Bruins fan you answered True", ret_val)

    def test_increment(self):
        """ See title """
        user_2 = User("John Q", "Public", 42, "False")

        ret_val = ch9_tiy.login_get_09_05(user_2)
        self.assertEqual(str(user_2.login_attempt), str(ret_val))

        ret_val = ch9_tiy.login_inc_09_05(user_2)
        self.assertEqual(str(user_2.login_attempt), str(ret_val))
        self.assertEqual(1, ret_val)
        ret_val = ch9_tiy.login_inc_09_05(user_2)
        self.assertEqual(str(user_2.login_attempt), str(ret_val))
        self.assertEqual(2, ret_val)

        ret_val = ch9_tiy.login_reset_09_05(user_2)
        self.assertEqual(str(user_2.login_attempt), str(ret_val))
        self.assertEqual(0, user_2.login_attempt)

    def test_flavor_ret(self):
        """ See title """
        restaurant = Restaurant("Rose", "Healthy", True)
        ret_val = ch9_tiy.flavor_ret_09_06(restaurant)
        self.assertEqual("Chocolate", ret_val)

    def test_privileges(self):
        """ See title """
        user_1 = User("John Q", "Public", "42", False)
        ret_val = ch9_tiy.privileges_09_08(user_1)
        self.assertEqual(['can add post', 'can delete post', 'can ban user'],
                         ret_val)

    def test_my_car(self):
        """ Runs code to test class in file car.py """
        my_new_car = Car('Saab', '900', 1984)
        self.assertEqual(0, my_new_car.odometer_get())
        my_new_car.odometer_set(281790)
        self.assertEqual(281790, my_new_car.odometer_get())

    def test_ordered_dict(self):
        """ Runs code from pg 185 """
        favorite_languages = OrderedDict()

        ret_val = ordered_dict(favorite_languages)

        self.assertEqual('python', favorite_languages['jen'])
        self.assertEqual('Python', ret_val)

    def test_python_random(self):
        """ Generates pseudo-random number """
        for value in range(1, 10):
            pseudo_random = random.randint(1, 6)
            value += 1
            print("Pseudo-random numbers 1-6 are: " + str(pseudo_random))
        for value in range(1, 10):
            pseudo_random = random.randint(1, 10)
            value += 1
            print("Pseudo-random numbers 1-10 are: " + str(pseudo_random))
        for value in range(1, 10):
            pseudo_random = random.randint(1, 20)
            value += 1
            print("Pseudo-random numbers 1-20 are: " + str(pseudo_random))

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
