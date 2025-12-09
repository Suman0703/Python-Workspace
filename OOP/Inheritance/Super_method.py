# super() is used to access the parent class inside the child class.

class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        super().show()     # calling parent method
        print("This is child class")

c = Child()
c.show()
