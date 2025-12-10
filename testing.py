# Importing a Module
from person import Person

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Lamda function
x = lambda a : a + 10
print(x(5))

# Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# scopes and functions
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Dates
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# JSON
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
johnsage = y["age"]
# the result is a Python dictionary:
print(f"John is {johnsage} years old.")

# try catch
try:
  print(notfound)
except:
  print("An exception occurred - notfound does not exist")

# user input
username = input("Enter username:")
print("Username is: " + username)

# Context Managers
with open(".env", "r") as file:
    print(file.read())