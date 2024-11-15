# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Shoaib", 21, "male")

print(student.count("Shoaib"))
print(student.index("male"))

for x in student:
    print(x)

if "Shoaib" in student:
    print("Shoaib is here!")



# output:
# 1
# 2
# Shoaib
# 21
# male
# Shoaib is here!