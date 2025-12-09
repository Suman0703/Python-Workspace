# When we want to work with class-level data

class Student:
    school = "ABC School"   # class variable

    @classmethod
    def get_school(cls):    # class method
        return cls.school


print(Student.get_school())
