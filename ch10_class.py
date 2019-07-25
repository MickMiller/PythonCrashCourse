""" File: ch10_class.py """

import os
import unittest
import json


class ReadFile(unittest.TestCase):
    """ See class name """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self, file_name):
        """ Initialize attributes """
        super().__init__()
        self.file_name = file_name
        self.line_number = 0

    def class_return_file(self, file_name):
        """ Return entire file """
        self.assertEqual(1, 1)
        try:
            with open(file_name) as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            return("The file " + file_name + " isn't found.")
        else:
            return(contents)

    def class_return_line(self, line_number):
        """ Read file one line at a time """

        line_cnt = 0
        ret_val = "None"
        with open(self.file_name) as file_object:
            for line in file_object:
                if line_cnt == line_number:
                    ret_val = line
                    break
                else:
                    line_cnt += 1
            return ret_val

    def class_count_words(self):
        """ Count the approximate number of words in a file """
        self.assertEqual(1, 1)

        try:
            with open(self.file_name) as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            msg = "test_book_length couldn't find file " + self.file_name
            print(msg)
            ret_val = None
        else:
            # Count the approximate number of works in the file
            words = contents.split()
            num_words = len(words)
            ret_val = num_words

        return ret_val

    def addition_10_06(self, in_1, in_2):
        """ See title """
        self.assertEqual(1, 1)

        try:
            num_1 = int(in_1)
        except ValueError:
            msg = "Invalid input " + in_1 + " is not integer."
            print(msg)
            return(msg)

        try:
            num_2 = int(in_2)
            sum_local = num_1 + num_2
        except (ValueError, UnboundLocalError):
            msg = "Invalid input entereed: either " + in_1 + " or " + in_2
            print(msg)
            return(msg)
        else:
            msg = "Sum of " + str(num_1) + " and " +\
                  str(num_2) + " = " + str(sum_local)
            print(msg)
            return(msg)

    def cat_dog_10_08(self, object_local):
        """ See title """
        self.assertEqual(1, 1)

        try:
            object_local.class_return_file(self.file_name)
            with open(self.file_name) as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            print("The file " + self.file_name + " isn't found.")
        else:
            print(contents)

    def print_or_skip_file_not_found(self, ret_val, filename):
        """ See title """
        self.assertEqual(1, 1)

        if ret_val == "The file " + filename + " isn't found.":
            ret_val = "File not found"

        return(ret_val)

    def common_words(self, filename, word, case):
        """ Return number of times word in file
            if case==lower then match against file in lower case
            else match against unchanged file
        """

        with open(filename) as f_obj:
            read_data = f_obj.read()
        if case == 'lower':
            count = read_data.lower().count(word)
        else:
            count = read_data.count(word)

        self.assertEqual(1, 1)
        return(count)

    def json_write(self, input_string):
        """ write file in json format """

        with open(self.file_name, 'w') as f_obj:
            json.dump(input_string, f_obj)

    def json_read(self):
        """ read file in json format """

        with open(self.file_name, 'r') as f_obj:
            return(json.load(f_obj))

    def json_recall_user_name(self, username, filename):
        """ write username to file in json format """
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)

        self.assertEqual(1, 1)
        return username

    def fav_num_rem_10_12(self, filename):
        """ See method name. """
        if os.path.exists(filename):
            ret_val = self.json_read()
        else:
            # fav_num = input("What is your favorite number?")
            fav_num = "3.14159"
            self.json_write(fav_num)
            ret_val = None
        return ret_val

    def get_new_username(self):
        """ See method name. """
        # new_username = input("What is your name? ")
        new_username = "Buckminster Fuller"
        self.json_write(new_username)
        return(new_username)

    def my_doc_test(self, param_1, param_2):
        """
        >>> my_function(2, 3)
        6
        >>> my_function('a', 3)
        'aaa'
        """
        self.assertEqual(1, 1)

        return param_1 * param_2
