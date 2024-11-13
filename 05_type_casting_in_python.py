x = 1 #int
y = 2.0 #float
z = "3" #str

print(type(x)) #int
print(type(y)) #float
print(type(z)) #str

# type casting method
x = float(x) #float
y = str(y) #str
z = int(z) #int

print(type(x)) #float
print(type(y)) #str
print(type(z)) #int

# real life use case of type casting
print("x is "+str(x))
print(y*3)
print("z is "+str(z))