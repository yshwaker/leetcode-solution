# Code

## Description

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

## Python Solution
1. using stack
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
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while carry or len(s1) or len(s2):
            num = carry
            if len(s1):
                num += s1.pop()
            if len(s2):
                num += s2.pop()
            carry, num = divmod(num, 10)

            newNode = ListNode(num)
            newNode.next = head
            head = newNode
        return head
```

2. recursively
```
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        diff = self.getLen(l1) - self.getLen(l2)
        dummy = ListNode(0)
        if (diff >= 0):
            dummy.next = self.getNextNode(l1, l2, diff)
        else:
            dummy.next = self.getNextNode(l2, l1, -diff)
        if dummy.next.val >= 10:
            dummy.next.val %= 10
            dummy.val = 1
            return dummy
        else:
            return dummy.next

    # get the next node based on the current node
    def getNextNode(self, l1, l2, diff):
        if not (l1 and l2):
            return None
        if diff != 0:
            curr = ListNode(l1.val)
            nxt = self.getNextNode(l1.next, l2, diff - 1)
        else:
            curr = ListNode(l1.val + l2.val)
            nxt = self.getNextNode(l1.next, l2.next, diff)
        if nxt and nxt.val >= 10:
            curr.val += 1
            nxt.val %= 10
        curr.next = nxt
        return curr



    def getLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

```
basic idea is: when I want to calculate the digit on certain position, I need to consider whether the result of next position is greater than 10, than I can calculate the digit on my current position. And this forms a recursive formula.

3. basic idea is: maintain a pointer(flag) to a position on new created linked list such that all digit on the right side of the position is 9. if carry occurs, all nodes after flag will become 0, and flag itself will self-increment.
```
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        diff = self.getLen(l1) - self.getLen(l2)
        if diff < 0:
            diff = -diff
            l1, l2 = l2, l1
        dummy = ListNode(0)
        curr = flag = dummy
        while diff > 0:
            curr.next = ListNode(l1.val)
            curr = curr.next
            if l1.val != 9:
                flag = curr
            diff -= 1
            l1 = l1.next
        while l1:
            new_node = ListNode(l1.val + l2.val)
            if new_node.val > 9:
                new_node.val %= 10
                flag.val += 1
                flag = flag.next
                while flag:
                    flag.val = 0
                    flag = flag.next
            curr.next = new_node
            curr = curr.next
            if curr.val < 9:
                flag = curr

            l1 = l1.next
            l2 = l2.next
        return dummy if dummy.val == 1 else dummy.next

    def getLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
```

## Complexity

time: O(n)
