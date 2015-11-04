__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/remove-linked-list-elements/
date: 11-3-2015
----------------
problem:
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
----------------
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        res = head
        while head:
            if head.val == val:
                # remove the first node 
                if res == head:
                    res = head.next
                else:
                    prev.next = prev.next.next
                    head = head.next
                    continue
            prev = head
            head = head.next
        return res

    # better solution
    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        res = head
        while head:
            if head.val == val:
                if prev:
                    prev.next = head.next
                else:
                    res = head.next
            else:
                prev = head
            head = head.next
        return res
