"""
Q217 - Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List


# Method 1 - find number of times the value occur in the list
# def containsDuplicate(self, nums: List[int]) -> bool:
#     for i in range(len(nums)):
#         if nums.count(nums[i]) > 1:
#             return True
#     return False


# Method 2 - sort and compare with the next value
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

"""
Method 1 runtime: O(n^2)
Method 2 runtime: O(n*log(n))
"""