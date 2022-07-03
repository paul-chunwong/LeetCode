print("------------------------------------------------------------------------- Create Function ")


# Without argument
def my_function():
    print("Hello from a function")


my_function()


# With argument
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Default Parameter Value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("India")
my_function()


# Pass in list
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Recursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
