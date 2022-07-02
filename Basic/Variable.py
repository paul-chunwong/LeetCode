print("Hello World")

# comment line
'''
comment line
'''

print("------------------------------- Variable")

x = 5
print(x)

x = "Paul"
print(x)

x = str(1)
print(x)
print(type(x))

x = int(2)
print(x)
print(type(x))

x = float(3)
print(x)
print(type(x))

x = "Python"
y = "is"
z = "good"
print(x, y, z)

x = "Python"
y = "is"
z = "good"
print(x + y + z)

print("------------------------------- Global Variable")

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

print("------------------------------- Variable Type")

x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "Paul", "age": "28"}  # dict
x = {"apple", "banana", "cherry"}  # set
x = True  # bool
x = None  # none type


print("------------------------------- Variable Type")
