#Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"

#Exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#Exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Exercise 8 
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Example 1 
thislist = ["apple", "banana", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry']

#Example 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry', 'apple', 'cherry']

#Example 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
3

#Example 4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#['apple', 'banana', 'cherry']
#[1, 5, 7, 9, 3]
#[True, False, False]

#Example 5
list1 = ["abc", 34, True, 40, "male"]
#['abc', 34, True, 40, 'male']

#Example 6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#<class 'list'>

#Example 7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#['apple', 'banana', 'cherry']

#Example 8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#banana

#Example 9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#cherry

#Example 10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#['cherry', 'orange', 'kiwi']

#Example 11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#['apple', 'banana', 'cherry', 'orange']

#Example 12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#['cherry', 'orange', 'kiwi', 'melon', 'mango']

#Example 13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#['orange', 'kiwi', 'melon']

#Example 14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Yes, 'apple' is in the fruits list
  
#Example 15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#['apple', 'blackcurrant', 'cherry']

#Example 16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#Example 17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']

#Example 18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#['apple', 'watermelon']

#Example 19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#['apple', 'banana', 'watermelon', 'cherry']

#Example 20
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']

#Example 21
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#['apple', 'orange', 'banana', 'cherry']

#Example 22
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Example 23
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#['apple', 'banana', 'cherry', 'kiwi', 'orange']

#Example 24
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']

#Example 25
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry', 'banana', 'kiwi']

#Example 26
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']

#Example 27
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']

#Example 28
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']

#Example 29
thislist = ["apple", "banana", "cherry"]
del thislist
#This list was sucessfully deleted.

#Example 30
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]

#Example 31
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  #apple
  #banana
  #cherry

#Example 32
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#apple
#banana
#cherry

#Example 33
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#apple
#banana
#cherry

#Example 34
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#apple
#banana
#cherry

#Example 35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#['apple', 'banana', 'mango']

#Example 36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#['apple', 'banana', 'mango']

#Example 37
newlist = [x for x in fruits if x != "apple"]
#['banana', 'cherry', 'kiwi', 'mango']

#Example 38
newlist = [x for x in fruits]
#['apple', 'banana', 'cherry', 'kiwi', 'mango']

#Example 39
newlist = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Example 40
newlist = [x for x in range(10) if x < 5]
#[0, 1, 2, 3, 4]

#Example 41
newlist = [x.upper() for x in fruits]
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#Example 42
newlist = ['hello' for x in fruits]
#['hello', 'hello', 'hello', 'hello', 'hello']

#Example 43
newlist = [x if x != "banana" else "orange" for x in fruits]
#['apple', 'orange', 'cherry', 'kiwi', 'mango']

#Example 44
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Example 45
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#[23, 50, 65, 82, 100]

#Example 46
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#Example 47
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#[100, 82, 65, 50, 23]

#Example 48
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#[50, 65, 23, 82, 100]

#Example 49
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#['Kiwi', 'Orange', 'banana', 'cherry']

#Example 50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#['banana', 'cherry', 'Kiwi', 'Orange']

#Example 51
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#['cherry', 'Kiwi', 'Orange', 'banana']

#Example 52
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']

#Example 53
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#['apple', 'banana', 'cherry']

#Example 54
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]

#EExample 55
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)
#['a', 'b', 'c', 1, 2, 3]

#Example 56
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#['a', 'b', 'c', 1, 2, 3].




  
