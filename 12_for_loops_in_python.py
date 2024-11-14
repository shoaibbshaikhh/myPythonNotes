# for loop = a statement that will execute it's block of code
#             a limited amount of times

                # while loop = unlimited
                # for loop = limited

import time  #time is imported for example 4

# example 1
for i in range(10):
    print(i+1)

# example 2
for i in range(50,100,2):
    print(i)

# example 3
for i in "Shoaib Shaikh":
    print(i)

# example 4
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy Eid!")


# Output:
# example 1
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

# example 2
# 50
# 52
# 54
# 56
# 58
# 60
# 62
# 64
# 66
# 68
# 70
# 72
# 74
# 76
# 78
# 80
# 82
# 84
# 86
# 88
# 90
# 92
# 94
# 96
# 98

# example 3
# S
# h
# o
# a
# i
# b
#
# S
# h
# a
# i
# k
# h

# example 4
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Happy Eid!