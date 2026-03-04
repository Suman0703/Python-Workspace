# WAPP to check if a list contains a palindrome of elements 
# copy method used create shallow copy of the list 

print ("Enter elements for your list")

x = input("enter first element:")
y = input ("enter Second element:")
z = input ("enter third element:")

list1 =[]
list1.append(x)
list1.append(y)
list1.append(z)

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palindrom List")
else:
    print("Not a palindrom")

