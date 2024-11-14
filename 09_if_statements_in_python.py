# If statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")



# Output:
# How old are you?: 100
# You are a century old!

# How old are you?: 21
# You are an adult!

# How old are you?: -2
# You haven't been born yet!

# How old are you?: 12
# You are a child!