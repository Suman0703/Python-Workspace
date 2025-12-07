# print the multiplication table of a number n using while

n = int(input("enter value for n:"))

if (n >= 1):
    count = 1
    while count <= 10:
        print (n * count)
        count += 1
else:
    print("Enter Other value")

        
# print the elements of the following list using a loop
list = [1,2,3,9,16,25,36,49,64,81,100]

i = 0
while i <= len(list):
    print(list[i])
    i += 1
    