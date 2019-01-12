"""
File: test_ip_ch3_pyfilling.
Purpose: One or more tests for headers in
  Introducing Python chapter 3: PyFilling: Lists, Tuples, Dictionaries & Sets

  Methods do not have docstring.
  Due to method descriptive names and method brevity not needed.
"""


import unittest
import ip_ch3_pyfilling


class TestCh3(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Lists
    def test_empty_list_creation(self):
        """ None."""
        result = ip_ch3_pyfilling.empty_list_creation()
        self.assertEqual(result, [])

    def test_empty_list_creation_2(self):
        """ None."""
        result = ip_ch3_pyfilling.empty_list_creation_2()
        self.assertEqual(result, [])

    # Convert Other Data Types to List with list()
    def test_create_list_other_types(self):
        result = ip_ch3_pyfilling.create_list_other_types('cat')
        self.assertEqual(result, ['c', 'a', 't'])

    # Get an Item by Using [offset]
    def test_get_list_item_via_offset(self):
        result = ip_ch3_pyfilling.get_list_item_via_offset(0)
        self.assertEqual(result, 'Groucho')
        result = ip_ch3_pyfilling.get_list_item_via_offset(-3)
        self.assertEqual(result, 'Groucho')
        result = ip_ch3_pyfilling.get_list_item_via_offset(1)
        self.assertEqual(result, 'Chico')
        result = ip_ch3_pyfilling.get_list_item_via_offset(-2)
        self.assertEqual(result, 'Chico')
        result = ip_ch3_pyfilling.get_list_item_via_offset(2)
        self.assertEqual(result, 'Harpo')
        result = ip_ch3_pyfilling.get_list_item_via_offset(-1)
        self.assertEqual(result, 'Harpo')

    # Lists of Lists
    def test_get_list(self):
        item_1 = ['a']
        result = ip_ch3_pyfilling.get_list(0)
        self.assertEqual(result, item_1)

    def test_get_list_inside_list(self):
        result = ip_ch3_pyfilling.get_list_inside_list(1, 0)
        self.assertEqual(result, 'b')
        result = ip_ch3_pyfilling.get_list_inside_list(1, 1)
        self.assertEqual(result, 'c')

    # Change an Item by [offset]
    def test_change_list(self):
        result = ip_ch3_pyfilling.change_list('b')
        self.assertEqual(result, 'b')

    # Get a Slice to Extract Items by Offset Range
    def test_get_list_slice(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        my_list = ip_ch3_pyfilling.get_list_slice(0, 2)
        self.assertEqual(my_list, ['Groucho', 'Chico'])
        self.assertEqual(marxes[1:3], ['Chico', 'Harpo'])
        self.assertEqual(marxes[0:-2], ['Groucho'])
        # why marxes[2:0] returns [] != 'Harpo' is a mystery TBD
        self.assertEqual(marxes[2:], ['Harpo'])

    # Add item to end with append()
    def test_append_list(self):
        marxes_local = ['Groucho', 'Chico', 'Harpo']
        # Holy horseradish Batman!  Updating marxes_local updates marxes
        # marxes = marxes_local
        marxes = list(marxes_local)  # this does copy to new instance
        to_be_added = ['Zeppo']
        marxes_local.append(to_be_added)
        ip_ch3_pyfilling.append_list(marxes, to_be_added)
        self.assertEqual(marxes, marxes_local)

    def test_combine_lists(self):
        marxes_local = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        to_be_added = ['Gummo']
        marxes_local += to_be_added
        ip_ch3_pyfilling.combine_list(marxes, to_be_added)
        self.assertEqual(marxes, marxes_local)

    def test_insert_list(self):
        marxes_local = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        where_be_added = 1
        marxes_local.insert(where_be_added, 'Karl')
        ip_ch3_pyfilling.insert_list(marxes, where_be_added, 'Karl')
        self.assertEqual(marxes, marxes_local)

    def test_delete_item_from_list(self):
        marxes_local = ['Groucho', 'Karl', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        del marxes_local[1]
        ip_ch3_pyfilling.delete_item_from_list(marxes, 1)
        self.assertEqual(marxes, marxes_local)

    def test_delete_list_item_by_value(self):
        marxes_local = ['Groucho', 'Karl', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        marxes_local.remove('Karl')
        ip_ch3_pyfilling.delete_list_item_by_value(marxes, 'Karl')
        self.assertEqual(marxes, marxes_local)

    def test_pop_item(self):
        marxes = ['Groucho', 'Karl', 'Chico', 'Harpo', 'Zeppo']
        marxes_local = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        index_to_pop = 1
        ip_ch3_pyfilling.pop_item(marxes, index_to_pop)
        self.assertEqual(marxes, marxes_local)

    def test_find_list_offset(self):
        marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        result = ip_ch3_pyfilling.find_list_offset(marxes, 'Harpo')
        self.assertEqual(result, 2)

    def test_in_list(self):
        marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        result = ip_ch3_pyfilling.in_list(marxes, 'Harpo')
        self.assertEqual(result, True)
        result = ip_ch3_pyfilling.in_list(marxes, 'ZHarpo')
        self.assertEqual(result, False)
        result = ip_ch3_pyfilling.in_list(marxes, 'arpo')
        self.assertEqual(result, False)

    def test_count_items_in_list(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        result = ip_ch3_pyfilling.count_items_in_list(marxes, 'Harpo')
        self.assertEqual(result, 1)
        result = ip_ch3_pyfilling.count_items_in_list(marxes, 'Bob')
        self.assertEqual(result, 0)

    def test_join_and_split_1ist(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        seperator = ' * '
        result = ip_ch3_pyfilling.join_and_split_1ist(marxes, seperator)
        local_join = seperator.join(marxes)
        self.assertEqual(result, local_join)

    def test_join_and_split_list_2(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        seperator = " * "
        local_join = seperator.join(marxes)
        result = ip_ch3_pyfilling.join_and_split_list_2(local_join, seperator)
        self.assertEqual(result, marxes)

    def test_sorted_list(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        sorted_marxes = ['Chico', 'Groucho', 'Harpo']
        result = ip_ch3_pyfilling.sorted_list(marxes)
        self.assertEqual(result, sorted_marxes)

    def test_sort_list(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        result = ip_ch3_pyfilling.sort_list(marxes)
        marxes.sort()
        self.assertEqual(result, marxes)

    def test_len_list(self):
        marxes = ['Groucho', 'Chico', 'Harpo']
        result = ip_ch3_pyfilling.len_list(marxes)
        self.assertEqual(result, 3)

    def test_copy_list_slice(self):
        my_list = [1, 2, 3]
        result = ip_ch3_pyfilling.copy_list_slice(my_list)
        self.assertEqual(result, ['firstSurprise', 2, 3])
# Next two lines are correct according to Introducing Python, pg 53
#   but they fail when run
#        result = ip_ch3_pyfilling.copy_list_slice_copy(my_list)
#        self.assertEqual(result, [1, 2, 3])  # new_list unchanged
        result = ip_ch3_pyfilling.copy_list_slice_list(my_list)
        self.assertEqual(result, ['surprise', 2, 3])
        result = ip_ch3_pyfilling.copy_list_slice_slice(my_list)
        self.assertEqual(result, ['differentSurprise', 2, 3])


if __name__ == '__main__':
    unittest.main()
