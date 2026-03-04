# if  statement
age = 21

if(age > 18):
    print ("You are an adult")
    print ("You can vote")


# if - elif
    # elif can be written multiple times
    # else 
    # we write else only one like default output if every condition is wrong 
light = "green"

if (light == "red"):
    print ("Stop") #identation 
elif (light == "yellow"):
    print ("wait")
elif (light == "green"):
    print("Go")
else :
    print ("our light is broken")

# nested if 
your_age = 24

if ( your_age >= 18):
    if ( your_age >= 80):
        print ("You cannot drive")
    else:
        print("You can Drive")
else:
    print("You cannot drive")