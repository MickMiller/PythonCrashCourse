"""
File: ch7_tiy.py
Purpose: Try It Yourself exercises ch7

"""


def greeter():
    """ Implementation of pg 118 function to validate Ch 7 ready to roll """
    name = input("Kindly enter \"your name\": ")
    print("Hello " + name)
    if name != "your name":
        print("You didn't enter \"your name\" so I'll enter it for you")
        return "your name"

    return name
