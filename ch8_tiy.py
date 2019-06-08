""" File: ch8_tiy.py Purpose: Try It Yourself exercises """


def display_message_8_1():
    """ See title """
    print("This is intended message.")


def favorite_book_8_2(title):
    """ See title """
    print("My favorite book is " + title)

    return("My favorite book is " + title)


def keyword_arg(first, second):
    """ See title """
    print("first is: " + first + ", second is: " + second)
    return_val = first + ", " + second
    print("return_val: " + return_val)

    return(return_val)


def default_val(first='First', second='Second'):
    """ See title """
    print("first is: " + first + ", second is: " + second)
    return_val = first + ", " + second
    print("return_val: " + return_val)

    return(return_val)


def make_shirt_8_3(text='2nd', size='large'):
    """ See title """
    return_val = size + ", " + text
    print("return_val: " + return_val)

    return(return_val)


def describe_city_8_5(city, country='United States'):
    """ See title """
    return_val = city + " is in " + country
    print("return_val: " + return_val)

    return(return_val)


def optional_parameter(last_name, first_name, middle_initial="", last=0):
    """ See title"""
    if middle_initial:
        full_name = first_name + " " + middle_initial + " " + last_name
    else:
        full_name = first_name + " " + last_name + str(last)

    return full_name


def optional_parameter_2(first, second, third="", forth=0):
    """ See title"""
    ret_val = first + " " + second
    if third:
        ret_val = first + " " + second + " " + third
    if forth:
        ret_val = first + " " + second + " " + third + " " + forth

    return ret_val


def return_dictionary(first_name, last_name, age=''):
    """ See title """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person


def city_name_8_6(city, country):
    """  See title """
    return(city + ", " + country)


def greet_users(names):
    """ Print a simple greeting to each user in list """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


def show_magicians_8_9(names):
    """ Print a simple greeting to each user in list """
    #  print("RMME entering make_great_8_9 list names: " + str(names))
    for name in names:
        msg = name.title()
        print(msg)


def make_great_8_10(names):
    """ Change items in list """
    for index, name in enumerate(names):
        name = names[index]
        name = "The Great " + name
        names[index] = name


def zero_or_more_parameters(size, *toppings):
    """ Print toppings list """
    print("\nMaking a " + str(size) +
          " inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def build_profile(first, last, **user_info):
    """ Accept arbitrary number of arguments on unknown kind """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


def sandwich_8_12(*ingredients):
    """ Accept arbitrary number of ingredients """
    print("\nMaking a sandwich with the following ingredients:")
    for stuff in ingredients:
        print("- " + stuff)


def cars_8_14(make, model, **options):
    """ Print car info """
    car_dict = {}
    car_dict['make'] = make
    car_dict['model'] = model
    for key, value in options.items():
        car_dict[key] = value

    return car_dict


def import_module_name():
    """ import_module_name """
    print("import_module")
