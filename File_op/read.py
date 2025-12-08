# all read operations

# read() - read the whole file 
with open("File_op\sample.txt", "r") as f:
    content = f.read()
    print(content)

# reading n no. of characters from a file 
'''with open("File_op\sample.txt", "r") as f:
    content = f.read(4)
    print(content)'''

# readline() -Read one line at a time
'''with open("File_op\sample.txt", "r") as f:
    content = f.readline()
    content2 = f.readline()
    print(content)
    print(content2)'''

# readlines() - Read All lines into list
'''with open("File_op\sample.txt", "r") as f:
    content = f.readlines()
    print(content)'''

# Iterating over the all file objects (including \n)
'''with open("File_op\sample.txt", "r") as f:
    for line in f:
        print(line.strip)'''