class Student:
    def __init__(self, name):
        self.name = name  # object attribute

    def show_name(self):  # method
        print("My name is", self.name)


s1 = Student("Suman")
s1.show_name()
