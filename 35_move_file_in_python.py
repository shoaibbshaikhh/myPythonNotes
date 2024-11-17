import os

source = "text.txt"
destination = "C:\\Users\\shaik\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is a already file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
except Exception:
    print("Something went wrong :(")