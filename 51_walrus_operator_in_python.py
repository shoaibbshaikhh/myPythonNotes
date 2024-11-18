# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variable as part of a larger expression

# happy = True
# print(happy)

# Output:
# True

# print(happy = True)  # it gives error so we can use walrus operator

print(happy := True)

# Output:
# True

# normal program
# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# Output:
# What food do you like?: mango
# What food do you like?: banana
# What food do you like?: apple
# What food do you like?: quit


# using walrus operator
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

# Output:
# What food do you like?: mango
# What food do you like?: banana
# What food do you like?: apple
# What food do you like?: quit