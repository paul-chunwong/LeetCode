# Get the character at position 1 of the string
a = "Hello, World!"
print(a[1])

# WRONG!! Can not modify string like this, must convert to list using list(str) then modify element.
# a[1] = a[2] # Wrong!
# print(a)


# Loop the string
for x in "aaa":
    print(x)

# Get string length
a = "Hello, World!"
print(len(a))

# Check if "free" is present in string
s = "The best things in life are free!"
print("free" in s)

# Check if "free" is present in string
s = "The best things in life are fraa!"
print("free" not in s)

print("------------------------------- String slicing")

# Slice string from position 2 (inclusive) - 5 (exclusive)
b = "Hello, World!"
print(b[2:5])

# Slice string from beginning - 5 (exclusive)
b = "Hello, World!"
print(b[:5])

# Slice string from position 2 (inclusive) - end (inclusive)
b = "Hello, World!"
print(b[2:])

# Slice string from position -5 (inclusive) - position -2 (exclusive)
b = "Hello, World!"
print(b[-5:-2])

print("------------------------------- String Modify")

# String to Uppercase
a = "Hello, World!"
print(a.upper())

# String to Lowercase
a = "Hello, World!"
print(a.lower())

# Remove whitespace before & after string
a = "       Hello, World! "
print(a.strip())  # returns "Hello, World!"

# Replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))  # "Jello, World!"

# Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# Combine string
print("AA" + "BB")

# Insert characters that are illegal in a string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))

# Find the position of "welcome" in the string:
txt = "Hello, welcome to my world."
print(txt.find("welcome"))

# Convert str to list:
a = "Hello"
print(list(a))  # "Hello" -> ['H', 'e', 'l', 'l', 'o']


print("------------------------------- Char Modify")
char = 'a'
print(char)
char = ord(char)
char = char + 1
char = chr(char)
print(char)