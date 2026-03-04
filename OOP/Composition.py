# Composition means one class contains another class as a PART of itself.
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def start_car(self):
        self.engine.start()      # using Engine's method
        print("Car is running")

c = Car()
c.start_car()
