''' Method Overloading means having multiple methods with the same name but different parameters. In languages like Java and C++, this is allowed directly. But in Python, true method overloading is NOT supported.'''

# Example of Method Overloading Using Default Arguments

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(5))         # one argument
print(obj.add(5, 10))     # two arguments
print(obj.add(5, 10, 15)) # three arguments
