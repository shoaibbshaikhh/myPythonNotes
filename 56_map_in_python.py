# map() = applies a function to each item in an iterable (list, tuple, etc.)

# map(function,iterable)

store = [("Shirt",20.00),
         ("Pants",25.00),
         ("Jacket",50.00),
         ("Socks",10.00)]  # prices in us dollars

# convert dollars in euros
to_euros = lambda data : (data[0],data[1] * 0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

# Output:
# ('Shirt', 16.4)
# ('Pants', 20.5)
# ('Jacket', 41.0)
# ('Socks', 8.2)