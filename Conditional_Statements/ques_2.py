# WAP to find the greatest of 3 numbers entered by the user 

x = int (input ("Enter value of First number x:"))
y = int (input ("Enter value of Second number y:"))
z = int (input ("Enter value of Third number z:"))

if (x > y and x > z):
    print("x is greater it has value:",x)
elif (y >x and y > z):
    print ("y is greate it has value:",y)
else:
    print ("z is greater it has value",z) 