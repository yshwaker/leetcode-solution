__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/reverse-linked-list/
date: 10-19-2015
----------------
problem:
Reverse a singly linked list.
----------------
not practiced enough
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        nxt = head.next
        prev = None
        while head:
            head.next = prev
            if not nxt:
                return head
            prev = head
            head = nxt
            nxt = nxt.next
