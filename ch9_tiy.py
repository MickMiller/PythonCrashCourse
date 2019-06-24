""" File: ch9_tiy.py Purpose: Try It Yourself exercises """


def restaurant_describe_09_01(restaurant):
    """ Code that returns restaurant description """
    ret_val = (restaurant.restaurant_name_get() + ", " +
               restaurant.restaurant_describe())
    return ret_val


def restaurant_name_get_09_01(restaurant):
    """ Code that returns restaurant description """
    ret_val = restaurant.restaurant_name_get()
    return ret_val


def restaurant_open_09_01(restaurant):
    """ Code that returns restaurant description """
    ret_val = restaurant.restaurant_open()
    return ret_val


def user_describe_09_03(restaurant):
    """ See title """
    ret_val = restaurant.user_describe()
    return ret_val


def user_greet_09_03(restaurant):
    """ See title """
    ret_val = restaurant.user_greet()
    return ret_val


def patron_served_09_04(restaurant):
    """ See title """
    ret_val = restaurant.restaurant_patron_get()
    return ret_val


def login_get_09_05(user):
    """ See title """
    ret_val = user.login_attempt
    return ret_val


def login_inc_09_05(user):
    """ See title """
    user.login_attempt += 1
    ret_val = user.login_attempt
    return ret_val


def login_reset_09_05(user):
    """ See title """
    user.login_attempt = 0
    ret_val = user.login_attempt
    return ret_val


def flavor_ret_09_06(user):
    """ See title """
    ret_val = user.ice_cream_stand.flavor_list()
    return ret_val


def privileges_09_08(user):
    """ See title """
    ret_val = user.admin.privileges.privileges_show()
    return ret_val


def electric_car(car):
    """ See title """
    ret_val = car.make + ", " + car.model + ", " + str(car.year) + ", " + \
        str(car.battery.battery_size)
    return ret_val


def describe_battery(car):
    """ See title """
    battery_size = car.battery.battery_size
    battery_range = car.battery.battery_range
    ret_val = "Battery size: " + str(battery_size) +\
              ", range: " + str(battery_range)
    return ret_val


def fill_gas_tank_09_09(car):
    """ See title """
    ret_val = car.battery.fill_gas_tank()
    return ret_val


def battery_upgrade_09_09(car):
    """ See title """
    if car.battery.battery_size < 85:
        car.battery.battery_size = 85
    return car.battery.battery_size
