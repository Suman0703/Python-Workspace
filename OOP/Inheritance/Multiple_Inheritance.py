# Two parents → One child

class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):   # inherits from both A and B
    def showC(self):
        print("Class C")

c = C()
c.showA()
c.showB()
c.showC()
