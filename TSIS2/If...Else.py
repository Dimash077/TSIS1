#Exercise 1
a = 50
b = 10
if a > b:
  print("Hello World")

#Exercise 2
a = 50
b = 10
if a != b:
  print("Hello World")

#Exercise 3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#Exercise 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

#Exercise 5
if a == b and c == d:
    print("Hello")

#Exercise 6
if a == b or c == d:
  print("Hello")

#Exercise 7
if 5 > 2:
    print("YES")

#Exercise 8
a = 2
b = 5
print("YES") if a == b else print("NO")

#Exercise 9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#EXAMPLE 1
a = 33
b = 200

if b > a:
  print("b is greater than a")

#EXAMPLE 2
a = 33
b = 200

if b > a:
  print("b is greater than a")

#EXAMPLE 3
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#EXAMPLE 4 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#EXAMPLE 5
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#EXAMPLE 6
a = 200
b = 33

if a > b: print("a is greater than b")

#EXAMPLE 7
a = 2
b = 330

print("A") if a > b else print("B")

#EXAMPLE 8
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

#EXAMPLE 9
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#EXAMPLE 10
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#EXAMPLE 11
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#EXAMPLE 12
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#EXAMPLE 13
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement