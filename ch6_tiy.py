"""
File: ch6_tiy.py
Purpose: Try It Yourself exercises ch6

"""


def person_6_1():
    """ See title """
    jerry_1 = {
        'first_name': 'Jerry',
        'last_name': 'Miller',
        'age': "27",
        'city': "North Chelmsford",
    }
    print('Dictionary jerry_1:', jerry_1)

    return jerry_1


def example(car_type):
    """ See title """
    print("\nCh5 example ============================================")
    if car_type == 'bmw':
        return_car = car_type.upper()
#        print("In ch5_tiy car is:", return_car)
    else:
        return_car = car_type.title()
#        print("In ch5_tiy car is:", return_car)

    return return_car


def if_5_5(alien_color):
    """ if and elif use"""
    print("if_5_5 example ===========================================")
    if alien_color == 'green':
        print("You have earned 5 points")
    elif alien_color == 'yellow':
        print("You have earned 10 points")
    elif alien_color == 'red':
        print("You have earned 15 points")
    else:
        print("In test_if_5_5 there is something seriously wrong")

    return alien_color


def if_5_8():
    """ Hello Admin """
    print("if_5_8 example ===========================================")
    user_list = ('admin', 'Eric', 'Mr. Jones', 'Terry')
    user = user_list[0]  # aka admin
#    user_list = ()  # uncomment to test empty list
    if user_list:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a report?")
        elif user == 'Eric':
            print("Hello " + user + ", welcome back!")
        else:
            print("Hello " + user + ", we don't know who you are FROWN")
    else:
        print("We need to find some users!")

    return user
