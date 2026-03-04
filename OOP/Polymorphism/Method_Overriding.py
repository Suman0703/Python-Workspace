# Child class changes the parent class method.

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")   # overriding parent method

c = Child()
c.show()
