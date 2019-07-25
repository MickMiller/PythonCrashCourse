""" File: ch10.py
   Additional methods for test_ch10
"""


def return_file(local_object):
    """ Print entire file """
    file_contents = local_object.class_return_file(local_object.file_name)
    return file_contents


def return_file_line(local_object, line_number):
    """ Print file line by line """
    line = local_object.class_return_line(line_number)
    return line


def return_file_52(local_object):
    """ Print entire file one line at a time """
    file_contents = local_object.class_return_file(local_object.file_name)
    return file_contents[:52]


def count_words(local_object):
    """ See title """
    num_words = local_object.class_count_words()
    return num_words
