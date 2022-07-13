"""
Q7 - Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


def reverse(x: int) -> int:
    temp = str(x)
    result = ""
    if temp[0] == '-':
        temp = temp[1:]

        i = len(temp) - 1
        while i >= 0:
            result = result + temp[i]
            i = i - 1
        result = '-' + result
    else:
        i = len(temp) - 1
        while i >= 0:
            result = result + temp[i]
            i = i - 1

    result = int(result)
    if result > (2 ** 31 - 1) or result < (-2 ** 31):
        return 0
    else:
        return result

"""
#1) Convert the int to str (if negative, take the '-' out)
#2) Reverse the str from the back (if negative, put '-' in the front)
#3) Convert the str back to int 
#4) Check if the final int is within 32bit range
"""

reverse(-12)
reverse(14)