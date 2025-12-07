# two string values 

data = input(("Enter two Values:")).split()
print(data)

# two integer values
# a,b = input("Enter Two numbers:").split()
# a = int(a)
# b = int(b)
# print(a + b)

# three integer values
a,b,c = input("Enter Three numbers:").split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)

# multiple int values using map()
x,y,z = map(int, input("Enter Three input Values:").split())
print("Total:", x + y + z)

# taking multiple float values 
p,q,r = map (float, input("Enter three float values").split())
print("Total:", p + q + r)

# taking strings 
name , city , branch = map(str, input("Enter your name,city and branch: ").split())
print(name , city , branch)

# Taking input in list
numbers = list(map(int, input("Enter numbers input Values:").split()))
print (numbers)