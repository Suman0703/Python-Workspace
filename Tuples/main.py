# Tuples allow us to create immutable sequence of values

tup = (1,2,3,4,5,6,3,3)
print(tup)
print(type(tup))

t = (9,)
print(t)

# Tuple packing
data = 10, 20, 30
print(data)
print(type(data))

# Tuple unpacking 
dat = (1, 2, 3)
a, b, c = dat
print(a)
print(b)
print(c)

# Tuple methods

print(tup.index(6)) # returns index of first occurrence

print(tup.count(3)) # count total occurrences