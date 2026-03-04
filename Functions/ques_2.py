# WAP to print the length of a list 
name = list(map(str, input("Enter numbers input Values:").split()))
print (name)

def print_len(name):
    print(len(name))

print_len(name)

#WAP to print the elements of a list in a single line

def print_lis(name):
    for ele in name:
        print(ele,end=" ")

print_lis(name)