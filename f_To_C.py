"""Module docstring goes here."""
from __future__ import print_function

F_BOIL_TEMP = 212.0
F_FREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RANGE = F_BOIL_TEMP - F_FREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE / F_RANGE


def f_to_c(f_param):
    "Convert Fahrenheit temp <f_param> to Celsius and return it."
    c_param = (f_param - F_FREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_param


if __name__ == '__main__':
    for f_temp in [-40.0, 32.0, 212.0]:
        c_temp = f_to_c(f_temp)
        print('%f F => %f C' % (f_temp, c_temp))
