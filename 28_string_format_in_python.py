# str.format() = optional method that gives users
#                 more control when displaying output

animal = "cow"
item = "moon"

# ex1:
print("The "+animal+" jumped over the "+item)

# Output:
# The cow jumped over the moon

# ex2:
print("The {} jumped over the {}".format(animal,item))

# Output:
# The cow jumped over the moon

# ex3:
print("The {1} jumped over the {0}".format(item,animal))  # Positional arguments

# Output:
# The cow jumped over the moon

# ex4:
# print("The {animal} jumped over the {item}".format(item="moon",animal="cow"))  # Keyword arguments

# Output:
# The cow jumped over the moon

# ex5:
text = "The {} jumped over the {}"
print(text.format(animal,item))

# Output:
# The cow jumped over the moon

# ex6:
name = "Shoaib"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))  # Create space from right side
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # Create space from right side
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # Create space from left side
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # Create space from both side

# Output:
# Hello, my name is Shoaib
# Hello, my name is Shoaib    . Nice to meet you
# Hello, my name is Shoaib    . Nice to meet you
# Hello, my name is     Shoaib. Nice to meet you
# Hello, my name is   Shoaib  . Nice to meet you


# ex7:
number1 = 3.14159

print("The number pi is {:.2f}".format(number1))  # display only 2 digit decimal = {:2f}

# Output:
# The number pi is 3.14

# ex8:
number2 = 1000000
print("The number is {:,}".format(number2))  # adds comma in number at right place

# Output:
# The number is 1,000,000


# ex9:
number3 = 1000
print("The number is {:b}".format(number3))  # display binary number

# Output:
# The number is 1111101000


# ex10:
number4 = 1000
print("The number is {:o}".format(number4))  # display octave number

# Output:
# The number is 1750


# ex11:
number5 = 1000
print("The number is {:x}".format(number5))  # display hexa-decimal number
print("The number is {:X}".format(number5))  # display Capital hexa-decimal number
print("The number is {:e}".format(number5))  # display scientific notation number
print("The number is {:E}".format(number5))  # display Capital scientific notation number

# Output:
# The number is 3e8
# The number is 3E8
# The number is 1.000000e+03
# The number is 1.000000E+03