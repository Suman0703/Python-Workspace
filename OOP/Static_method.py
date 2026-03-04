class Person:
    @staticmethod
    def greet(): # no self argument needed
        print("Hello! This is a static method.")
        
Person.greet()   # No object needed


# Another example
class Math:
    @staticmethod
    def add(a, b):   # no self, no cls
        return a + b


# Call without creating object
print(Math.add(5, 3))
