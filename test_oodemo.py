""" File: test_oodemo.py
Author: Gerard (Mick) Miller
Purpose: Working code showing often used snippits, eg do <something> for list.
    my_stooges3 = ("Moe", "Larry, "Curley")
    for stooge in stooges3:
        print("Stoog is: ", stooge)Bash
    To print documentation, from window running Bash:
        python -m pydoc test_oodemo | more # TBD issue:
            lots of doc on methods Python brings in,
                eg Methods inherited from unittest.case.TestCase - __call__
                eg python -m pydoc -k test_ |wc - generates 756 lines
            pdoc test_oodemo AND pdoc oodeo_class_elec gave concise results
"""


import unittest
import ast
from oodemo_class_car import Car
from oodemo_class_elec import ElectricCar


class TestOoDemo(unittest.TestCase):
    """ class TestOoDemo
    - unittest.TestCase.
      o https://docs.python.org/2/library/unittest.html
      o Python unit testing framework, sometimes referred to as “PyUnit"
      o unittest supports test automation, sharing of setup and shutdown code
        for tests, aggregation of tests into collections, and independence of
        the tests from the reporting framework. The unittest module provides
        classes that make it easy to support these qualities for a set of tests
    """

    # setUp and tearDown form a test fixture.
    # Many test cases can use same fixture.
    # setUp is method in class unittest.TestCaseRun
    # It's run first, can create objects for other methonds
    def setUp(self):
        """ Called first when instanciating Car. """
        self.stooges3 = ["Moe", "Larry", "Curly"]
        inf = open('oer.py', 'r')  # oer Oodemo Expected Results
        oer = ast.literal_eval(inf.read())
        inf.close()
        self.my_beetle = Car(oer['oer_0'], oer['oer_1'], oer['oer_2'])

    def tearDown(self):  # Run last and cleans up, eg
        pass

    def test_car_descriptive_name(self):
        """ See title AND object created in setUp. """
        msg = self.my_beetle.class_get_descriptive_name()
        self.assertEqual('2015 Volkswagen Beetle', msg)

    def test_car_read_odometer(self):
        """ See title AND object created in setUp. """
        msg = self.my_beetle.class_get_descriptive_name()
        self.assertEqual('2015 Volkswagen Beetle', msg)

    def test_car_increment_odometer(self):
        """ See title. """
        my_saab = Car('Saab', '900', 1984)
        my_saab.class_increment_odometer(281236)
        self.assertEqual(my_saab.class_read_odometer(),
                         "This car has 281236 miles on it.")

    def test_car_elec(self):
        """ Electric car instanciated. """
        my_tesla = ElectricCar('tesla', 'Roadster', 2015)
        msg = my_tesla.class_get_descriptive_name()
        self.assertEqual('2015 Tesla Roadster', msg)
        self.assertNotEqual('NOT 2015 Tesla Roadster', msg)
        self.assertIn('2015 Tesla Roadster', msg)
        self.assertNotIn('Z', msg)
        # my_tesla.battery.describe_battery()
        # my_tesla is object name based on class ElectricCar
        # battery is attribute of ElectricCar based on class Battery
        # describe_battery() is method of class Battery
        self.assertEqual("This car has a 60-kWh battery.",
                         my_tesla.battery.describe_battery())

    def test_child_override(self):
        """ Different answers to same request for car & Electric car. """
        my_saab = Car('Saab', '900', 1984)
        msg = my_saab.class_fill_gas_tank()
        self.assertEqual("Gas tank filled. 1984 Saab 900", msg)

        my_tesla = ElectricCar('tesla', 'Roadster', 2015)
        msg = my_tesla.class_fill_gas_tank()
        self.assertEqual("Can't fill gas tank of electric car!", msg)

    def test_stooges3(self):
        """ Test of 'do something for list'. """
        index = 0

        for stooge in self.stooges3:
            self.assertEqual(self.stooges3[index], stooge)
            index += 1

    def test_list_comprehension(self):
        """ See title - this works, why to use it is TBD. """

        comprehension_stooge_list = [stooge for stooge in self.stooges3]
        self.assertEqual(self.stooges3, comprehension_stooge_list)


# If you are running your module (the source file) as the main program, e.g.
# python test_oodemo.py
# interpreter assigns the hard-coded string "__main__" to the __name__variable
# so if true and unittest.main() runs
if __name__ == '__main__':
    unittest.main()
