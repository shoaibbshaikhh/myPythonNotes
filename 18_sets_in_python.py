# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# method1:
# for x in utensils:
#     print(x)

# method2:
# utensils.add("napkin")
# for x in utensils:
#     print(x)

# method3:
# utensils.remove("fork")
# for x in utensils:
#     print(x)

# method4:
# utensils.clear()
# for x in utensils:
#     print(x)

# method5:
# utensils.update(dishes)
# for x in utensils:
#     print(x)

# method6:
# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)

# method7:
# print(utensils.difference(dishes))

# method8:
# print(utensils.intersection(dishes))



# Output:
# method1:
# knife
# spoon
# fork

# method2:
# fork
# knife
# napkin
# spoon

# method3:
# spoon
# knife

# method4:
#

# method5:
# spoon
# cup
# bowl
# plate
# fork
# knife

# method6:
# bowl
# cup
# plate
# spoon
# knife
# fork

# method7:
# {'spoon', 'fork'}

# method8:
# {'knife'}