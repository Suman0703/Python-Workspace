'''Creates student class that takes name & marks of # subjects as arguments in constructor.then create a method to print the average'''

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average score is", sum/3)


s1 = student("Suman",[89,90,91])
s1.get_avg()

s1.name = "Raman" # chnaging attributes values directly