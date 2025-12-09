# All classes have a function called __init()__ which is always executed when the object is being intiated

class Student:
    # default Constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, full_name , marks): # self is a by default argument
        self.name = full_name
        self.marks = marks
        print("Student names")

S1 = Student("suman" ,78) # Attributes
print(S1.name ,S1.marks)

s2 = Student("Simran",89)
print(s2.name ,s2.marks)