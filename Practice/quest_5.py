# WAP to give grades based on their marks 

marks = int (input ( "Enter your marks:"))

if(marks >= 90):
    print ("Grade A+")
elif(marks > 80):
    print ("Grade A")
elif(marks > 70):
    print("Grade B")
elif(marks > 60):
    print ("Grade C")
elif(marks > 50):
    print("PASS")
else:
    print("FAIL")