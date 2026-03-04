try:
    with open("File_op\sample.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.Please check the name")
except PermissionError:
    print("NO permission to read this file")
except Exception as e:
    print("Some Other error Occurred:",e)