#Exercise 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Exercise 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Exercise 3
for x in range(6):
    print(x)

#Exercise 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#EXAMPLE 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

#EXAMPLE 2
for x in "banana":
  print(x) 

#EXAMPLE 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#EXAMPLE 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

#EXAMPLE 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

#EXAMPLE 6
for x in range(6):
  print(x) 

#EXAMPLE 7
for x in range(2, 6):
  print(x) 

#EXAMPLE 8
for x in range(2, 30, 3):
  print(x) 

#EXAMPLE 9
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#EXAMPLE 10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

#EXAMPLE 11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#EXAMPLE 12
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement