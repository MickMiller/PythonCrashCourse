"""
File: test_ch3.py
Purpose: One or more tests for headers in
    Introducing Python chapter 3: PyFilling: Lists, Tuples, Dictionaries & Sets
    File to be ADDed, COMMITted and MERGEd into branch master"
ER are this change wiped out by git pull"""

import unittest
import ch3_pyfilling  # imports all functions in module ch3_pyfilling
from ch3_tiy import names_3_1  # from module ch3_tiy import function names_3_1
from ch3_tiy import greetings_3_2
from ch3_tiy import fav_transportation_3_3
from ch3_tiy import dinner_guest_3_4
from ch3_tiy import dinner_guest_3_5
from ch3_tiy import dinner_guest_3_6
from ch3_tiy import dinner_guest_3_7
from ch3_tiy import seeing_world_3_8
from ch3_tiy import dinner_guest_3_9
from ch3_tiy import show_items_in_list_3_10
from ch3_tiy import change_list_3_10
from ch3_tiy import insert_in_list_3_10
from ch3_tiy import del_from_list_3_10
from ch3_tiy import remove_by_value_3_10
from ch3_tiy import remove_by_label_3_10
from ch3_tiy import remove_by_pop_3_10
from ch3_tiy import len_3_10
from ch3_tiy import sort_list_unchanged_3_10
from ch3_tiy import sort_list_changed_3_10
from ch3_tiy import append_3_10
from ch3_tiy import reverse_3_10
from ch3_tiy import sort_list_reverse_3_10


