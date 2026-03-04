# One parent → Multiple children
class Parent:
    def showParent(self):
        print("Parent class")

class Child1(Parent):
    def showC1(self):
        print("Child 1")

class Child2(Parent):
    def showC2(self):
        print("Child 2")

c1 = Child1()
c2 = Child2()

c1.showParent()
c2.showParent()
