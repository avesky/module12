"""
Program: abstract_class.py
Author: Andy Volesky
Last date modified: 11/17/2021

The purpose of this program:

Write an abstract class Rider with ride and riders abstract methods. Write subclasses Bicycle, Motorcycle, Car that implement (override) the abstract methods.
Include your driver code. Create on object of each Bicycle, Motorcycle and Car. Call the methods for each.
Sample output could include:
Human powered, not enclosed
1 or 2 if tandem or a daredevil
Engine powered, not enclosed
1 or 2
Engine powered, enclosed
1 plus comfortably

"""

from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass
    def riders(self):
        pass

class Bicycle(Rider):
    def __init__(self, power, enclosed, num_riders):
        self.power = power
        self.enclosed = enclosed
        self.num_riders = num_riders

    # overrides abstract method with implementation
    def ride(self):
        return str(self.power) + ", " + str(self.enclosed)

    def riders(self):
        return str(self.num_riders)

    def __str__(self):
        return str(self.ride())

class Motorcycle(Rider):
    def __init__(self, power, enclosed, num_riders):
        self.power = power
        self.enclosed = enclosed
        self.num_riders = num_riders

    # overrides abstract method with implementation
    def ride(self):
        return str(self.power) + ", " + str(self.enclosed)

    def riders(self):
        return str(self.num_riders)

    def __str__(self):
        return str(self.ride())
class Car(Rider):
    def __init__(self, power, enclosed, num_riders):
        self.power = power
        self.enclosed = enclosed
        self.num_riders = num_riders

    # overrides abstract method with implementation
    def ride(self):
        return str(self.power) + ", " + str(self.enclosed)

    def riders(self):
        return str(self.num_riders)

    def __str__(self):
        return str(self.ride())


rider1 = Bicycle('human powered', 'not enclosed', '1 not tandem')
print(rider1.ride())
print(rider1.riders())
rider2 = Motorcycle('engine powered', 'not enclosed', '1 not tandem')
print(rider2.ride())
print(rider2.riders())
rider3 = Car('engine powered', 'enclosed', '1-4 riders')
print(rider3.ride())
print(rider3.riders())