# Break = used to terminate the loop when encountered
# continue = terminate the execution in the current iteration and continues execution of the loop with the next iteration


# search for a number x in this tuple using loop 

tuple  = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter the number that you want to find:"))

i = 0
while i <= len(tuple):
    i += 1
    if(x == tuple[i]):
        print("Found at index",i)
        break
print("End of loop")

# continue 
j = 0
while j <= 5:
    if(j == 3):
        j += 1
        continue
    print(j)
    j += 1 