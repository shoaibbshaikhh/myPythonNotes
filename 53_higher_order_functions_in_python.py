# Higher Order Function = a function that either:
#                         1. accepts a function as an arguments
#                           or
#                         2. returns a function
#                           (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)     #Output: "HELLO"
hello(quiet)    #Output: "hello"


def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(divide(10))   # Output: "5.0"