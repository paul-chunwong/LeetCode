"""
Given an integer n, return a string array answer(1 - indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i( as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1", "2", "Fizz"]

Example 2:
Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]

Example 3:
Input: n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz",
"""
from Basic import List

def fizzBuzz(n: int) -> List[str]:
    list = []
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(str(i))
        i = i + 1
    return list
