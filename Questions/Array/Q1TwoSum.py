"""
Q1 - Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]


myList = [2, 7, 11, 15]
print(twoSum(myList, 9))

myList = [3, 2, 4]
print(twoSum(myList, 6))


"""
Worst Case Runtime: O(n^2)

Iterate the nested loop and find the matching sum.
pointer j needs to starts at the next position of pointer i 
    1) reduce runtime to avoid unnecessary access
    2) avoid the case where adding twice of the number at same position equals to the target (e.g. [3,3] , 6)
"""
