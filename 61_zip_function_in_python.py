# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames, passwords)

print(type(users))

for i in users:
    print(i)

# Output:
# <class 'zip'>
# ('Dude', 'p@ssword')
# ('Bro', 'abc123')
# ('Mister', 'guest')

users = dict(zip(usernames, passwords))

print(type(users))

for key, value in users.items():
    print(key+" : "+value)

# Output:
# <class 'dict'>
# Dude : p@ssword
# Bro : abc123
# Mister : guest


users = list(zip(usernames, passwords))

print(type(users))

for i in users:
    print(i)

# Output:
# <class 'list'>
# ('Dude', 'p@ssword')
# ('Bro', 'abc123')
# ('Mister', 'guest')


usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)

# Output:
# ('Dude', 'p@ssword', '1/1/2021')
# ('Bro', 'abc123', '1/2/2021')
# ('Mister', 'guest', '1/3/2021')