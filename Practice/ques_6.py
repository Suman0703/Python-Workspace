# WAP to check if a number entered by a user is even or odd 

num = int (input ("Enter the value of number:"))
remainder = num % 2
if (remainder == 0):
    print ("Even")
else:
    print ("ODD") 