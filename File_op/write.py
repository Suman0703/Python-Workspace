
# write() - Write a string(overwrite)
'''with open("File_op\sample.txt", "w") as f:
    f.write("This is a sample File ")
    f.write("\nI am learning Python")'''

# writelines() - write a list of strings

lines = [ "I will perform File I/O operations in this file \n","I will learn Javascript after this"]
with open("File_op\sample.txt", "w") as f:
    f.writelines(lines)