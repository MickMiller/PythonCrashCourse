"""
File: ch4_tiy.py
Purpose: Try It Yourself exercises 3-1 to 3-13

"""


def for_example():
    """ See title """
    print("\nFOR example =======================================")
    return_list = []
    comic_list = ['Moe', 'Larry', 'Curley']
    for comic in comic_list:
        print("in for_example comic is:" + comic +
              " is one of the Three Stooges")
        return_list.append(comic)

    return return_list


def pizza_4_1():
    """ 3 parts
    1) Print list of pizza toppings
    2) Print 1 message with each topping
    3) Print 1 message at end
    """
    print("In pizza_4_1")
    pizza_toppings = ['pepperoni', 'onion', 'green pepper']
    for topping in pizza_toppings:
        print("Delicious pizza topping is:", topping)

    print("I eat lots of pizza!")
    return pizza_toppings


def count2twenty_4_3():
    """
    Use for loop to print numbers from 1 to 20 inclusive
    """
    numbers = list(range(1, 21))
    for number in numbers:
        print(number, ' ')
    return numbers


def sum_1_million_4_4():
    """
    Run min(), max() and sum() on list of a million numbers
    """
    numbers = list(range(1, 1000001))
    print("min:", min(numbers))
    print("max:", max(numbers))
    sum_numbers = sum(numbers)
    print("sum:", sum_numbers)

    return sum_numbers


def odd2twenty_4_6():
    """
        Use for loop to print every 3rd number from 1 to 30 inclusive
    """
    numbers = list(range(1, 21, 2))
    for number in numbers:
        print(number, ' ')
    return numbers


def three2thirty_4_7():
    """
        Use for loop to print every 3rd number from 1 to 30 inclusive
    """
    numbers = list(range(1, 31, 3))
    for number in numbers:
        print(number, ' ')
    return numbers


def cube1to10_4_8():
    """
    Use for loop to print cubes from 1 to 10
    """
    cubed_list = []
    for number in range(1, 11):
        number_cubed = number ** 3
        print(number_cubed, ' ')
        cubed_list.append(number_cubed)
    return cubed_list


def list_comprehension_4_9():
    """
    Use list_comprehension loop to print cubes from 1 to 10
    """
    cubed_list = [number ** 3 for number in range(1, 11)]
    print("Cubed list:", cubed_list)

    return cubed_list


def slices_4_10(slice_range_start, slice_range_end):
    """
    Use for loop to generate list of numbers from 1 to 20 inclusive.
    Use slices to:
      Print first three items in list
      Print middle three items in list
      Print last three items in list
    """
    all_numbers = list(range(1, 21))
    numbers = all_numbers[slice_range_start:slice_range_end]
    for number in numbers:
        print(number, ' ')
    return numbers
