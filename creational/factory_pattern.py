# Factory pattern is a creational design patterns
# that provides an interface for creating objects in a superclass,
# but allows a subclass to alter the type of the created object.
import abc


class Transportation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    def print_(self):
        print self.name


class Ship(Transportation):
    def __init__(self):
        pass

    def get(self):
        return Ship()

    @property
    def name(self):
        return "SHIP"


class Truck(Transportation):
    def __init__(self):
        pass

    def get(self):
        return Truck()

    @property
    def name(self):
        return "TRUCK"


truck = Truck()
ship = Ship()

transportations = [truck, ship]

for transportation in transportations:
    transportation.print_()
