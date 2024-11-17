# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism: # parent class
    alive = True

class Animal(Organism): # child parent class

    def eat(self):
        print("This animal is eating")

class Dog(Animal):  # child class
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

# Output:
# True
# This animal is eating
# This dog is barking

