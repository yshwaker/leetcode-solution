from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/min-stack/
date: 11-13-2015
----------------
problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
----------------
basic idea:
maintain an additional stack which only push data that is no greater than top of the data
if push[3,2,1,2,1]
then this stack contains [3,2,1,1]

"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.real = deque()
        self.min_deque = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.real.append(x)
        if not self.min_deque:
            self.min_deque.append(x)
        else:
            if self.min_deque[-1] >= x:
                self.min_deque.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.real and self.min_deque:
            if self.real[-1] == self.min_deque[-1]:
                self.min_deque.pop()
            self.real.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.real[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_deque[-1]
