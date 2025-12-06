# functions are the block of code that perform a specific task
# def keyword is used

def cal_sum(a,b):
    sum = a + b
    print(sum)
    return sum

cal_sum(4,6)
cal_sum(45,78)

# function without arguments
def greet():
    print("Hello,Welcome to my code")

greet()

output = greet()
print(output) # none bcz it does not have any return value