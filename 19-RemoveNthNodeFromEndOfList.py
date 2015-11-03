__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
date: 11-02-2015
----------------
problem:
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
----------------
track the Nth node from the current node.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = head
        count = 0
        mark = None
        while head:
            if count == n:
                mark = res
            elif count > n:
                mark = mark.next
            count += 1
            if head.next:
                head = head.next
            else:
                break
        # remove the first node, ep. [1,2,3] remove 3rd node
        if not mark:
            return res.next
        else:
            mark.next = mark.next.next
        return res
