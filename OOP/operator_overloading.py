''' Using the same operator (+, -, , ==, >, etc.) to perform different actions depending on the objects involved.'''

class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
