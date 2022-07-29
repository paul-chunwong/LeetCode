"""
Split bill program:
3 users, want to split the bill, total $100

eg) $100/3 -> $33.3333....

"""
from typing import List

"""
Inputs:

double total;
int numberOfUser;

int / int = 3
double / int = 3.33333

result = 0
result = total/numberOfUser

print("This is the amount you need to pay per person: ")
print(result)

"""
import math

# total = 100.0
# numberOfUser = 3

print("Please input the total amount of the bill: ")
total = float(input())
print("Please input the number of people you want to split the bill: ")
numberOfUser = int(input())

# total = 100 * 100
# total = 10000

result = total/numberOfUser
# result = math.floor(result)
# result = 3333

# result = result / 100
# result = 33.33

print("This is the amount you need to pay per person: $" + str(round(result,2)))





str = 'Hello World!'
print(str[2:5])


def sum(nums: List[int]):
    result = 0
    for i in nums:
          result = result + i
    return result

print(sum([0,200,300]))

