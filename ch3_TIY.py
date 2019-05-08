"""
File: ch3_TIY.py
Purpose: Try It Yourself exercises 3-1 to 3-10

"""


def names_3_1(fl_index):
    """ Function that creates empty list """
    friend_list = ["Moe", "Larry", "Curley", "Shemp"]
    print(friend_list[fl_index])
    return friend_list[fl_index]


def greetings_3_2(fl_index):
    """ Function that creates empty list """
    friend_list = ["Moe", "Larry", "Curley", "Shemp"]
    m_print_1 = "Greetings, "
    m_print_2 = " Uncle Sam would like you to travel the world."
    m_print_msg = m_print_1 + friend_list[fl_index] + m_print_2
    print(m_print_msg)
    return m_print_msg
