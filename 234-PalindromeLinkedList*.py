__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/palindrome-linked-list/
date: 11-11-2015
----------------
problem:
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
----------------
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        mid = self.findMiddle(head)
        p2 = self.reverse(mid)
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def findMiddle(self, head):
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        return p1

    def reverse(self, head):
        p = None
        while head:
            q = head
            head = head.next
            q.next = p
            p = q
        return p
