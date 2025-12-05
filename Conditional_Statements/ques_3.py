# WAP a program to check if a number is a multiple of 7 or not 

x = int (input ("Enter your number:"))

remainder = x % 7

if (remainder == 0):
    print ("Number is a multiple of 7")
else:
    print("number is not a multiple of 7 ")