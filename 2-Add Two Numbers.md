# Code

## Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

## Python Solution
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            newNode = ListNode(val)
            cur.next = newNode
            cur = newNode
        return dummy.next


```
## Some thinking

special case:
1. l1 longer than l2
2. l2 longer than l1
3. l1 and l2 both finished adding and carry is 1 at that time.

## Complexity
time: O(N)
space: O(N)


## more concised version coming from Discussion
```
class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
```
