# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# def double(x):
#     return x * 2
# print(double(5))  # Output: "10"

double = lambda x:x * 2
multiply = lambda x, y : x * y
add = lambda x, y, z : x + y + z
full_name = lambda first_name, last_name : first_name+" "+last_name
age_check = lambda age : True if age >= 18 else False

print(double(5))    # Output: "10"
print(multiply(5,6))    # Output: "30"
print(add(5, 6, 7)) # Output: "18"
print(full_name("Shoaib","Shaikh"))    # Output: "Shoaib Shaikh"
print(age_check(21))    # Output: "True"