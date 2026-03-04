# WAP a program to find the average of three numbers

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

def aver(a,b,c):
    if(a==0 or b==0 or c==0 ):
        print("Enter another value instead of 0")
    else:
     total = a+b+c
     average = total/3
     print(average)

aver(a,b,c) 