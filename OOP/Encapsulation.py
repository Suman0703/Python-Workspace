# Encapsulation means protecting data inside a class and allowing access only through methods.

class Student:
    def __init__(self, name, marks):
        self.__name = name    # private attribute
        self.__marks = marks  # private attribute

    def show(self):           # public method to access data
        print(self.__name, self.__marks)

    def set_marks(self, new_marks):  # public method to modify data
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Marks cannot be negative!")


s = Student("Suman", 90)

s.show()          # access data safely

s.set_marks(95)   # modify data safely
s.show()
