"""
Q136 - Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
from typing import List


def singleNumber(self, nums: List[int]) -> int:
    nums.sort()
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            return nums[i]
        elif nums[i] != nums[i + 1]:
            return nums[i]
        i = i + 2


"""
Runtime: O(n)
"""










