'''A destructor is a special method in Python that is automatically called when an object is deleted or goes out of memory.'''

# def __del__(self):  it is a destructor method

class Demo:
    def __init__(self):
        print("Object is created")

    def __del__(self):
        print("Object is destroyed")

# create object
d = Demo()

# delete object manually
del d
