# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

# ex1:
squares = []    # create an empty list
for i in range(1,11):   # create a for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)


# same program like above but in less syntax
squares = [i * i for i in range(1,11)]
print(squares)

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ex2:
students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x : x >= 60, students))
print(passed_students)

# same program like above but in less syntax
students = [100,90,80,70,60,50,40,30,0]
passed_students = [i for i in students if i >= 60]
print(passed_students)

# Output:
# [100, 90, 80, 70, 60]
