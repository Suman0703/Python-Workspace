
# using append (it adds strings in the last)
'''with open("File_op\sample.txt", "a") as f:
    f.write("\nThis is a sample File ")
    f.write("\nI am learning Python")'''

# Using print to write to file
with open("File_op\sample.txt", "a") as f:
    print("\nthis is append function using print", file=f)
