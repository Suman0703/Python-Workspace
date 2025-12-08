import os

# check if file exists

if os.path.exists("File_op\sample.txt"):
    print("File Exists")

# Rename File
os.rename("File_op\sample.txt","File_op\Demo.txt")

# Delete File
os.remove("File_op\un.txt")