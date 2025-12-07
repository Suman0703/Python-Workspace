# WAP to find the number x in a tuple

tuple  = (1,4,9,16,25,36,49,64,81,100,4)

x = int(input("Enter the number that you want to find:"))

i = 0
for el in tuple:
    if(el == x):
        print("number found at index",i)
        # break
    i += 1
    