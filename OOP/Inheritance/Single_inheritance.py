class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):   # inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()
