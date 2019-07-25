""" A set of classes that can be used to represent electric cars. """


from oodemo_class_car import Car


class ElectricCar(Car):  # Car is parent class
    """ Models aspects of a car, specific to electric vehicles. """

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()  # battery instance assigned to this class

    def class_fill_gas_tank(self):
        """ See title. """
        return "Can't fill gas tank of electric car!"


class Battery():
    """ A simple attempt to model a battery for an electric car. """

    def __init__(self, battery_size=60):
        """ Initialize the batteery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        # print("This car has a " + str(self.battery_size) + "-kWh battery.")
        return("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """ Print a statement about the range this battery provides. """
        if self.battery_size == 60:
            car_range = 140
        elif self.battery_size == 85:
            car_range = 185

        message = "This car can go approximately " + str(car_range)
        message += " miles on a full charge."
        print(message)
