# Set is collection of unordered items
# each collection in the set must be unique and immutable but 
# set itself is a mutable i.e we can add and remove new elements but cannot change the elements values 
# sets do no store lists and dict
# set ignore dublicate values

collection = {1,2,3,3,3,4,5,"hello","green",True}
set1 = { 1,2,3,"mango", "apple"}

print(collection)

#empty set 
collection1 = set()

# Set methods
collection.add("Suman") #adds an element
collection.add((1,2,3,4))
print(collection)

collection.remove("Suman") #removes the element
print(collection)

collection.pop() #Removes a random value 
print(collection)

print(collection.union(set1)) #combines both set values and return new 

print(collection.intersection(set1)) #combines common values and return new

collection.clear() #empties the set
print(collection)