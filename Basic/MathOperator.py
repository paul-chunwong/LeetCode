print("------------------------------------------------------------------------- Operator ")

"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

print(10 / 3)
print(10 // 3)
print(10 % 3)

print(4 < 5 and 9 < 10)
print(not (4 < 5 and 9 < 10))
print(6 < 5 or 9 < 10)

print("------------------------------------------------------------------------- Math")

# Find min, max
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

# Find absolute value
x = abs(-7.25)
print(x)

# Square
x = pow(4, 3)
print(x)

import math

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

