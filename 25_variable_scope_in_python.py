# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = "Shoaib" # global scope (available inside & outside function)

def display_name():
    name = "Shaikh" # local scope (available only inside this function)
    print(name)

display_name()

# Output:
# Shaikh


print(name)

# Output:
# Shoaib