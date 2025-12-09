# Same function name, but different behavior depending on the object.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

# Same function name but different behavior
for animal in (Dog(), Cat()):
    animal.sound()
