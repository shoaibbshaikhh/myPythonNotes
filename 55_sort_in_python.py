# sort() method = used with lists
# sort() function = used with iterables

# students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]

# students.sort()
# students.sort(reverse=True) # sort in reverse order

# for i in students:
#     print(i)

# Output:
# Mr.Krabs
# Patrick
# Sandy
# Spongebob
# Squidward


# sorted_students = sorted(students)
#
# for i in sorted_students:
#     print(i)

# Output:
# Mr.Krabs
# Patrick
# Sandy
# Spongebob
# Squidward

# students = [("Squidward","F",60),
#             ("Sandy","A",33),
#             ("Patrick","D",36),
#             ("Spongebob","B",20),
#             ("Mr.Krabs","C",78)]
#
# grade = lambda grades : grades[1]  # Sorted using grades
# students.sort(key=grade)
#
# for i in students:
#     print(i)

# Output:
# ('Sandy', 'A', 33)
# ('Spongebob', 'B', 20)
# ('Mr.Krabs', 'C', 78)
# ('Patrick', 'D', 36)
# ('Squidward', 'F', 60)


# Sorting iterables:
students = (("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr.Krabs","C",78))

age = lambda ages : ages[2]  # Sorted using ages
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)


# Output:
# ('Spongebob', 'B', 20)
# ('Sandy', 'A', 33)
# ('Patrick', 'D', 36)
# ('Squidward', 'F', 60)
# ('Mr.Krabs', 'C', 78)