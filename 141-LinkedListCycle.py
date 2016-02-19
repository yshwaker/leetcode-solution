__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/linked-list-cycle/
date: 02-19-2016
----------------
problem:
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
----------------
if revere the linked list. if it has a cycle in it, then it will go back to
head.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        front = head
        rear = head.next
        print head.val
        print head.next.val
        while rear:
            if head == rear:
                return True
            temp = rear.next
            rear.next = front
            front = rear
            rear = temp
            if front == head:
                return True
        else:
            return False
