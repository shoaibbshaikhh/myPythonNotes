# filter() = creates a collection of elements from an iterable for which a function returns

# filter(function, iterable)

friends = [("Rachel",19),
           ("Monice",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data : data[1] >= 18

driving_buddies = list(filter(age, friends))

for i in driving_buddies:
    print(i)

# Output:
# ('Rachel', 19)
# ('Monice', 18)
# ('Chandler', 21)
# ('Ross', 20)
