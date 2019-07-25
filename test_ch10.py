""" File: test_ch10.py Purpose:
    Ch 10, pg 190 file_reader implementation
    To use self.assert() prints and input commented out and hardcoded.
"""

import builtins
import os
import unittest
from ch10_class import ReadFile
import ch10


class TestFileReader(unittest.TestCase):
    """ class TestFileReader """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_learning_python_10_01(self):
        """ See title """
        object_local = ReadFile('learning_python_10_01.txt')
        list_file = ch10.return_file(object_local)
        self.assertEqual(list_file,
                         ("I've learned that:\n"
                          "- process is important\n"
                          "- there are tools, eg PyCharm and TDD to support"
                          " process\n"))

    def test_learning_c_10_02(self):
        """ See title """
        object_local = ReadFile('learning_python_10_01.txt')
        line = ch10.return_file_line(object_local, 0)
        self.assertEqual(line,
                         "I've learned that:\n")
        line = ch10.return_file_line(object_local, 1)
        self.assertEqual(line,
                         "- process is important\n")
        line = ch10.return_file_line(object_local, 2)
        self.assertEqual(line,
                         ("- there are tools, eg PyCharm and TDD to support"
                          " process\n"))

    def test_guest_10_03(self):
        """ See title """
        # user_name = input("What is your name? ")
        filename = 'guest.txt'
        user_name = "DaMick"
        with open(filename, 'w+') as file_object:
            file_object.write(user_name)
            file_object.seek(0) # set pointer so read from beginning of file
            name_read = file_object.readline()
        self.assertEqual(user_name, name_read)

    def test_guest_10_04(self):
        """ See title """
        # user_name = input("What is your name? ")
        user_name = "Dr. Stephen Hawking"
        # print("Welcome " + user_name)
        with open('guest_book.txt', 'w+') as file_object:
            file_object.write(user_name)
            file_object.seek(0) # set pointer so read from beginning of file
            name_read = file_object.readline()

        self.assertEqual(user_name, name_read)

    def test_guest_10_05(self):
        """ See title """
        user_input_list = ["Because it's solution oriented! ",
                           "Solution oriented.  What are you from Joisey?",
                           "q"]
        index = 0
        with open('why_like_programming.txt', 'w+') as file_object:
            # user_input = input("Why do you like programming? (\'q\'=quit)")
            user_input = user_input_list[index]
            index += 1
            file_object.write(user_input)
            while user_input != 'q':
                # user_input = input("Why do you like programming? (\'q\'=qt)")
                user_input = user_input_list[index]
                index += 1
                file_object.write(user_input)
                if user_input != 'q':
                    break

            file_object.seek(0)  # pointer to beginning of file
            user_input_read = file_object.readlines()
            self.assertEqual(
                ["Because it's solution oriented! Solution oriented.  "
                 "What are you from Joisey?"], # This is a joke.  I'm from NJ
                user_input_read)

    def test_zerodivisionerror(self):
        """ See title """
        # print("Enter two numbers, and I'll divide (\'q\'=quit)")
        user_input = ["1", "2", "1", "0", "q"]
        index = 0
        while True:
            # first_number = input("\n first number: ")
            first_number = user_input[index]
            index += 1
            if first_number == 'q':
                break
            # second_number = input("\n second number: ")
            second_number = user_input[index]
            index += 1
            if second_number == 'q':
                break
            try:
                answer = int(first_number) / int(second_number)
            except ZeroDivisionError:
                # print("You can't divide by 0!")
                answer = "You can't divide by 0!"
                self.assertEqual("You can't divide by 0!", answer)
                break
            else:
                # print(answer)
                self.assertEqual(0.5, answer)

    def test_filenotfounderror(self):
        """ See title """
        filename = 'file_does_not_exist.txt'

        try:
            with open(filename) as f_obj:
                contents = f_obj.read()
        except builtins.FileNotFoundError:
            # print("The file " + filename + " isn't found.")
            result = "The file file_does_not_exist.txt isn't found."
        else:
            # print(contents)
            result = contents

        self.assertEqual("The file file_does_not_exist.txt isn't found.",
                         result)

    def test_json_write(self):
        """ See title """
        number = [2, 3, 5, 7, 11, 13]

        filename = 'number.json'

        object_local = ReadFile(filename)
        object_local.json_write(number)

        self.assertEqual(1, 1)

    def test_json_read(self):
        """ See title """
        filename = 'number.json'
        number = [2, 3, 5, 7, 11, 13]

        object_local = ReadFile(filename)

        number_retured = object_local.json_read()
        self.assertEqual(number, number_retured)

    def test_json_recall_user_name(self):
        """ See title """

        # username = input("What is your name?")
        username = 'Benjamin Franklin'
        filename = 'username.json'

        object_local = ReadFile(filename)

        name_returned = object_local.json_recall_user_name(username, filename)
        self.assertEqual(username, name_returned)

    def test_json_recall_user_read(self):
        """ See title """

        username = 'Benjamin Franklin'
        filename = 'username.json'

        object_local = ReadFile(filename)

        name_returned = object_local.json_read()
        self.assertEqual(username, name_returned)

    def test_fav_num_10_11(self):
        """ See title """
        filename = "fav_num_10_11"
        object_local = ReadFile(filename)

        # fav_num = input("What is your favorite number? ")
        fav_num = "3.14159"
        object_local.json_write(fav_num)

        fav_num_stored = object_local.json_read()
        # print("I know your favorite number!  It's " + fav_num_stored)

        self.assertEqual(fav_num, fav_num_stored)

    def test_fav_num_rem_10_12(self):
        """ See title """
        filename = "fav_num_rem_10_11"
        local_object = ReadFile(filename)

        if os.path.exists(filename):
            os.remove(filename)

        ret_val = local_object.fav_num_rem_10_12(filename)
        self.assertEqual(ret_val, None)

        ret_val = local_object.fav_num_rem_10_12(filename)
        self.assertEqual(ret_val, "3.14159")

    def test_verify_user_10_13(self):
        """ See title """
        filename = 'username.json'
        local_object = ReadFile(filename)

        try:
            with open(filename) as f_obj:
                contents = f_obj.read()
        except builtins.FileNotFoundError:
            # username = input("What is your name? ")
            username = "Buckminster Fuller"
            local_object.json_write(username)
            # print("We'll remember you when you come back " + username + "1")
        else:
            # name_ok = input(contents +
            #                 "- is this your name? Y or anything else")
            name_ok = "n"
            if name_ok == "Y":
                print("Hello " + contents)
            else:
                new_username = local_object.get_new_username()
                self.assertEqual("Buckminster Fuller", new_username)

        if os.path.exists(filename):  # Tidy up
            os.remove(filename)

    def test_my_doc_test(self):
        """ Demo of Doctest"""

        local_object = ReadFile("alice.txt")

        here_val = 1 * 1
        ret_val = local_object.my_doc_test(1, 1)
        self.assertEqual(here_val, ret_val)

        here_val = 2 * 3
        ret_val = local_object.my_doc_test(2, 3)
        self.assertEqual(here_val, ret_val)

        here_val = 'a' * 3
        ret_val = local_object.my_doc_test('a', 3)
        self.assertEqual(here_val, ret_val)

    def test_count_words(self):
        """ See title. """
        local_object = ReadFile("file_w_4_words.txt")

        count = ch10.count_words(local_object)
        # print("Count of words is: ", count)
        self.assertEqual(4, count)


if __name__ == '__main__':
    unittest.main()
