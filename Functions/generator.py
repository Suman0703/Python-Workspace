# Generator function is used to generate Sequence without storing all values

def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)