# Grandparent → Parent → Child
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

c = C()
c.showA()
c.showB()
c.showC()
