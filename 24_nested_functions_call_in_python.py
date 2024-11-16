# nested functions calls = function calls inside other functions calls
#                          innermost functions calls are resolved first
#                          returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# Output:
# Enter a whole positive number: -3.14
# 3


# Same program like above but in a single line
print(round(abs(float(input("Enter a whole positive number: ")))))

# Output:
# Enter a whole positive number: -3.14
# 3