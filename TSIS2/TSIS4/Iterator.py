#Example 1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))    #блогодаря iterator мы принтим каждый элемент.

#Example 2
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))    # Здесь мы принтуем по буквам стринг тоже итерируемый по последовательнсти
print(next(myit))
print(next(myit))
print(next(myit))

#Example 3
mytuple = ("apple", "banana", "cherry")
 
for x in mytuple:
    print(x)          #for здесь пробегается по каждому и принтует слова

#Example 4
mystr = "banana"
for x in mystr:      # здесь уже пробегаается по каждой букве и принтует
    print(x)

#Example 5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))            
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Example 6
class MyNumbers:
   def __iter__(self):
     self.a = 1
     return self
   
def __next__(self):
   if self.a <=20:
    self.a +=1
    return x
   else:
      raise StopIteration
   
MyClass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
   print(x)



