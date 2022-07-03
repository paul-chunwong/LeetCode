print("------------------------------------------------------------------------- If-Else ")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# One line if-else statement
a = 2
b = 330
print("A") if a > b else print("B")

# One line if-else statement
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print("------------------------------------------------------------------------- While Loop ")

# Break the loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue the loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("------------------------------------------------------------------------- For Loop ")

# For loop in list
fruits = ["apple", "banana"]
for x in fruits:
    print(x)

# For loop in string
for x in "ban":
    print(x)

# For loop using range from beginning (0 - 2 exclusive)
for x in range(3):
  print(x)

# For loop using specific range (2 - 5 exclusive)
for x in range(2, 5):
  print(x)

# For loop using specific range (2, 5, 8) with increment 3
for x in range(2, 10, 3):
  print(x)