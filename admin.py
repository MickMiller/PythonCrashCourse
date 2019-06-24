""" File: admin with classes Admin and Privileges """

import unittest


class Admin(unittest.TestCase):
    """ Subclass of User """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self):
        """ Initialize Admin attributes """
        super().__init__()
        self.privileges = Privileges()


class Privileges(unittest.TestCase):
    """ Subclass of Admin which is subclass of User """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self):
        """ Initialize Privileges """
        super().__init__()
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def privileges_show(self):
        """ See title """
        ret_val = self.privileges
        return ret_val
