#Exercise 1
class MyNumbers:
    def __init__(self, n):
        self.n = n
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.n:
            x = self.a ** 2
            self.a += 1
            return x
        else:
            raise StopIteration

MyClass = MyNumbers(5)
myiter = iter(MyClass)
for x in myiter:
    print(x)

#Exercise 2
def even_numbers(n):
    for number in range(0,n+1):
        if number%2 ==0:
            yield number
n = int(input("Any number:"))
even_num = even_numbers(n)
print(",".join(str(num) for num in even_num))

#Exrecise 3
def divisible_num(n):
    for number in range(0,n+1):
        if number%3==0 and number%4==0:
            yield number
n = int(input("Any number:"))
divi_num = divisible_num(n)
print(",".join(str(num) for num in divi_num))

#Exercise 4
def squares(a,b):
   for number in range(a,b+1):
      yield number **2

for square in squares(1,5):
   print(square)

#Exercise 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)



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



