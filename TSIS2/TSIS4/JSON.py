#Example 1
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'    
y = json.loads(x)               #If you have a JSON string, you can parse it by using the json.loads() method.
print(y["age"])

#Example 2
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York" 
}        #If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
y = json.dumps(x)
print(y)

#Example 3
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False)) 
print(json.dumps(None))

#Example 4
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

#Example 5
json.dumps(x, indent=4)     #indent divide by parts

#Example 6
json.dumps(x, indent=4, separators=(". ", " = "))

#Example 7
json.dumps(x, indent=4, sort_keys=True)
