""" File: user.py with class User """

import unittest
from admin import Admin


class User(unittest.TestCase):
    """" A Class User example. """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, first_name, last_name, age, bruins_fan):
        """ Initialize name and age attributes """
        super().__init__()
        self.user_first_name = first_name
        self.user_last_name = last_name
        self.user_age = age
        self.user_bruins_fan = bruins_fan
        self.login_attempt = 0
        self.admin = Admin()

    def login__reset(self):
        """ See title """
        self.login_attempt = 0
        return self.login_attempt

    def login__increment(self):
        """ See title """
        self.login_attempt = self.login_attempt + 1
        return self.login_attempt

    def user_describe(self):
        """ Prints User info """
        return(self.user_first_name + " " + self.user_last_name + ", " +
               self.user_age + " " + self.user_bruins_fan)

    def user_greet(self):
        """ Prints greeting """
        return("Hi " + self.user_first_name +
               " to Bruins fan you answered " +
               self.user_bruins_fan)
