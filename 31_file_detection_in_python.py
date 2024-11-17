import os

path = "D:\\CS\\Practice\\pythonPrograms\\pythonCode\\pythonCourse"

if os.path.exists(path):
    print("That location exists!")
    # if os.path.isfile(path):
    #     print("That is a file")
    # elif os.path.isdir(path):
    #     print("That is a directory")
else:
    print("That location doesn't exists!")