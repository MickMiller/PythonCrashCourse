"""
File: ch3_pyfilling.py
Purpose: Examples of running code for headers in Introducing Python Ch 3

"""


def empty_list_creation():
    """ Function that creates empty list """
    empty_list = []
    return empty_list


def empty_list_creation_2():
    """ Function that creates empty list """
    another_empty_list = list()
    return another_empty_list


def create_list_other_types(input_string):
    """ Convert from string to list """
    local_list = list(input_string)
    return local_list


def get_list_item_via_offset(my_offset):
    """ docstring exists so no missing-docstring Missing class msg """
    marxes = ['Groucho', 'Chico', 'Harpo']
    choice = marxes[my_offset]
    return choice


def get_list(offset_1):
    """ docstring exists so no missing-docstring Missing class msg """
    item_1 = ['a']
    item_2 = ['b', 'c']
    item_all = [item_1, item_2]
    choice = item_all[offset_1]
    return choice


def get_list_inside_list(offset_1, offset_2):
    """ docstring exists so no missing-docstring Missing class msg """
    item_1 = ['a']
    item_2 = ['b', 'c']
    item_all = [item_1, item_2]
    choice = item_all[offset_1][offset_2]
    return choice


def change_list(new_item):
    """ docstring exists so no missing-docstring Missing class msg """
    item_1 = ['a']
    item_1 = new_item
    return item_1


def get_list_slice(start_slice, end_slice):
    """ docstring exists so no missing-docstring Missing class msg """
    marxes = ['Groucho', 'Chico', 'Harpo']
    return marxes[start_slice:end_slice]


def append_list(list_local, add_to_list):
    """ docstring exists so no missing-docstring Missing class msg """
    list_local.append(add_to_list)
    return list_local


def combine_list(list_local, to_be_added):
    """ docstring exists so no missing-docstring Missing class msg """
    list_local.extend(to_be_added)
    return list_local


def insert_list(list_local, where_be_added, to_be_added):
    """ docstring exists so no missing-docstring Missing class msg """
    list_local.insert(where_be_added, to_be_added)
    return list_local


def delete_item_from_list(list_local, where_to_delete):
    """ docstring exists so no missing-docstring Missing class msg """
    del list_local[where_to_delete]
    return list_local


def delete_list_item_by_value(list_local, name_to_delete):
    """ docstring exists so no missing-docstring Missing class msg """
    list_local.remove(name_to_delete)
    return list_local


def pop_item(list_local, index_to_pop):
    """ docstring exists so no missing-docstring Missing class msg """
    list_local.pop(index_to_pop)
    return list_local


def find_list_offset(list_local, item_to_find):
    """ docstring exists so no missing-docstring Missing class msg """
    return list_local.index(item_to_find)


def in_list(list_local, is_item_in_list):
    """ docstring exists so no missing-docstring Missing class msg """
    return is_item_in_list in list_local


def count_items_in_list(my_list, item):
    """ docstring exists so no missing-docstring Missing class msg """
    return my_list.count(item)


def join_and_split_1ist(list_local, seperator):
    """ docstring exists so no missing-docstring Missing class msg """
    joined = seperator.join(list_local)
    return joined


def join_and_split_list_2(list_local, seperator):
    """ docstring exists so no missing-docstring Missing class msg """
    seperated = list_local.split(seperator)
    return seperated


def sorted_list(list_local):
    """ docstring exists so no missing-docstring Missing class msg """
    return sorted(list_local)


def sort_list(list_local):
    """ docstring exists so no missing-docstring Missing class msg """
    list_local.sort()
    return list_local


def len_list(local_list):
    """ docstring exists so no missing-docstring Missing class msg """
    return len(local_list)


def copy_list_slice(my_list):
    """ docstring exists so no missing-docstring Missing class msg """
    new_list = my_list  # both my_list and new_list refer to same object
    my_list[0] = 'firstSurprise'
    return new_list


def copy_list_slice_copy(my_list):
    """ docstring exists so no missing-docstring Missing class msg """
    new_list = my_list.copy()  # new_list is copy of my_list
    my_list[0] = 'firstSurprise'
    return new_list


def copy_list_slice_list(my_list):
    """ docstring exists so no missing-docstring Missing class msg """
    new_list = list(my_list)
    new_list[0] = "surprise"
    return new_list


def copy_list_slice_slice(my_list):
    """ docstring exists so no missing-docstring Missing class msg """
    new_list = my_list[:]
    new_list[0] = 'differentSurprise'
    return new_list


if __name__ == '__main__':
    """ docstring exists so no missing-docstring Missing class msg """
    import doctest
    doctest.testmod()
