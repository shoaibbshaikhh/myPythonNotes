# Slicing = Create a substring by extracting elements from another string
#             indexing[] or slice()
#             [start:stop:step]

#indexing[start:stop:step]
name = "Shoaib Shaikh"

first_name = name[0:6]      #[start:6]
last_name = name[7:]        #[7:end]
funky_name = name[::2]      #[start:end:2]
reversed_name = name[::-1]  #[start:end:-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#slicing(start,stop,step)
website1 = "https://google.com"
website2 = "https://microsoft.com"

url_slice = slice(8,-4)

print(website1[url_slice])
print(website2[url_slice])


# Output:
# Shoaib
# Shaikh
# Soi hih
# hkiahS biaohS
# google
# microsoft
