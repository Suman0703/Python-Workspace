# Files have cursor/index position inside.

# tell()- where i am
'''with open("File_op\sample.txt", "r") as f:
    print(f.tell()) # starts at 0

    f.read(5)
    print(f.tell()) # now 5'''

# seek jump to another position
with open("File_op\sample.txt", "r") as f:
    f.read(10)
    f.seek(0)  # back to start
    again = f.read(5)
    print(again)