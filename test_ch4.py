"""
File: test_ch4.py
Purpose: One or more tests for Try It Yourself in ch4
"""

import unittest
import ch4_tiy


class TestCh4TIY(unittest.TestCase):
    """ Class TIY (Test It Yourself) """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_example(self):
        """ See title """
        compare_list = []
        print("\nFOR example =======================================")
        test_comic_list = ['Moe', 'Larry', 'Curley']
        for comic in test_comic_list:
            print("comic is:" + comic + " is one of the Three Stooges")
            compare_list.append(comic)

        self.assertEqual(compare_list, ch4_tiy.for_example())

    def test_pizza_4_1(self):
        """ 3 parts
        1) Print list of pizza toppings
        2) Print 1 message with each topping
        3) Print 1 message at end
        Note: this file tests that correct list returned, not printed
        """
        print("\nPizza_4_1 ============================================")
        test_pizza_toppings = ['pepperoni', 'onion', 'green pepper']
        # print("DEBUG - test_pizza_toppings", test_pizza_toppings)
        # print("DEBUG - pizza_toppings", ch4_tiy.pizza_4_1())

        self.assertEqual(test_pizza_toppings, ch4_tiy.pizza_4_1())

    def test_count2twenty_4_3(self):
        """
        Use for loop to print numbers from 1 to 20 inclusive
        """
        print("\ncount2twenty_4_3 =====================================")
        test_numbers = list(range(1, 21))

        self.assertEqual(test_numbers, ch4_tiy.count2twenty_4_3())

    def test_sum_1_million_4_4(self):
        """
        Run min(), max() and sum() on list of a million numbers
        """
        print("\nsum_1_million_4_4 =====================================")
        test_numbers = list(range(1, 1000001))
        test_sum_numbers = sum(test_numbers)

        self.assertEqual(test_sum_numbers, ch4_tiy.sum_1_million_4_4())

    def test_odd2twenty_4_6(self):
        """
        Use for loop to print odd numbers from 1 to 20 inclusive
        """
        print("\nodd2twenty_4_6 =====================================")
        test_numbers = list(range(1, 21, 2))

        self.assertEqual(test_numbers, ch4_tiy.odd2twenty_4_6())

    def test_three2thirty_4_7(self):
        """
        Use for loop to print every 3rd number from 1 to 30 inclusive
        """
        print("\nthree2thirty_4_7 ===================================")
        test_numbers = list(range(1, 31, 3))

        self.assertEqual(test_numbers, ch4_tiy.three2thirty_4_7())

    def test_cube1to10_4_8(self):
        """
        Use for loop to print cubes from 1 to 10
        """
        test_cubed_list = []
        print("\ntest_cube1to10_4_8 AND list_comprehension ==========")
        for test_number in range(1, 11):
            test_number_cubed = test_number ** 3
            test_cubed_list.append(test_number_cubed)

        self.assertEqual(test_cubed_list, ch4_tiy.cube1to10_4_8())
        self.assertEqual(test_cubed_list, ch4_tiy.list_comprehension_4_9())

    def test_slices_4_10(self):
        """
        Use slices to:
          Print first three items in list
          Print middle three items in list
          Print last three items in list
        """
        print("\nslices_4_10 =====================================")
        test_numbers = list(range(1, 21))

        test_slice_range_start = 0
        test_slice_range_end = 3
        test_range = test_numbers[test_slice_range_start:test_slice_range_end]
        print("First three items in list are:")
        self.assertEqual(test_range,
                         ch4_tiy.slices_4_10(test_slice_range_start,
                                             test_slice_range_end))

        test_slice_range_start = 9
        test_slice_range_end = 12
        test_range = test_numbers[test_slice_range_start:test_slice_range_end]
        print("Middle three items in list are:")
        self.assertEqual(test_range,
                         ch4_tiy.slices_4_10(test_slice_range_start,
                                             test_slice_range_end))

        test_slice_range_start = 17
        test_slice_range_end = 21
        test_range = test_numbers[test_slice_range_start:test_slice_range_end]
        print("Last three items in list are:")
        self.assertEqual(test_range,
                         ch4_tiy.slices_4_10(test_slice_range_start,
                                             test_slice_range_end))

    def test_pizza_slice_4_11(self):
        """ 3 parts
        1) Add new pizza to original list
        2) Add different pizza to friends list
        3) Verify lists are different
        Note: this file tests that correct list returned, not printed and
              verify done here
        """
        print("\nPizza_slice_4_11 ===================================")
        test_pizza_mine = ['pepperoni', 'onion', 'green pepper']
        test_pizza_friend = test_pizza_mine[:]
        test_pizza_mine.append("pineapple")
        test_pizza_friend.append("sausage")

        print("My favorite pizzas are:")
        for test_pizza in test_pizza_mine:
            print(test_pizza)

        print("My friends favorite pizzas are:")
        for test_pizza in test_pizza_friend:
            print(test_pizza)

        self.assertNotEqual(test_pizza_mine, test_pizza_friend)

    def test_tuple_4_13(self):
        """
        Create tuple of 5 items
        Attempt to change tuple
        Overwrite entire tuple
        """
        print("\ntest_tuple_4_13 ====================================")
        menu_tuple = ("carrot", "kiwi", "hummis", "pepper", "cracker")
        for menu in menu_tuple:
            print("menu_tuple item is:", menu)

        print("")

        # generates E1137: 'menu_tuple' does not support item assignment
        # (unsupported-assignment-operation)
        # menu_tuple[0] = "meat"

        menu_tuple = \
            ("pretzels", "beer", "potato chips", "beef jerkey", "salt")
        for menu in menu_tuple:
            print("menu_tuple item is:", menu)
        # prevents no-self-use error
        self.assertTupleEqual(menu_tuple, menu_tuple)


class TestCh4(unittest.TestCase):
    """" class TestCh4 """

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
