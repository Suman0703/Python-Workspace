# Recursion = When a functions calls itself repeatedly

# prints n to 1 backwards
def show(n):
    if(n==0): #Base Case
        return
    print(n)
    show(n-1) # Call Stack

show(7)

# Factorial of num
def fact(num):
    if( num == 0 or num == 1):
        return 1
    else:
        return fact(num-1)*num

print(fact(9))