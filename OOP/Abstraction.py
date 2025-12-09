# hiding the unnecessary details

from abc import ABC, abstractmethod

class Animal(ABC):         # abstract class
    @abstractmethod
    def sound(self):       # abstract method
        pass               # no details here (hidden)


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Using objects
d = Dog()
c = Cat()

d.sound()
c.sound()
