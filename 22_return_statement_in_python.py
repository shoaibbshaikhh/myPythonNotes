# return statement = functions send python values/objects back to the caller
#                     These values/objects are known as the function's return value

def multiply(number1,number2):
    result = number1 * number2
    return result

print(multiply(6,8))


# another way to write above code in less no. of lines
def multiply(number1,number2):
    return number1 * number2
print(multiply(8,6))


Output:
# 48
# 48