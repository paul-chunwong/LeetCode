"""
Q26 - Remove Duplicates

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements. Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
              [0,1,0,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    isEndPoint = False
    for j in range(len(nums)):
        if isEndPoint or len(nums) == 0 or len(nums) == 1:
            break
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                break
            else:
                nums[1] = -101
                break
        else:
            for k in range(j + 1, len(nums)):
                if nums[j + 1] > nums[j]:
                    break
                elif nums[k] > nums[j]:
                    nums[j + 1] = nums[k]
                    nums[k] = -101
                    break
                elif k == len(nums) - 1:
                    isEndPoint = True
                    break

    return nums.index(max(nums)) + 1


"""
Use nested loop to run thought the list via two pointers method
    1) Need to be careful about the short length list
    2) Adjust the second pointer corresponds to the first pointer to increase runtime make less trouble
    3) Check for when we need to stop while running the loop
"""
