# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args):  # You can give anything name you want but important thing is '*' asterisk
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5))


# Output:
# 15


def add(*stuff):  # You can give anything name you want but important thing is '*' asterisk
    sum = 0
    stuff = list(stuff)  # we can use list but not tuple here
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5))


# Output:
# 14