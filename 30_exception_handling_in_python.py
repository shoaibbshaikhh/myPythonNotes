# exception = events detected during execution that interrupt the flow of a program
from logging import exception

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("You can't divide by zero! idiot!")
except ValueError:
    print("Enter only numbers plz")
except Exception:
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")


# Output:
# ex1:
# Enter a number to divide: 5
# Enter a number to divide by: 0
# You can't divide by zero! idiot!
# This will always execute

# ex2:
# Enter a number to divide: 5
# Enter a number to divide by: pizza
# Enter only numbers plz
# This will always execute

# ex3:
# Enter a number to divide: 5
# Enter a number to divide by: 3
# 1.6666666666666667
# This will always execute