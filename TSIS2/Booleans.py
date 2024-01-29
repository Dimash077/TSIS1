#Exercise 1
print(10>9)
True

#Exercise 2 
print(10==9)
False

#Exercise 3
print(10<9)
False

#Exercise 4
print(bool("abc"))
True

#Exercise 5 
print(bool(0))
False

#Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)
True
False
False

#Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  #b is not greater than a

 #Example 3
print(bool("Hello"))
print(bool(15))
True
True

#Example 4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
True 
True

#Example 5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
True  
True    
True

#Example 6 
bool(False)  #False
bool(None)   #False
bool(0)      #False
bool("")     #False
bool(())     #False
bool([])     #False
bool({})     #False

#Example 7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
False

#Example 8 
def myFunction() :
  return True

print(myFunction())
True

#Example 9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  #YES!

#Example 10
x = 200
print(isinstance(x, int))
True
