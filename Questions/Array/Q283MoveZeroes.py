"""
Q283 - Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
from typing import List


# Method 1 failed for some reasons
# def moveZeroes(nums: List[int]) -> None:
#     i = 0
#     while i < len(nums):
#         if nums[i] == 0:
#             nums.pop(i)
#             nums.append(0)
#             continue
#         i = i + 1


# Method 2
def moveZeroes(nums: List[int]) -> None:
    insertPosition = 0
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            temp = nums.pop(i)
            nums.insert(insertPosition,temp)
            insertPosition = insertPosition + 1
        i = i + 1
    return nums


print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))
print(moveZeroes([0,0]))
print(moveZeroes([0,0,3]))

"""
Method 2 runtime: O(n)
"""