"""
Q125 - Valid Palindrome

A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""


def isPalindrome(s: str) -> bool:
    s = s.lower()
    tempList = ""
    i = 0
    while i < len(s):
        if s[i].isalnum():
            tempList = tempList + s[i]
        i = i + 1
    print(tempList)

    reversedList = ""
    i = len(tempList)-1
    while i >= 0:
        reversedList = reversedList + tempList[i]
        i = i - 1

    if tempList == reversedList:
        return True
    else:
        return False

print(isPalindrome("A man, a plan, a canal: Panama"))


"""
Need to consider the case where all non-alphanumeric should be removed before checking the two strings
"""