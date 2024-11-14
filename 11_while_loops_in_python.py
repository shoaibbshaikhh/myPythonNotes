# While loop = a statement that will execcute it's block of code,
#             as long as it's condition remains true

# method 1
# name = ""

# while len(name) == 0:
#     name = input("Enter you name: ")

# method 2
name = None

while not name:
    name = input("Enter you name: ")

print("Hello "+name)


# Output:
# method 1:
# Enter you name:
# Enter you name:
# Enter you name:
# Enter you name: Shoaib
# Hello Shoaib

# method 2:
# Enter you name:
# Enter you name:
# Enter you name:
# Enter you name: Shoaib
# Hello Shoaib