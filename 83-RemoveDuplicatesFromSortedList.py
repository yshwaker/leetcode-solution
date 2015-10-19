__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
date: 10-19-2015
----------------
problem:
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
----------------
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        while head:
            if head.next:
                if head.next.val == head.val:
                    head.next = head.next.next
                    continue
            head = head.next
        return start
