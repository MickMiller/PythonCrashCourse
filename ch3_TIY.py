"""
File: ch3_tiy.py
Purpose: Try It Yourself exercises 3-1 to 3-10

"""


def names_3_1(fl_index):
    """ Function that creates and prints list """
    friend_list = ["Moe", "Larry", "Curley", "Shemp"]
    return friend_list[fl_index]


def greetings_3_2(fl_index):
    """ Function that creates and prints list with common text list """
    friend_list = ["Moe", "Larry", "Curley", "Shemp"]
    m_print_1 = "Greetings, "
    m_print_2 = " Uncle Sam would like you to travel the world."
    m_print_msg = m_print_1 + friend_list[fl_index] + m_print_2
    return m_print_msg


def fav_transportation_3_3(fl_index):
    """ Creates and prints list with favorite modes of transport """
    friend_list = ["Car", "foot", "Segway"]
    m_print_1 = "I like to get places using "
    m_print_2 = " to travel the world."
    m_print_msg = m_print_1 + friend_list[fl_index] + m_print_2
    return m_print_msg


def dinner_guest_3_4(fl_index):
    """ Creates and prints list with favorite modes of transport """
    guest_list = ["Larry da Vinci", "Ben Franklin", "Genghis Khan"]
    m_print_1 = "Dear "
    m_print_2 = " could you attend a BBQ at my house on 4 July 2019."
    m_print_msg = m_print_1 + guest_list[fl_index] + m_print_2
    return m_print_msg


def dinner_guest_3_5(guest_num, attend_or_not):
    """ Creates and prints guest with possible changes """
    guest_list = \
        ["Larry da Vinci", "Ben Franklin", "Genghis Khan"]
    m_print_t = "Who can attend:"
    m_print_f = "Who can not attend:"
    #
    if attend_or_not == "T":
        guest_list[2] = "Hellen Keller"
        m_print_msg = m_print_t + guest_list[guest_num]
        print(m_print_msg)
    else:
        m_print_msg = m_print_f + guest_list[guest_num]
        print(m_print_msg)
    #
    return m_print_msg


def dinner_guest_3_6():
    """ Creates and prints guest with possible changes """
    guest_list = \
        ["Larry da Vinci", "Ben Franklin", "Hellen Keller"]
    guest_list.insert(0, "Al Einstein")
    guest_list.insert(2, "Prof Uncle Eric")
    guest_list.append("Dear Old Dad")
    m_print_0 = "A bigger table was found!  Here are all the guests:"
    #
    # Print all invitations via a loop
    m_print_msg = m_print_0 + "\n" + str(guest_list)
    print(m_print_msg)
    #
    return m_print_msg


def dinner_guest_3_7():
    """ Creates and prints guest with possible changes """
    guest_list = \
        ["Larry da Vinci", "Ben Franklin", "Hellen Keller"]
    guest_list.insert(0, "Al Einstein")
    guest_list.insert(2, "Prof Uncle Eric")
    guest_list.append(" Dear Old Dad")
    m_print_0 = "Sorry only 2 guests."
    #
    # Remove guests
    guest_list.pop(0)
    guest_list.pop(0)
    guest_list.pop(0)
    guest_list.pop(0)
    # Print all invitations via a loop
    m_print_0 = "Remaining guests are:"
    m_print_msg = m_print_0 + "\n" + str(guest_list)
    print(m_print_msg)
    #
    guest_list.pop(0)
    guest_list.pop(0)
    print("Guest list", guest_list)
    #
    m_print_msg = str(guest_list)
    return(m_print_msg)


def seeing_world_3_8():
    """ World sites to see
    three lists:
    1) world_list - starting list
    2) temp_list - used for clarity - visibility into process
    3) list_to_verify - as development proceeds this list grows,
       typically temp_list is correct then appended to this list """

    world_list = \
        ["Frankfort", "Richmond", "Joisey", "Normandy", "Auschwitz"]
    list_to_verify = world_list[:]
    #
    # Print original list in original order
    print("List in original order:", world_list)
    #
    # Change order of list via sorted and show original list unchanged
    list_to_print = sorted(world_list)
    print("List in alphabetical order:", list_to_print)
    list_to_verify.append(list_to_print)
    #
    # Show original list unchanged
    print("Original order preserved 1:", world_list)
    #
    # Reverse order of list via sorted and show original list unchanged
    temp_list = sorted(world_list)
    temp_list = sorted(temp_list, reverse=True)
    print("List in reverse alphabetical order:", temp_list)
    list_to_verify.append(temp_list)
    print("In ch3_TIY list_to_verify:", list_to_verify)
    print("Original order preserved_2:", world_list)
    #
    #
    # Change order of list via reverse() and show original list changed
    temp_list = world_list[:]
    temp_list.reverse()
    print("List reversed AND list changed:", temp_list)
    list_to_verify.append(temp_list)
    #
    # Change order of list via reverse() and show back to original list
    temp_list.reverse()
    print("List reversed back to original AND list changed:", temp_list)
    list_to_verify.append(temp_list)
    #
    # Change list to alphabetical order via sort & show order has changed
    temp_list = world_list[:]  # Copy w_l to n_l
    temp_list.sort()
    print("List:", temp_list)
    list_to_verify.append(temp_list)
    #
    # List to reverse alphabetical order via sort & show order has changed
    temp_list.sort(reverse=True)
    list_to_verify.append(temp_list)
    print("List reversed and changed via sort")
    print("In ch3_TIY list_to_verify:", list_to_verify)
    return(list_to_verify)


def dinner_guest_3_9():
    """ Returns dinner guests """
    guest_list = ["Larry da Vinci", "Ben Franklin", "Genghis Khan"]
    return len(guest_list)


def show_items_in_list_3_10(param_1):
    """ See title
    14 commands tested.  Form of all tests:
    - show BEFORE
    - document HOW
    - show AFTER
    - return results
    """
    original_list = ["Teach Python", "Build boxes", "Create workshop"]
    # Show items in list (first, last and in-between)
    ret_value = original_list[param_1]
    return ret_value


def change_list_3_10(list_itself, list_index, list_element):
    """ See title   """
    # Change items in list (first, last and in-between)
    list_itself[list_index] = list_element
    return list_itself


def insert_in_list_3_10(list_itself, list_index, list_element):
    """ See title   """
    # Insert item into list
    list_itself.insert(list_index, list_element)
    return list_itself


def del_from_list_3_10(list_itself, list_index):
    """ See title   """
    # Delete from list
    del list_itself[list_index]
    return list_itself


def remove_by_value_3_10(list_itself, list_value):
    """ See title   """
    # Delete from list
    list_itself.remove(list_value)
    return list_itself


def remove_by_label_3_10(list_itself, list_value):
    """ See title   """
    # Delete from list
    list_itself.remove(list_value)
    return list_itself


def remove_by_pop_3_10(list_itself, list_value):
    """ See title   """
    # Delete from list
    list_itself.pop(list_value)
    return list_itself


def len_3_10(list_itself):
    """ See title   """
    return len(list_itself)


def sort_list_unchanged_3_10(list_itself):
    """ See title   """
    sorted(list_itself)
    return list_itself


def sort_list_changed_3_10(list_itself):
    """ See title   """
    list_itself.sort()
    return list_itself


def append_3_10(list_itself, element_to_add):
    """ See title     """
    list_itself.append(element_to_add)
    return list_itself


def reverse_3_10(list_itself):
    """ See title   """
    list_itself.reverse()
    return list_itself


def sort_list_reverse_3_10(list_itself):
    """ See title   """
    list_itself.sort(reverse=True)
    return list_itself
