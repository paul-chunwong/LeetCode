"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
"""
# Not Fast!
def checkPrime(num: int, primeDict:{}) -> bool:
    i = 2
    while i < num/2+1:
        if i in primeDict:
            if num%i == 0:
                return False
        i = i + 1
    return True

def countPrimes(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return 0
    count = 1
    j = 3
    primeDict = {}
    while j < n:
        if checkPrime(j,primeDict) == True:
            print(j)
            primeDict[j] = j
            count = count + 1
        j = j + 1
    return count-1

print(countPrimes(1000))
