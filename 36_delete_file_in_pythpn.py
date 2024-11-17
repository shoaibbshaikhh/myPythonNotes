import os
import shutil

path = "folder"
try:
    os.remove(path) # only removes files not folder..
    # os.rmdir(path)  # only removes empty directory not file
    # shutil.rmtree(path)  # delete files contain directory also but not only file
except FileNotFoundError:
    print("That file was not found :(")
except PermissionError:
    print("You do not have permission to delete that :(")
except OSError:
    print("You cannot delete that using that function :(")
else:
    print(path+" was deleted :)")