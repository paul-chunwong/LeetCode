"""
Q14 - Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
from typing import List


# def longestCommonPrefix(strs: List[str]) -> str:
#     smallestStr = strs[0]
#
#     for s in strs:
#         if len(s) < len(smallestStr):
#             smallestStr = s
#
#     i = 0
#     while i < len(smallestStr):
#         j = 0
