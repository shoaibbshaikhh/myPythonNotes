# nested loops = the "inner loop" will finish all of it's iterations before
#                 finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


# Output:
# How many rows?: 6
# How many columns? 5
# Enter a symbol to use: @
# @@@@@
# @@@@@
# @@@@@
# @@@@@
# @@@@@
# @@@@@