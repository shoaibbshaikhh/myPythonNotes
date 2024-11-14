# Loop  control statements = change a loops execution from its normal sequence


# break = used to determine the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as placeholder

#break:
while True:
    name = input("Ente your name: ")
    if name != "":
        break

# continue:
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# pass:
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)



# Output:
# break:
# Ente your name:
# Ente your name:
# Ente your name: Shoaib

# continue:
# 1234567890

# pass
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 14
# 15
# 16
# 17
# 18
# 19
# 20