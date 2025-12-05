# lists are mutable i.e we can updates values 
# we can store multiple types of data in a list

marks = [ 98.4,89,67,56,90]
print(marks)
print(type(marks))
print (marks [0]) # output = 98.4

marks[1] = 78
print(marks)

# list slicing
print(marks[0 : 3])

# negative 
print(marks[-4 : -1])

# list Methods 
list = [1,2,3]

list.append(4)# adds one element at the end
print(list)

list.sort() # Sort list in ascending order
print(list)

list.sort(reverse=True) # Sort in decending order
print(list)

list.reverse()# reverse list
print(list)

list.insert(4,7) # insert element at index
print(list)

list.remove(1) #Remove first occurrence of the element
print(list)

list.pop(3) #Remove element at idx
print(list)