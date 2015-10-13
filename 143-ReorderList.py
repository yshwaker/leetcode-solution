#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/reorder-list/
date: 10-5-2015
----------------
problem:
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You must do this in-place without altering the nodes' values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
---------------
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create(n):
    "test component"
    next_node = ListNode(n)
    n -= 1
    while n > 0:
        node = ListNode(n)
        node.next = next_node
        next_node = node
        n -= 1
    return next_node


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        procedure:
        1.find the middle node
        2.reverse the linked list from mid node to the end
        3.interleave two linked list
        """
        if head is None:
            return
        count = 0
        begin = head
        # find mid position
        while head is not None:
            count += 1
            head = head.next
        mid = count / 2 + 1
        # find mid element and reverse the linked list from mid
        head = begin
        while mid > 0:
            if mid == 1:
                # temp = head.next
                # head.next = None
                # head = temp
                head.next, head = None, head.next
            else:
                head = head.next
            mid -= 1
        end = self.reverse(head)
        # interleaving
        head = begin
        tail = end
        head_next = None
        tail_next = None
        while tail is not None:
            head_next = head.next
            tail_next = tail.next
            tail.next = head.next
            head.next = tail
            head = head_next
            tail = tail_next
        # self.traverse(begin)

    def reverse(self, head):
        prev = None
        current = head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev

    # test component
    def traverse(self, head):
        while head is not None:
            print head.val,
            head = head.next
        print ""


# Test Case
def main():
    sol = Solution()
    head = create(10)
    sol.reorderList(head)

if __name__ == "__main__":
    main()
