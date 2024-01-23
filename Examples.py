#Comments
#EXAMPLE 1
#This is a comment
print("Hello, World!")

#EXAMPLE 2
print("Hello, World!") #This is a comment

#EXAMPLE 3
#print("Hello, World!")
print("Cheers, Mate!")

#EXAMPLE 4
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#EXAMPLE 5
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#Data Types
#EXAMPLE 1
x = 5
print(type(x))

#Numbers
#EXAMPLE 1 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#EXAMPLE 2
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#EXAMPLE 3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#EXAMPLE 4 
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#EXAMPLE 5 
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#EXAMPLE 6
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#EXAMPLE 7 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#EXAMPLE 8 
import random

print(random.randrange(1, 10))

#Strings
#EXAMPLE 1
print("Hello")
print('Hello')

#EXAMPLE 2
a = "Hello"
print(a)

#EXAMPLE 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#EXAMPLE 4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#EXAMPLE 5
a = "Hello, World!"
print(a[1])

#EXAMPLE 6
for x in "banana":
  print(x)

#EXAMPLE 7
  a = "Hello, World!"
print(len(a))

#EXAMPLE 8
txt = "The best things in life are free!"
print("free" in txt)

#EXAMPLE 9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#EXAMPLE 10
  txt = "The best things in life are free!"
print("expensive" not in txt)

#EXAMPLE 11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#EXAMPLE 12
  b = "Hello, World!"
print(b[2:5])

#EXAMPLE 13
b = "Hello, World!"
print(b[:5])

#EXAMPLE 14
b = "Hello, World!"
print(b[2:])

#EXAMPLE 15
b = "Hello, World!"
print(b[-5:-2])

#EXAMPLE 16
a = "Hello, World!"
print(a.upper())

#EXAMPLE 17
a = "Hello, World!"
print(a.lower())

#EXAMPLE 18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#EXAMPLE 19
a = "Hello, World!"
print(a.replace("H", "J"))

#EXAMPLE 20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#EXAMPLE 21
a = "Hello"
b = "World"
c = a + b
print(c)

#EXAMPLE 22
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#EXAMPLE 23(WRONG)
age = 36
txt = "My name is John, I am " + age
print(txt)

#EXAMPLE 24
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#EXAMPLE 25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#EXAMPLE 26
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#EXAMPLE 27(WRONG)
# txt = "We are the so-called "Vikings" from the north."

#EXAMPLE 28
txt = "We are the so-called \"Vikings\" from the north."

#Syntax
#EXAPMLE 1
if 5 > 2:
  print("Five is greater than two!")
#EXAPMLE 2(WRONG)
# if 5 > 2:
# print("Five is greater than two!")

#EXAPMLE 3
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#EXAPMLE 4(WRONG)
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")

#EXAPMLE 5
x = 5
y = "Hello, World!"

#EXAPMLE 6
#This is a comment.
print("Hello, World!")

#Variables
#EXAMPLE 1
x = 5
y = "John"
print(x)
print(y)

#EXAMPLE 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#EXAMPLE 3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#EXAMPLE 4
x = 5
y = "John"
print(type(x))
print(type(y))

#EXAMPLE 5
x = "John"
# is the same as
x = 'John'

#EXAMPLE 6
a = 4
A = "Sally"
#A will not overwrite a

#EXAMPLE 7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#EXAMPLE 8(WRONG)
# 2myvar = "John"
# my-var = "John"
# my var = "John"

#EXAMPLE 9
myVariableName = "John"

#EXAMPLE 10
MyVariableName = "John"

#EXAMPLE 11
my_variable_name = "John"

#EXAMPLE 12
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#EXAMPLE 13
x = y = z = "Orange"
print(x)
print(y)
print(z)

#EXAMPLE 14
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#EXAMPLE 15
x = "Python is awesome"
print(x)

#EXAMPLE 16
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#EXAMPLE 17
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#EXAMPLE 18
x = 5
y = 10
print(x + y)

#EXAMPLE 19(WRONG)
x = 5
y = "John"
print(x + y)

#EXAMPLE 20
x = 5
y = "John"
print(x, y)

#EXAMPLE 21
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#EXAMPLE 22
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#EXAMPLE 23
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#EXAMPLE 24
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)