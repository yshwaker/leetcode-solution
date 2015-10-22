from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/implement-stack-using-queues/
date: 10-22-2015
----------------
problem:
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

----------------
"""


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.queue1:
            self.queue1.append(x)
            if self.queue2:
                self._move(self.queue2, self.queue1)
        elif not self.queue2:
            self.queue2.append(x)
            self._move(self.queue1, self.queue2)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queue1:
            self.queue1.popleft()
        else:
            self.queue2.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False

    def _move(self, q_from, q_to):
        while q_from:
            q_to.append(q_from.popleft())