class TestCh3TIY(unittest.TestCase):
    """ Class TestCh3TIT (Test It Yourself) """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Lists
    def test_names_3_1(self):
        """ See title """
        print("\nDinner_guest_3_1 =======================================")
        transport_list = ["Moe", "Larry", "Curley", "Stan"]
        tn_result = names_3_1(0)
        self.assertEqual(tn_result, transport_list[0])
        tn_result = names_3_1(1)
        self.assertEqual(tn_result, transport_list[1])
        tn_result = names_3_1(2)
        self.assertEqual(tn_result, transport_list[2])
        # Next two lines show error
        # tn_result = names_3_1(3)
        # self.assertEqual(tn_result, transport_list[3])

    def test_greetings_3_2(self):
        """ See title """
        print("\nDinner_guest_3_2 =======================================")
        transport_list = ["Moe", "Larry", "Curley", "Stan"]
        m_print_1 = "Greetings, "
        m_print_2 = " Uncle Sam would like you to travel the world."
        tg_result = m_print_1 + transport_list[0] + m_print_2
        self.assertEqual(tg_result,
                         greetings_3_2(0))
        tg_result = m_print_1 + transport_list[1] + m_print_2
        self.assertEqual(tg_result,
                         greetings_3_2(1))
        tg_result = m_print_1 + transport_list[2] + m_print_2
        self.assertEqual(tg_result,
                         greetings_3_2(2))

    def test_fav_transportation_3_3(self):
        """ See title """
        print("\nDinner_guest_3_3 =======================================")
        transport_list = ["Car", "foot", "Segway"]
        m_print_1 = "I like to get places using "
        m_print_2 = " to travel the world."
        tf_result = m_print_1 + transport_list[0] + m_print_2
        self.assertEqual(tf_result,
                         fav_transportation_3_3(0))
        tf_result = m_print_1 + transport_list[1] + m_print_2
        self.assertEqual(tf_result,
                         fav_transportation_3_3(1))
        tf_result = m_print_1 + transport_list[2] + m_print_2
        self.assertEqual(tf_result,
                         fav_transportation_3_3(2))

    def test_dinner_guest_3_4(self):
        """ See title """
        print("\nDinner_guest_3_4 =======================================")
        guest_list = ["Larry da Vinci", "Ben Franklin", "Genghis Khan"]
        m_print_1 = "Dear "
        m_print_2 = " could you attend a BBQ at my house on 4 July 2019."
        td_result = m_print_1 + guest_list[0] + m_print_2
        self.assertEqual(td_result,
                         dinner_guest_3_4(0))
        td_result = m_print_1 + guest_list[1] + m_print_2
        self.assertEqual(td_result,
                         dinner_guest_3_4(1))
        td_result = m_print_1 + guest_list[2] + m_print_2
        self.assertEqual(td_result,
                         dinner_guest_3_4(2))

    def test_dinner_guest_3_5(self):
        """ See title """
        print("\nDinner_guest_3_5 =======================================")
        guest_list = \
            ["Larry da Vinci", "Ben Franklin", "Genghis Khan", "Hellen Keller"]
        m_print_t = "Who can attend:"
        m_print_f = "Who can not attend:"
        #
        ret_result = dinner_guest_3_5(2, "F")
        tret_result = guest_list[2]
        tret_result = m_print_f + tret_result
        self.assertEqual(ret_result, tret_result)
        #
        ret_result = dinner_guest_3_5(2, "T")
        tret_result = guest_list[3]
        tret_result = m_print_t + tret_result
        self.assertEqual(ret_result, tret_result)
        #
        ret_result = dinner_guest_3_5(0, "T")
        tret_result = guest_list[0]
        tret_result = m_print_t + tret_result
        self.assertEqual(ret_result, tret_result)
        #
        ret_result = dinner_guest_3_5(1, "T")
        tret_result = guest_list[1]
        tret_result = m_print_t + tret_result
        self.assertEqual(ret_result, tret_result)
        #
        ret_result = dinner_guest_3_5(2, "T")
        tret_result = guest_list[3]
        tret_result = m_print_t + tret_result
        self.assertEqual(ret_result, tret_result)

    def test_dinner_guest_3_6(self):
        """ See title """
        print("\nDinner_guest_3_6 =======================================")
        guest_list = \
            ["Larry da Vinci", "Ben Franklin", "Hellen Keller"]
        guest_list.insert(0, "Al Einstein")
        guest_list.insert(2, "Prof Uncle Eric")
        guest_list.append("Dear Old Dad")

        m_print_0 = "A bigger table was found!  Here are all the guests:"
        #
        td_result = m_print_0 + "\n" + str(guest_list)
        self.assertEqual(td_result, dinner_guest_3_6())

    def test_dinner_guest_3_7(self):
        """ See title """
        print("\nDinner_guest_3_7 =======================================")
        guest_list = \
            ["Larry da Vinci", "Ben Franklin", "Hellen Keller"]
        guest_list.insert(0, "Al Einstein")
        guest_list.insert(2, "Prof Uncle Eric")
        guest_list.append(" Dear Old Dad")

        m_print_0 = "Sorry only 2 guests."
        guest_list.pop(0)
        guest_list.pop(0)
        guest_list.pop(0)
        guest_list.pop(0)
        #
        m_print_0 = "Remaining guests are:"
        td_result = m_print_0 + "\n" + str(guest_list)
        guest_list.pop(0)
        guest_list.pop(0)
        #
        td_result = str(guest_list)
        self.assertEqual(td_result, dinner_guest_3_7())

    def test_seeing_world_3_8(self):
        """ See title """
        print("\nSeeing the world 3_8 =======================================")
        world_list = \
            ["Frankfort", "Richmond", "Joisey", "Normandy", "Auschwitz"]

        # Change order of list via sorted and show original list unchanged
        # List in original order
        list_to_verify = world_list[:]  # Copy w_l to l_t_v

        # Next executable line alphabetizes w_l and assigns to n_l
        #    w_l unchanged
        new_list = sorted(world_list)
        list_to_verify.append(new_list)  # adds new object, n_l to end of l_t_v
        # list_to_verify.attach(new_list) #  adds 5 items viz n_l to l_t_v

        # Reverse order of list via sorted and show original list unchanged
        new_list = sorted(world_list, reverse=True)
        list_to_verify.append(new_list)
        #
        # Change order of list via reverse() and show original list changed
        new_list = world_list[:]
        new_list.reverse()  # Reverses new_list
        list_to_verify.append(new_list)
        #
        # Change order of list via reverse() and show back to original list
        new_list.reverse()  # Re-reverses n_l restoring original
        list_to_verify.append(new_list)
        #
        # Change list to alphabetical order via sort
        new_list = world_list[:]  # Copy w_l to n_l
        new_list.sort()
        list_to_verify.append(new_list)
        #
        # Change list to reverse alphabetical order via sort
        new_list.sort(reverse=True)
        list_to_verify.append(new_list)
        self.assertEqual(list_to_verify, seeing_world_3_8())

    def test_dinner_guest_3_9(self):
        """ See title """
        print("\ndinner_guests_3_9 =======================================")
        guest_list = ["Larry da Vinci", "Ben Franklin", "Hellen Keller"]
        self.assertEqual(len(guest_list), dinner_guest_3_9())

    def test_show_items_in_list_3_10(self):
        """ 14 commands tested for 3-10 Every Function.  Form of all tests:
        - Make BEFORE list
        - Send to dinner_guest_3_10()
        - ASSERT that returned value is ER
        - Naming convention is DESCRIPTION_3_10
        - DESCRIPTIONS:
          show_items_in_list      change_list           insert   del
          remove_by_value         remove_by_label       pop      len
          sort_list_unchanged     sorted_list_changed   append   reverse
          reversed_list_changed
        """
        print("\ntest_show_items_in_list_3_10")
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
    # Show items in list (first, last and in-between)
        results_all_list = my_list[0]
        results_all_list = results_all_list + my_list[2]
        results_all_list = results_all_list + my_list[1]
        returned_list = show_items_in_list_3_10(0)
        returned_list = returned_list + show_items_in_list_3_10(2)
        returned_list = returned_list + show_items_in_list_3_10(1)

        self.assertEqual(results_all_list, returned_list)

    def test_change_list_3_10(self):
        """ See title   """
        print("\ntest_change_list_3_10")
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        # Change items in list (first, last and in-between)
        result_list = my_list[:]
        result_list[0] = "Learn Python"
        result_list[1] = "Build jigs"
        result_list[2] = "Modular workspaces"
        returned_list = my_list[:]
        returned_list = change_list_3_10(returned_list, 0, "Learn Python")
        returned_list = change_list_3_10(returned_list, 1, "Build jigs")
        returned_list = change_list_3_10(returned_list, 2,
                                         "Modular workspaces")

        self.assertEqual(result_list, returned_list)

    def test_insert_in_list_3_10(self):
        """ See title   """
        # Add item to specified place in list
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = my_list[:]
        my_list.insert(1, "very well")
        returned_list = insert_in_list_3_10(returned_list, 1, "very well")

        self.assertEqual(my_list, returned_list)

    def test_del_from_list_3_10(self):
        """ See title   """
        # del from specified place in list
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = my_list[:]
        del my_list[1]
        returned_list = del_from_list_3_10(returned_list, 1)

        self.assertEqual(my_list, returned_list)

    def test_remove_by_value_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = my_list[:]
        my_list.remove("Build boxes")
        returned_list = remove_by_value_3_10(returned_list, "Build boxes")

        self.assertEqual(my_list, returned_list)

    def test_remove_by_label_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = my_list[:]
        already_done = "Build boxes"
        my_list.remove(already_done)
        returned_list = remove_by_label_3_10(returned_list, already_done)

        self.assertEqual(my_list, returned_list)

    def test_remove_by_pop_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = my_list[:]
        my_list.pop(1)
        returned_list = remove_by_pop_3_10(returned_list, 1)

        self.assertEqual(my_list, returned_list)

    def test_len_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = my_list[:]
        my_len = len(my_list)
        list_len = len_3_10(returned_list)

        self.assertEqual(my_len, list_len)

    def test_sort_list_unchanged_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        returned_list = sort_list_unchanged_3_10(my_list)

        self.assertEqual(my_list, returned_list)

    def test_sort_list_changed_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        my_list.sort()
        returned_list = sort_list_changed_3_10(my_list)
        my_list.sort()

        self.assertEqual(my_list, returned_list)

    def test_append_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        sent_list = my_list[:]
        returned_list = append_3_10(sent_list, "FTJ")
        my_list.append("FTJ")

        self.assertEqual(my_list, returned_list)

    def test_reverse_3_10(self):
        """ See title   """
        # reversed_list_changed
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        sent_list = my_list[:]
        returned_list = reverse_3_10(sent_list)
        my_list.reverse()

        self.assertEqual(my_list, returned_list)

    def test_sort_list_reverse_3_10(self):
        """ See title   """
        my_list = ["Teach Python", "Build boxes", "Create workshop"]
        sent_list = my_list[:]
        returned_list = sort_list_reverse_3_10(sent_list)
        my_list.sort(reverse=True)
        self.assertEqual(my_list, returned_list)


