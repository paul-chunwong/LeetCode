"""
Q242 - Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s.count(s[i]) != t.count(t[t.find(s[i])]) or t.find(s[i]) == -1:
            return False
    return True
