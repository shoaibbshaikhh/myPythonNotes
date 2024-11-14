# Logical operators (and, or, not) = used to check if two or more condition statements is true

temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("the temperature is good today!")
#     print("go outside!")
# elif temp < 0 or temp > 30:
#     print("the temperature is bad today!")
#     print("stay inside!")

# not logical operator:
if not(temp >= 0 and temp <= 30):
    print("the temperature is good today!")
    print("go outside!")
elif not(temp < 0 or temp > 30):
    print("the temperature is bad today!")
    print("stay inside!")



# Output:
# What is the temperature outside?: 25
# the temperature is good today!
# go outside!

# What is the temperature outside?: -20
# the temperature is bad today!
# stay inside!

# not logical operator:
# What is the temperature outside?: 25
# the temperature is bad today!
# stay inside!

# What is the temperature outside?: -20
# the temperature is good today!
# go outside!
