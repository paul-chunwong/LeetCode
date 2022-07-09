"""
Q35 - Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List

# nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# [4,9,5] [4,4,8,9,9]

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    resultList = []

    while len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] == nums2[0]:
            resultList.append(nums1.pop(0))
            nums2.pop(0)
        elif nums1[0] > nums2[0]:
            nums2.pop(0)
        elif nums1[0] < nums2[0]:
            nums1.pop(0)

    return resultList

print(intersect([9, 5], [9, 4, 9, 8, 4]))
print(intersect([1, 2], [2, 1]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersect([1, 4, 6, 6, 8], [2, 4, 6, 8, 8]))




# Wrong approach
# from typing import List
#
#
# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     if len(nums1) >= len(nums2):
#         longList = nums1
#         shortList = nums2
#     else:
#         longList = nums2
#         shortList = nums1
#
#     # print(shortList)
#     # print(longList)
#
#     resultList = []
#     k = 0
#
#     while k < len(shortList):
#         i = 0
#         while i < len(longList):
#             tempList = []
#             if shortList[k] == longList[i]:
#                 tempList.append(shortList[k])
#                 j = k + 1
#                 i2 = 0
#                 print(shortList[k])
#                 while j < len(shortList):
#                     if k+1 < len(longList):
#                         if longList[k+1] == shortList[j]:
#                             tempList.append(shortList[j])
#                             print(shortList[j])
#                         else:
#                             break
#                     j = j + 1
#                     i = i + 1
#             if len(tempList) > len(resultList):
#                 resultList = tempList
#             i = i + 1
#
#         k = k + 1
#
#     return resultList
#
#
# print(intersect([9, 5], [9, 4, 9, 8, 4]))
# # print(intersect([1, 2], [2, 1]))
# print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
# print(intersect([1, 4, 6, 6, 8], [2, 4, 6, 8, 8]))
