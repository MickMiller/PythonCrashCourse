"""
File: test_ch5.py
Purpose: One or more tests for Try It Yourself in ch5
"""

import unittest
# import ch5_tiy


class TestCh4TIY(unittest.TestCase):
    """ Class TIY (Test It Yourself) """

    def setUp(self):
        pass

    def tearDown(self):
        pass
    #
    # def test_example(self):
    #     """ Simple example from PCC, pg 76 """
    #     test_cars = ["saab", "toyota", "bmw", "subaru"]
    #
    #     for test_car in test_cars:
    #         if test_car == 'bmw':
    #             car = ch5_tiy.example(test_car)
    #             test_car = test_car.upper()
    #         else:
    #             car = ch5_tiy.example(test_car)
    #             test_car = test_car.title()
    #
    #         self.assertEqual(car, test_car)
    #
    # def test_conditional_5_1(self):
    #     """ 10 test of IF - half True and half False """
    #     print("test_conditional_5_1 =================================")
    #     # Equality and inequality with strings
    #     car = ['saab']
    #     self.assertEqual(True, car == ['saab'])
    #     self.assertEqual(False, car == ['Saab'])
    #     self.assertEqual(True, car != ['Saab'])
    #
    #     # More equality and inequality with strings
    #     car = 'Saab'
    #     self.assertEqual(True, car == 'Saab')
    #     self.assertEqual(True, car != 'saab')
    #     self.assertEqual(True, (car.lower() == 'saab'))
    #
    #     # Equality and inequality with numbers
    #     number = 1
    #     self.assertEqual(True, number == 1)
    #     self.assertEqual(False, number != 1)
    #     self.assertEqual(True, number > 0)
    #     self.assertEqual(True, number < 2)
    #     self.assertEqual(True, number <= 1)
    #     self.assertEqual(True, number >= 1)
    #     self.assertEqual(True, number <= 2)
    #
    #     # Equality and inequality with AND and OR
    #     self.assertEqual(True, (number == 1 and number != 2))
    #     self.assertEqual(True, (number == 1 and 'Saab' in car))
    #     self.assertEqual(True, (number == 1 and 'Audi' not in car))
    #     self.assertEqual(True, (number > 0 or number <= 0))  # Usually passes
    #     self.assertEqual(False, (number > 1 or number < 1))
    #
    #     # Different style of AND and OR
    #     print("I predict True:", 'Saab' in car)
    #
    #     # Is item NOT in list
    #     print("I predict True:", 'Audi' not in car)
    #
    # def test_if_5_3(self):
    #     """ if alien colors #1 test """
    #     print("test_if_5_3 ==========================================")
    #     alien_color = 'green'
    #     if alien_color == 'green':
    #         print("You have earned 5 points")
    #
    #     if alien_color != 'green':
    #         print("You have earned 0 points")
    #
    #     self.assertEqual(alien_color, 'green')
    #
    # def test_if_5_4(self):
    #     """ if alien colors #2 test """
    #     print("test_if_5_4 ==========================================")
    #     alien_color_list = ['green', 'yellow', 'red']
    #     alien_color = alien_color_list[0]  # aka green
    #     if alien_color == 'green':
    #         print("You have earned 5 points")
    #     elif alien_color != 'green':
    #         print("You have earned 10 points")
    #     self.assertEqual(alien_color, 'green')
    #
    #     alien_color = alien_color_list[2]  # aka red
    #     if alien_color == 'green':
    #         print("You have earned 5 points")
    #     else:
    #         print("You have earned 10 points")
    #
    #     self.assertNotEqual(alien_color, 'green')
    #
    # def test_if_5_5(self):
    #     """ if alien colors #3 test """
    #     print("test_if_5_5 ==========================================")
    #     alien_color_list = ['green', 'yellow', 'red']
    #     test_alien_color = alien_color_list[0]  # aka green
    #     self.assertEqual(test_alien_color, ch5_tiy.if_5_5(test_alien_color))
    #     test_alien_color = alien_color_list[1]  # aka yellow
    #     self.assertEqual(test_alien_color, ch5_tiy.if_5_5(test_alien_color))
    #     test_alien_color = alien_color_list[2]  # aka red
    #     self.assertEqual(test_alien_color, ch5_tiy.if_5_5(test_alien_color))
    #
    # def test_if_5_6(self):
    #     """ if stages of life test """
    #     print("test_if_5_6 ==========================================")
    #     age = 1
    #     if age < 2:
    #         print("Stage of life is baby")
    #     elif age < 4:
    #         print("Stage of life is toddler")
    #     elif age < 13:
    #         print("Stage of life is kid")
    #     elif age < 20:
    #         print("Stage of life is teenager")
    #     elif age < 65:
    #         print("Stage of life is adult")
    #     elif age >= 4:
    #         print("Stage of life is elder")
    #     else:
    #         print("In test_if_5_6 there is a serious error")
    #
    #     self.assertEqual(1, 1)  # prevent no-self-use error
    #
    # def test_if_5_7(self):
    #     """ if Favorite fruit with independent if statements """
    #     print("test_if_5_7 ==========================================")
    #     favorite_fruits_list = ['apples', 'kiwi', 'bananas']
    #     favorite_fruit = favorite_fruits_list[0]  # aka apples
    #     if favorite_fruit == 'apples':
    #         print("You really like", favorite_fruit)
    #     if favorite_fruit == 'kiwi':
    #         print("You really like", favorite_fruit)
    #     if favorite_fruit == 'bananas':
    #         print("You really like", favorite_fruit)
    #     if favorite_fruit == 'not apples':
    #         print("You really like", favorite_fruit)
    #     if favorite_fruit == 'not kiwi':
    #         print("You really like", favorite_fruit)
    #
    #     self.assertEqual(1, 1)  # prevent no-self-use error
    #
    # def test_if_5_8(self):
    #     """ Hello Admin """
    #     print("test_if_5_8 ==========================================")
    #     test_user_list = ('admin', 'Eric', 'Mr. Cleese', 'Terry')
    #     user = test_user_list[0]  # aka admin
    #     self.assertEqual(user, ch5_tiy.if_5_8(user))
    #
    # def test_if_5_9(self):
    #     """ Hello Admin """
    #     print("test_if_5_9 ==========================================")
    #     test_current_user_list = ('admin', 'eric', "smith", 'jones', 'terry')
    #     test_new_user_list = ('a', 'e', "smith", 'jones', 't')
    #     test_new_user_candidate = 'A'
    #     if test_new_user_candidate.lower() in test_new_user_list:
    #         print("Kindly enter new username:")
    #     elif test_new_user_candidate.lower() not in test_current_user_list:
    #         print("Username is available")
    #
    #     self.assertEqual(1, 1)  # prevent no-self-use error
    #
    # def test_if_5_10(self):
    #     """ Ordinal Numbers """
    #     print("test_if_5_10 =========================================")
    #     test_number_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    #     number = test_number_list[3]
    #     for number in test_number_list:
    #         if number == 1:
    #             print("In test_if_5_10 ===== number:: " + str(number) + "st")
    #         elif number == 2:
    #             print("In test_if_5_10 ===== number:: " + str(number) + "nd")
    #         elif number == 3:
    #             print("In test_if_5_10 ===== number:: " + str(number) + "rd")
    #         else:
    #             print("In test_if_5_10 ====== number: " + str(number) + "th")
    #
    #     self.assertEqual(1, 1)  # prevent no-self-use error

    def test_add_list(self):
        """ Ordinal Numbers """
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        # see ~/Documents/Capture_1.PNG gathered 20190530 14:00
        test_number_list =\
            (25.63, 3.59, 1.99, 244.84, 19.99,
             1.59, 22.31, 4.77, 102.53, 6.18, 34.81,
             20.95, 13.88, 68.54, 5.33, 38.73,
             9.18, 60.00, 25.00, 40.0, 30.27,
             23.97, 27.72, 13.79, 73.00, 60.00,
             124.55, 14.95, 54.36, 18.02, 18.92,
             9.56, 11.76, 65.43, 1.99, 32.36,
             4.70, 3.24, 40.00, 481.93, 25.00,
             25.00
             )
        total = 0
        for num in test_number_list:
            total = total + num

        print("Total is:", total)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        self.assertEqual(1, 1)  # prevent no-self-use error


class TestCh5(unittest.TestCase):
    """" class TestCh5 """

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
