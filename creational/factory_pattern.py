import abc


class Transportation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass

    def create(self):
        print self.get().name


class Ship(Transportation):
    def __init__(self):
        self.name = "SHIP"

    def get(self):
        return Ship()


class Truck(Transportation):
    def __init__(self):
        self.name = "TRUCK"

    def get(self):
        return Truck()


truck = Truck()
ship = Ship()

transportation = [truck, ship]

for trans in transportation:
    trans.create()
