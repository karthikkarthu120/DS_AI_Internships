import math
from py_compile import main
print(math.sqrt(16))

#Functions
def greet():
    print("Hello, World!")
greet()

#Function with parameters
def add_numbers(a,b):
    return a + b
result = add_numbers(5, 3)
print("The sum of 5 and 3 is:", result)

#Function with default parameters
x= 10

def show_value():
    x = 5
    print(x)

show_value()
print(x)

#Global variable
import math
import random

print(math.sqrt(16))
print(random.randint(1, 10))

#Global and local variables
icecream = "vanilla"
def food():
    fruit = "apple"
    vegetable = "carrot"
    print(fruit,"is good for health")
    print(icecream,"is a good flavour")
    print("Vegetable is also good for health:", vegetable)
food()

import random
print(random.randint(1, 25))