class TestCh3(unittest.TestCase):
    """" dclass TestCh3 """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Lists
    def test_empty_list_creation(self):
        """ See title """
        el_result = ch3_pyfilling.empty_list_creation()
        self.assertEqual(el_result, [])

    def test_empty_list_creation_2(self):
        """ See title """
        el_result = ch3_pyfilling.empty_list_creation_2()
        self.assertEqual(el_result, [])

    # Convert Other Data Types to List with list()
    def test_create_list_other_types(self):
        """ See title """
        el_result = ch3_pyfilling.create_list_other_types('cat')
        self.assertEqual(el_result, ['c', 'a', 't'])

    # Get an Item by Using [offset]
    def test_get_list_item_via_offset(self):
        """ See title """
        el_result = ch3_pyfilling.get_list_item_via_offset(0)
        self.assertEqual(el_result, 'Groucho')
        el_result = ch3_pyfilling.get_list_item_via_offset(-3)
        self.assertEqual(el_result, 'Groucho')
        el_result = ch3_pyfilling.get_list_item_via_offset(1)
        self.assertEqual(el_result, 'Chico')
        el_result = ch3_pyfilling.get_list_item_via_offset(-2)
        self.assertEqual(el_result, 'Chico')
        el_result = ch3_pyfilling.get_list_item_via_offset(2)
        self.assertEqual(el_result, 'Harpo')
        el_result = ch3_pyfilling.get_list_item_via_offset(-1)
        self.assertEqual(el_result, 'Harpo')

    # Lists of Lists
    def test_get_list(self):
        """ See title """
        item_1 = ['a']
        gl_result = ch3_pyfilling.get_list(0)
        self.assertEqual(gl_result, item_1)

    def test_get_list_inside_list(self):
        """ See title """
        gi_result = ch3_pyfilling.get_list_inside_list(1, 0)
        self.assertEqual(gi_result, 'b')
        gi_result = ch3_pyfilling.get_list_inside_list(1, 1)
        self.assertEqual(gi_result, 'c')

    # Change an Item by [offset]
    def test_change_list(self):
        """ See title """
        cl_result = ch3_pyfilling.change_list('b')
        self.assertEqual(cl_result, 'b')

    # Get a Slice to Extract Items by Offset Range
    def test_get_list_slice(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        my_list = ch3_pyfilling.get_list_slice(0, 2)
        self.assertEqual(my_list, ['Groucho', 'Chico'])
        self.assertEqual(marxes[1:3], ['Chico', 'Harpo'])
        self.assertEqual(marxes[0:-2], ['Groucho'])
        # why marxes[2:0] returns [] != 'Harpo' is a mystery TBD
        self.assertEqual(marxes[2:], ['Harpo'])

    # Add item to end with append()
    def test_append_list(self):
        """ See title """
        marxes_local = ['Groucho', 'Chico', 'Harpo']
        # Holy horseradish Batman!  Updating marxes_local updates marxes
        # marxes = marxes_local
        marxes = list(marxes_local)  # this does copy to new instance
        to_be_added = ['Zeppo']
        marxes_local.append(to_be_added)
        ch3_pyfilling.append_list(marxes, to_be_added)
        self.assertEqual(marxes, marxes_local)

    def test_combine_lists(self):
        """ See title """
        marxes_local = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        to_be_added = ["Gummo"]
        marxes_local += to_be_added
        ch3_pyfilling.combine_list(marxes, to_be_added)
        self.assertEqual(marxes, marxes_local)

    def test_insert_list(self):
        """ See title """
        marxes_local = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        where_be_added = 1
        marxes_local.insert(where_be_added, 'Karl')
        ch3_pyfilling.insert_list(marxes, where_be_added, 'Karl')
        self.assertEqual(marxes, marxes_local)

    def test_delete_item_from_list(self):
        """ See title """
        marxes_local = ['Groucho', 'Karl', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        del marxes_local[1]
        ch3_pyfilling.delete_item_from_list(marxes, 1)
        self.assertEqual(marxes, marxes_local)

    def test_delete_list_item_by_value(self):
        """ See title """
        marxes_local = ['Groucho', 'Karl', 'Chico', 'Harpo', 'Zeppo']
        marxes = list(marxes_local)  # this does a copy to new instance
        marxes_local.remove('Karl')
        ch3_pyfilling.delete_list_item_by_value(marxes, 'Karl')
        self.assertEqual(marxes, marxes_local)

    def test_pop_item(self):
        """ See title """
        marxes = ['Groucho', 'Karl', 'Chico', 'Harpo', 'Zeppo']
        marxes_local = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        index_to_pop = 1
        ch3_pyfilling.pop_item(marxes, index_to_pop)
        self.assertEqual(marxes, marxes_local)

    def test_find_list_offset(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        fl_result = ch3_pyfilling.find_list_offset(marxes, 'Harpo')
        self.assertEqual(fl_result, 2)

    def test_in_list(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
        in_result = ch3_pyfilling.in_list(marxes, 'Harpo')
        self.assertEqual(in_result, True)
        in_result = ch3_pyfilling.in_list(marxes, 'ZHarpo')
        self.assertEqual(in_result, False)
        in_result = ch3_pyfilling.in_list(marxes, 'Harp')
        self.assertEqual(in_result, False)

    def test_count_items_in_list(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        ci_result = ch3_pyfilling.count_items_in_list(marxes, 'Harpo')
        self.assertEqual(ci_result, 1)
        ci_result = ch3_pyfilling.count_items_in_list(marxes, 'Bob')
        self.assertEqual(ci_result, 0)

    def test_join_and_split_1ist(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        separator = ' * '
        ci_result = ch3_pyfilling.join_and_split_1ist(marxes, separator)
        local_join = separator.join(marxes)
        self.assertEqual(ci_result, local_join)

    def test_join_and_split_list_2(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        separator = " * "
        local_join = separator.join(marxes)
        js_result = ch3_pyfilling.join_and_split_list_2(local_join, separator)
        self.assertEqual(js_result, marxes)

    def test_sorted_list(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        sorted_marxes = ['Chico', 'Groucho', 'Harpo']
        sl_result = ch3_pyfilling.sorted_list(marxes)
        self.assertEqual(sl_result, sorted_marxes)

    def test_sort_list(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        so_result = ch3_pyfilling.sort_list(marxes)
        marxes.sort()
        self.assertEqual(so_result, marxes)

    def test_len_list(self):
        """ See title """
        marxes = ['Groucho', 'Chico', 'Harpo']
        ll_result = ch3_pyfilling.len_list(marxes)
        self.assertEqual(ll_result, 3)

    def test_copy_list_slice(self):
        """ See title """
        my_list = [1, 2, 3]
        cl_result = ch3_pyfilling.copy_list_slice(my_list)
        self.assertEqual(cl_result, ['firstSurprise', 2, 3])
        # Next two lines are correct according to Introducing Python, pg 53
        #   but they fail when run
        #        cl_result = ch3_pyfilling.copy_list_slice_copy(my_list)
        #        self.assertEqual(cl_result, [1, 2, 3])  # new_list unchanged
        cl_result = ch3_pyfilling.copy_list_slice_list(my_list)
        self.assertEqual(cl_result, ['surprise', 2, 3])
        cl_result = ch3_pyfilling.copy_list_slice_slice(my_list)
        self.assertEqual(cl_result, ['differentSurprise', 2, 3])


if __name__ == '__main__':
    unittest.main()
