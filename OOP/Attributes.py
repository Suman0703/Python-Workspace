class Student:
    # obj attributes > class attribute
    # CLASS ATTRIBUTE (same for all students)
    school = "Public School"

    def __init__(self, name, marks):
        # OBJECT ATTRIBUTES (different for each student)
        self.name = name
        self.marks = marks


# Creating objects
s1 = Student("Suman", 90)
s2 = Student("Samriti", 85)

# Accessing class attribute
print(s1.school)  
print(s2.school)  

# Accessing object attributes
print(s1.name, s1.marks)  
print(s2.name, s2.marks)  
