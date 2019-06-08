"""
File: test_ch8.py
Purpose: One or more tests for Try It Yourself
"""

import unittest


import ch7_tiy


class TestCh7TIY(unittest.TestCase):
    """ Class TIY (Test It Yourself) """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_greeter(self):
        """ See title """
        self.assertEqual("your name", ch7_tiy.greeter())

    def test_rental_cat_7_1(self):
        """ See title """
        car = input("Kindly enter type of car you'd like: ")
        print("We'll see if we can find you a " + car)

        self.assertEqual(1, 1)

    def test_restaurant_seating_cat_7_2(self):
        """ See title """
        dinner_cnt = input("How many in your party? ")
        if int(dinner_cnt) > 8:
            print("You'll have to wait")
        else:
            print("Walk this way!")

        self.assertEqual(1, 1)

    def test_multiple_of_ten_7_3(self):
        """ See title
        Note there is no testing of input so text input accepted and may or
            may not be a multiple of 10
        """
        num_entered = input("Enter a number: ")
        if (int(num_entered) % 10) == 0:
            print("Number is a multiple of 10")
        else:
            print("Not a multiple of 10")

        self.assertEqual(1, 1)

    def test_pizza_toppings_7_4(self):
        """ See title """
        topping = "w"
        while topping != "q":
            topping = input("Enter a pizza topping or \"q\" to quit: ")
            if topping == "q":
                break
            print("Your topping is: " + topping)

        self.assertEqual(1, 1)

    def test_movie_tickets_7_5(self):
        """ See title
        There is no testing of input so "w" causes an error.
        """
        response = -1
        while response != 0:
            response = input("Enter your age or \"q\" to quit: ")
            if response == "q":
                break
            elif int(response) < 3:
                print("Your ticket is free!")
            elif int(response) <= 12:
                print("Your ticket is $10")
            else:
                print("Your ticket is $15")

        self.assertEqual(1, 1)

    def test_three_exits_7_6(self):
        """ Three ways to exit while:
            conditional test, active variable and break """
        cnt = 0
        response = -1
        while response != 0:
            if cnt >= 4:
                break
            print("Enter age OR")
            print("        \"q\" to quit OR")
            response = \
                input("        \"c\" to not print msg \"Your ticket is\": ")
            if response == "q":
                break
            elif response == "c":
                continue
            elif int(response) < 3:
                print("Your ticket is free!")
            elif int(response) <= 12:
                print("Your ticket is $10")
            else:
                print("Your ticket is $15")

        self.assertEqual(1, 1)

    # def test_movie_tickets_7_7(self): # During development did it

    def test_deli_7_8(self):
        """ Inside while loop move items from one list to another """
        # Initial lists
        sandwich_orders = ['green eggs and ham', 'pizza', 'burgers', 'fries']
        finished_sandwiches = []

        while sandwich_orders:  # Turns false when list empty
            sandwich = sandwich_orders.pop()
            finished_sandwiches.append(sandwich)
            print("Just made sandwich: " + sandwich)

        print("Sandwiches are:" + str(finished_sandwiches))

        self.assertEqual(1, 1)

    def test_deli_no_pastrami_7_9(self):
        """ 7_8 with restriction no pastrami """
        # Initial lists
        sandwich_orders = ['pastrami', 'green eggs and ham', 'pizza',
                           'pastrami', 'burgers', 'fries', 'pastrami']
        finished_sandwiches = []

        print("Yes we have no pastrami, we have no pastrami today")

        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')

        while sandwich_orders:  # Turns false when list empty
            sandwich = sandwich_orders.pop()
            finished_sandwiches.append(sandwich)
            print("Just made sandwich: " + sandwich)

        print("Sandwiches are:" + str(finished_sandwiches))

        self.assertEqual(1, 1)

    def test_dream_vacation_7_10(self):
        """ Builds list """
        # Initial list
        vacation_location = []
        user_input = "w"

        while user_input != "q":
            print("To exit enter \"q\"")
            user_input = input("Where would you like to go on vacation?")
            if user_input != "q":
                vacation_location.append(user_input)

        print("Dream locations are:{0}".format(str(vacation_location)))

        self.assertEqual(1, 1)


class TestCh7(unittest.TestCase):
    """" class TestCh7 """

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
