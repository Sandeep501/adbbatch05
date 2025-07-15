# abstract class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def move(self):
        pass
    
class Car(Vehicle):
    def start(self):
        return "Car engine started"

class Bike(Vehicle):
    def start(self):
        return "Bike engine started"
    
    def move(self):
        return "Bike started moving"

car = Car()
bike = Bike()

print(car.start())
print(bike.move())


    