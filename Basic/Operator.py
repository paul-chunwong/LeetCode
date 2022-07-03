"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

print(10/3)
print(10//3)
print(10%3)

print(4 < 5 and 9 < 10)
print(not(4 < 5 and 9 < 10))
print(6 < 5 or 9 < 10)
