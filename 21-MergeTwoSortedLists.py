__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/merge-two-sorted-lists/
date: 10-19-2015
----------------
problem:
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
----------------
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = None
        cur = None
        while l1 and l2:
            if l1.val < l2.val:
                if not cur:
                    start = l1
                    cur = l1
                else:
                    cur.next = l1
                    cur = cur.next
                l1 = l1.next
            else:
                if not cur:
                    start = l2
                    cur = l2
                else:
                    cur.next = l2
                    cur = cur.next
                l2 = l2.next
        if not l1:
            if cur:
                cur.next = l2
            else:
                start = l2
        else:
            if cur:
                cur.next = l1
            else:
                start = l1
        return start
