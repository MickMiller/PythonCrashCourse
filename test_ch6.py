"""
File: test_ch6.py
Purpose: One or more tests for Try It Yourself in ch6
"""

import unittest
import ch6_tiy


class TestCh6TIY(unittest.TestCase):
    """ Class TIY (Test It Yourself) """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # PyDictCreation, access and other basic operations
    # noinspection PyDictCreation
    def test_simple_dict(self):
        """ Ch 6, pg 96 """
        # Next line has simpliest dictionary possible.
        # Dictionary name: alien_0, with key-value pair color-green
        # Key: color
        # Value: green
        alien_0 = {'color': 'green'}
        print(alien_0['color'])
        alien_1 = {'color': 'green', 'points': '5'}
        print('alien_1:', alien_1)

        alien_1['x_position'] = 0
        alien_1['y_position'] = 25
        print('alien_1:', alien_1)
        self.assertEqual(1, 1)  # prevent no-self-use error

        alien_2 = {}  # Creates empty dictionary
        alien_2['color'] = 'green'
        alien_2['points'] = 5
        print('alien_2:', alien_2)

        # Change value
        alien_2['color'] = 'yellow'
        print('alien_2 with color change:', alien_2)

        # Remove key-Value Pair
        del alien_2['color']
        print('alien_2 after color deletion:', alien_2)

        # Example of longer list
        favorite_languages = {
            'jen': 'python',
            'sarah': 'c',
            'edward': 'ruby',
            'phil': 'python',
        }
        print("Sarah's favorite language is " +
              favorite_languages['sarah'].title()
              + ".")

    def test_person_6_1(self):
        """ See title """
        test_jerry_1 = {
            'first_name': 'Jerry',
            'last_name': 'Miller',
            'age': "27",
            'city': 'North Chelmsford',
        }
        print("================== test_person_6_1: ")
        print(test_jerry_1["first_name"])
        print(test_jerry_1["last_name"])
        print(test_jerry_1["age"])
        print(test_jerry_1["city"] + "\n")

        self.assertEqual(test_jerry_1, ch6_tiy.person_6_1())

    def test_fav_num_6_2(self):
        """ Given key print dictionary value """
        test_glossary = {
            'Dijkstra': 0,
            'Three Dog Night': 1,
            'Jerry': 2,
            'Fluffy': 3,
            'Monty Python': 4,
        }
        print("test_fav_num_6_2 -----------------", test_glossary['Dijkstra'])
        print(test_glossary['Three Dog Night'])
        print(test_glossary['Jerry'])
        print(test_glossary['Fluffy'])
        print(test_glossary['Monty Python'])

        self.assertEqual(1, 1)

    def test_fav_num_6_3(self):
        """ Print key-value pairs """
        test_fav_num_dict_1 = {
            "0": 'Were number',
            "2": 'A pair is',
            "3": 'Pi is a little more than',
            "4": '2 squared is',
        }
        for key, value in test_fav_num_dict_1.items():
            print("\nKey: " + key)
            print("\nValue: " + value)

        self.assertEqual(1, 1)

    # noinspection PyDictCreation,PyDictCreation
    def test_fav_num_6_4(self):
        """ Add to list"""
        test_fruit_dict = {
            'apple': 'Planted by Johnny Appleseed',
            'bananas': 'Hard to know when to stop',
            'carrots': 'orange and long',
            'date': 'like a fig but different',
            'Elderberry': 'High in zinc',
        }

        test_fruit_dict['fig'] = "I don\'t give a"
        test_fruit_dict['grapes'] = "Green, Red or Black"
        test_fruit_dict['hardy kiwi'] = "Help you sleep"
        test_fruit_dict['indian plum'] = "color is very dark purple"
        test_fruit_dict['jackfruit'] = "Looks like green sandpaper"

        for key, value in test_fruit_dict.items():
            print("Key is: " + key)
            print("Value is: value" + value)

        self.assertEqual(1, 1)

    def test_river_country_6_5(self):
        """ Print key-valye pairs """
        test_river_country = {
            'nile': 'egypt',
            'mississippi': 'usa',
            'yangtze': 'china',
        }

        for key, value in test_river_country.items():
            print("The " + key + " runs through " + value)

        for key, value in test_river_country.items():
            print("River name is: " + key)

        for key, value in test_river_country.items():
            print("River country is: " + value)

        self.assertEqual(1, 1)

    def test_polling_6_6(self):
        """ Loop through list and extract relevant dictionary info """
        test_favorite_languages = {
            'jen': 'python',
            'sarah': 'c',
            'edward': 'ruby,',
            'phil': 'python',
        }
        test_poll_list = ['jen', 'phil', 'fred', 'barney']

        for folks in test_poll_list:  # Loop through all items in list
            # Loop through all keys in dictionary
            if folks not in test_favorite_languages.keys():
                print(folks + ' kindly take the language poll.')
            else:
                print(folks + ' thanks for taking the poll!')

        self.assertEqual(1, 1)

    def test_people_6_7(self):
        """ Dictionary in a list """
        # Based on 6_1 make dictionaries for people
        test_jerry = {
            'first_name': 'Jerry',
            'last_name': 'Miller',
            'age': "27",
            'city': 'North Chelmsford',
        }
        test_merrick = {
            'first_name': 'Merrick',
            'last_name': 'Miller',
            'age': "27",
            'city': 'Frankfurt, DE',
        }
        test_rose = {
            'first_name': 'Rose',
            'last_name': 'Miller',
            'age': "25",
            'city': 'North Chelmsford',
        }

        # Make list called people that contain all 3 dictionaries
        people = [test_jerry, test_merrick, test_rose]

        # Loop through list and print dictionary
        for folks in people[:]:
            print("People:" + str(folks))
            print('    First name: ' + folks['first_name'])
            print('    Last name: ' + folks['last_name'])
            print('    Age: ' + folks['age'])
            print('    City: ' + folks['city'])

        self.assertEqual(1, 1)

    def test_pets_6_8(self):
        """ Dictionary in a list """
        # Make dictionaries with pet info
        dusty = {
            'kind': 'cat',
            'owners_name': 'Mick',
        }
        skittles = {
            'kind': 'putty cat',
            'owners_name': 'Rose',
        }

        # Several pets stored in list
        pets = [dusty, skittles]

        # Loop through dictionary and print list
        for critter in pets[:]:
            print("    Kind of critter: " + critter['kind'])
            print("    Owners name: " + critter['owners_name'])

        self.assertEqual(1, 1)

    def test_favorite_places_6_9(self):
        """ Dictionary in a dictionary """
        # Dictionary favorite_places
        # noinspection PyUnusedLocal
        favorite_places = {
            'beach': ['Santa Monica'],
            'ocean': ['Atlantic', 'Pacific'],
            'promised_land': ['Joisey', 'Da Shore', 'Jones '],
        }

        # People and their favorite places
        people_favorite_places = {
            'Moe': ['beach'],
            'Larry': ['beach', 'ocean'],
            'Curley': ['beach', 'ocean', 'promised_land'],
        }

        # Print each name and their favorite places
        for name, favorite_places in people_favorite_places.items():
            print(name.title() + ' favorite places are: ')
            for place in favorite_places:
                print(place.title())

        self.assertEqual(1, 1)

    def test_fav_num_6_10(self):
        """ List in a dictionary """
        test_glossary = {
            'Dijkstra': [0, 1, 2],
            'Three Dog Night': [1, 2, 4],
            'Jerry': [2, 4, 6],
            'Fluffy': [3, 6, 9],
            'Monty Python': [4, 8, 16]
        }

        for entry in test_glossary.items():
            print("Entry is: ", entry)

        self.assertEqual(1, 1)

    def test_dict_in_dict(self):
        """ Dictionary in a dictionary """
        cities = {
            'Boston': {
                'country': 'USA',
                'population': '650,000',
                'fact': 'Sports teams doing well',
                },
            'London': {
                'country': 'UK',
                'population': '50,000,000',
                'fact': 'Sherlock Holmes lived there',
                },
            'Tokyo': {
                'country': 'Japan',
                'population': '100,000,000',
                'fact': 'Make nice cars',
            },
        }

        for city_name, city_info in cities.items():
            print("City Name: " + city_name + ": ")
            print("City Info: " + city_info['country'])
            print("           " + city_info['population'])
            print("           " + city_info['fact'] + '\n')

        self.assertEqual(1, 1)


class TestCh6(unittest.TestCase):
    """" class TestCh6 """

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
