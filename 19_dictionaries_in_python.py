# dictionary = A changeable, unordered collection of unique key: value pairs
#             Fast because they use hashing, allow us to access a value quickly


capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

# ex1:
# print(capitals['Russia'])

# ex2:
# print(capitals['Germany'])

# ex3:
# print(capitals.get('germany'))

# ex4:
# print(capitals.keys())

# ex5:
# print(capitals.values())

# ex6:
# print(capitals.items())

# ex7:
# for key,value in capitals.items():
#     print(key, value)

# methods in dictionaries
# ex8:
# capitals.update({'Germany':'Berlin'})
# for key,value in capitals.items():
#     print(key, value)

# ex9:
# capitals.update({'USA':'Las Vegas'})
# for key,value in capitals.items():
#     print(key, value)

# ex10:
# capitals.pop('China')
# for key,value in capitals.items():
#     print(key, value)

# ex11:
# capitals.clear()
# for key,value in capitals.items():
#     print(key, value)




# Output:
# ex1:
# Moscow

# ex2:
#     print(capitals['Germany'])
#           ~~~~~~~~^^^^^^^^^^^
# KeyError: 'Germany'

# ex3:
# None

# ex4:
# dict_keys(['USA', 'India', 'China', 'Russia'])

# ex5:
# dict_values(['Washington DC', 'New Delhi', 'Beijing', 'Moscow'])

# ex6:
# dict_items([('USA', 'Washington DC'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])

# ex7:
# USA Washington DC
# India New Delhi
# China Beijing
# Russia Moscow

# ex8:
# USA Washington DC
# India New Delhi
# China Beijing
# Russia Moscow
# Germany Berlin

# ex9:
# USA Las Vegas
# India New Delhi
# China Beijing
# Russia Moscow

# ex10:
# USA Washington DC
# India New Delhi
# Russia Moscow

# ex11:
#