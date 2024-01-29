#Exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Exercise 4 
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')

#Example 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry', 'apple', 'cherry')

#Example 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3

#Example 4
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#<class 'tuple'>
#<class 'str'>

#Example 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#('apple', 'banana', 'cherry')
#(1, 5, 7, 9, 3)
#(True, False, False)

#Example 6
tuple1 = ("abc", 34, True, 40, "male")
#('abc', 34, True, 40, 'male')

#Example 7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#<class 'tuple'>

#Example 8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#('apple', 'banana', 'cherry')

#Example 9
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#banana

#Example 10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#cherry

#Example 11
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#('cherry', 'orange', 'kiwi')

#Example 12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#('apple', 'banana', 'cherry', 'orange')

#Example 13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#('cherry', 'orange', 'kiwi', 'melon', 'mango')

#Example 14
histuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  #Yes, 'apple' is in the fruits tuple

#Example 15
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#("apple", "kiwi", "cherry")

#Example 16
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#('apple', 'banana', 'cherry', 'orange')

#Example 17
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#('apple', 'banana', 'cherry', 'orange')

#Example 18
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#('banana', 'cherry')

#Example 19
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Example 20
fruits = ("apple", "banana", "cherry")
#('apple', 'banana', 'cherry')

#Example 21
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#apple #banana #cherry

#Example 22
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']

#Example 23
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#apple   #['mango', 'papaya', 'pineapple']   #cherry
  
#Example 24
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple    #banana   #cherry

#Example 25
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  #apple #banana #cherry

#Example 26
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#apple #banana  #cherry
  
#Example 27
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#('a', 'b', 'c', 1, 2, 3)

#Example 28
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


