# Pythonn can be used to perform operations on a file 

f = open("File_op\sample.txt","r") #open the file

data = f.read() # read data from file

# line1 = f.readline() read file line by line

print(data)
print(type(data))

f.close() # Closing the file