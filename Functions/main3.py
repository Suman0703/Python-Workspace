# variable length arguments 

def total(*nums):
    print(sum(nums)) # sum built in function

total(10,80)
total(90,7,8,7)

# Keyword Variable arguments
def info(**data):
    print(data)

info(name = "suman", age="19",Branch = "CSE")