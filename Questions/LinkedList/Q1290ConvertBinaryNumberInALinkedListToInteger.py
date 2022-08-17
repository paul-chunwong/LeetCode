"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.



Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10


Example 2:

Input: head = [0]
Output: 0
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        str1 = ""
        cur = head
        while cur:
            str1 = str1 + str(cur.val)
            cur = cur.next
        return int(str1,2)