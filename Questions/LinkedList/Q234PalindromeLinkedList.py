"""
Q234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.


Example 1:

Input: head = [1,2,2,1]
Output: true


Example 2:

Input: head = [1,2]
Output: false

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        list = []
        while cur:
            list.append(cur.val)
            cur = cur.next

        if list == list[::-1]:
            return True
        else:
            return False