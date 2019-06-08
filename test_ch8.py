"""
File: test_ch8.py
Purpose: One or more tests for Try It Yourself
"""

import unittest
import ch8_tiy
from ch8_imports import import_module_name_function_name
from ch8_imports import import_module_name_function_name_abbreviated as imnfna
import ch8_imports as imna


class TestCh8TIY(unittest.TestCase):
    """ Class TIY (Test It Yourself) """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_display_message_8_1(self):
        """ See title """
        ch8_tiy.display_message_8_1()

        self.assertEqual(1, 1)

    def test_keyword_arg(self):
        """ See title """
        self.assertEqual("First, Second",
                         ch8_tiy.keyword_arg("First",
                                             "Second"))
        self.assertEqual("Second, First",
                         ch8_tiy.keyword_arg("Second",
                                             "First"))

    def test_default_val(self):
        """ See title """
        self.assertEqual("First, Second",
                         ch8_tiy.default_val("First"))
        self.assertEqual("First, 2nd",
                         ch8_tiy.default_val("First",
                                             "2nd"))
        self.assertEqual("This is first returned, This is 2nd returned",
                         ch8_tiy.default_val(second="This is 2nd returned",
                                             first="This is first returned"))

    def test_make_shirt_8_3(self):
        """ See title """
        self.assertEqual("GMM, 6 7/8",
                         ch8_tiy.make_shirt_8_3("6 7/8", "GMM"))
        self.assertEqual('7 6/8, GM',
                         ch8_tiy.make_shirt_8_3(text='GM', size='7 6/8'))

    def test_large_shirt_8_4(self):
        """ See title """
        self.assertEqual("6 7/8, GMM",
                         ch8_tiy.make_shirt_8_3("GMM", "6 7/8"))
        self.assertEqual('7 6/8, GM',
                         ch8_tiy.make_shirt_8_3(size='7 6/8', text='GM'))

    def test_describe_city_8_5(self):
        """ See title """
        self.assertEqual("Frankfurt is in Germany",
                         ch8_tiy.describe_city_8_5("Frankfurt", "Germany"))
        self.assertEqual("London is in England",
                         ch8_tiy.describe_city_8_5("London", "England"))
        self.assertEqual('Chelmsford is in United States',
                         ch8_tiy.describe_city_8_5('Chelmsford'))

    def test_optional_parameter(self):
        """ Call with optional parameters including missing last param and
            missing last 2 params
        """
        self.assertEqual("Bruce Springsteen0",
                         ch8_tiy.optional_parameter("Springsteen", "Bruce"))
        self.assertEqual("Eric The Red",
                         ch8_tiy.optional_parameter("Red", "Eric", "The"))

        self.assertEqual("one two",
                         ch8_tiy.optional_parameter_2(
                             "one", "two"))

        self.assertEqual("one two three",
                         ch8_tiy.optional_parameter_2(
                             "one", "two", "three"))
        self.assertEqual("one three two",
                         ch8_tiy.optional_parameter_2(
                             "one", "three", "two"))
        self.assertEqual("one two three four",
                         ch8_tiy.optional_parameter_2(
                             "one", "two", "three", "four"))

    def test_return_dictionary(self):
        """ See title """
        self.assertDictEqual(
            {'first': 'First_dict_item', 'last': 'Second', 'age': 'Optional'},
            ch8_tiy.return_dictionary(
                "First_dict_item",
                "Second",
                "Optional"))

        self.assertDictEqual(
            {'first': 'First_dict_item', 'last': 'Second'},
            ch8_tiy.return_dictionary(
                "First_dict_item", "Second"))

    def test_city_name_8_6(self):
        """ See title """
        while True:
            city_name = input("Kindly enter city (\'q\' to quit): ")
            if city_name == 'q':
                break

            country_name = input("Kindly enter country (\'q\' to quit): ")
            if country_name == 'q':
                break

            print("\"" + city_name + ", " + country_name + "\"")
            self.assertEqual(city_name + ", " + country_name,
                             ch8_tiy.city_name_8_6(city_name, country_name))

    def test_album_8_7(self):
        """ See title"""
        print("Kindly enter 3 artists, albums (optionally) number of tracks:")
        print("If optional parameter is not entered then assert will fail")
        name_1 = input("Enter ")
        album_1 = input("album title")
        tracks_1 = input("Num of tracks (optional)")
        artist_dict_num_1 =\
            ch8_tiy.return_dictionary(name_1, album_1, tracks_1)

        name_2 = input("Enter ")
        album_2 = input("album title")
        tracks_2 = input("Num of tracks (optional)")
        artist_dict_num_2 =\
            ch8_tiy.return_dictionary(name_2, album_2, tracks_2)

        name_3 = input("Enter ")
        album_3 = input("album title")
        tracks_3 = input("Num of tracks (optional)")
        artist_dict_num_3 =\
            ch8_tiy.return_dictionary(name_3, album_3, tracks_3)

        self.assertDictEqual({'first': name_3,
                              'last': album_3,
                              'age': tracks_3},
                             ch8_tiy.return_dictionary(
                                 name_3, album_3, tracks_3))

        print("artist_dict_1:", artist_dict_num_1)
        print("artist_dict_2:", artist_dict_num_2)
        print("artist_dict_3:", artist_dict_num_3)

    def test_album_8_8(self):
        """ See title"""
        print("Kindly enter artist, album (optionally) number of tracks:")
        while True:
            print("Enter \'q\' to quit")
            name = input("Enter ")
            if name == 'q':
                break
            album = input("album title")
            tracks = input("Num of tracks (optional)")
            artist_dict_num =\
                ch8_tiy.return_dictionary(name, album, tracks)

            # Note if optional parameter not entered then assert will fail
            self.assertDictEqual({'first': name,
                                  'last': album,
                                  'age': tracks},
                                 ch8_tiy.return_dictionary(
                                     name, album, tracks))

            print("artist_dict_1:", artist_dict_num)

    def test_greet_users(self):
        """ Print a simple greeting to each user in list """
        user_names = ['hanna', 'ty', 'margot']
        ch8_tiy.greet_users(user_names)

        self.assertEqual(1, 1)

    def test_show_magicians_8_9(self):
        """ Print a simple greeting to each user in list """
        names = ['houdini', 'david']
        ch8_tiy.show_magicians_8_9(names)

        self.assertEqual(1, 1)

    def test_great_magicians_8_10(self):
        """ Print a list with text """
        names = ['houdini', 'david']
        ch8_tiy.make_great_8_10(names)
        ch8_tiy.show_magicians_8_9(names)
        self.assertEqual(1, 1)

    def test_great_magicians_8_11(self):
        """ Print a list with text """
        names = ['houdini', 'david']
        names_saved = names[:]
        ch8_tiy.make_great_8_10(names)
        ch8_tiy.show_magicians_8_9(names)
        self.assertEqual(1, 1)
        print("Original list which is changed: " + str(names))
        print("Saved unchanged list: " + str(names_saved))

    def test_build_profile(self):
        """ Accept arbitrary number of arguments on unknown kind """
        user_profile = ch8_tiy.build_profile('albert',
                                             'einstein',
                                             location='princeton',
                                             field='physics')
        print(user_profile)
        self.assertEqual(1, 1)

    def test_sandwich_8_12(self):
        """ Accept arbitrary number of ingredients """
        ch8_tiy.sandwich_8_12('meat')
        ch8_tiy.sandwich_8_12('meat',
                              'cheese')
        ch8_tiy.sandwich_8_12('meat',
                              'cheese',
                              'veggies')
        self.assertEqual(1, 1)

    def test_user_profile_8_13(self):
        """ Accept arbitrary number of arguments on unknown kind """
        user_profile = ch8_tiy.build_profile('Da Mick',
                                             'Miller',
                                             location='North Chelmsford',
                                             field='physics')
        print(user_profile)
        self.assertEqual(1, 1)

    def test_sandwich_8_13(self):
        """ Accept arbitrary number of ingredients """
        ch8_tiy.sandwich_8_12('meat')
        ch8_tiy.sandwich_8_12('meat',
                              'cheese')
        ch8_tiy.sandwich_8_12('meat',
                              'cheese',
                              'veggies')
        self.assertEqual(1, 1)

    def test_cars_8_14(self):
        """ Accept arbitrary number of arguments on unknown kind """
        car_profile = ch8_tiy.cars_8_14('Saab',
                                        '900')
        print("Car is: " + str(car_profile))
        car_profile = ch8_tiy.cars_8_14('Saab',
                                        '900',
                                        color='Red',
                                        tranny='5 speed')
        print("Car is: " + str(car_profile))
        car_profile = ch8_tiy.cars_8_14('Saab',
                                        '900',
                                        color='Grey',
                                        tranny='auto',
                                        top='sunroof')
        print("Car is: " + str(car_profile))
        self.assertEqual(1, 1)

    def test_import_module_name(self):
        """ import_module name """
        ch8_tiy.import_module_name()
        self.assertEqual(1, 1)

    def test_import_module_name_function_name(self):
        """ import_module name """
        import_module_name_function_name()
        self.assertEqual(1, 1)

    def import_module_name_function_name_abbreviated(self):
        """ import_module_name_function_name_abbreviated """
        imnfna()
        self.assertEqual(1, 1)

    def test_import_module_name_abbreviated(self):
        """ import_module_name_abbreviated """
        imna.import_module_name_abbreviated()
        self.assertEqual(1, 1)


class TestCh8(unittest.TestCase):
    """" class TestCh8 """

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
