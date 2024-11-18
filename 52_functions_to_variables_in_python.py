def hello():
    print("Hello")

hello()  # Output: "Hello"
print(hello) # Output: "<function hello at 0x000002A472541440>"  # and this number change continues when we run the code

hi = hello
hi() # Output: "Hello"

say = print
say("Whoa! I can't believe this works! :)")  # now say also run as print() function

# Output:
# Whoa! I can't believe this works! :)