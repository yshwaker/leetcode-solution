from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/valid-parentheses/
date: 11-3-2015
----------------
problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
----------------
not forget to check if stack is empty when pop from stack, i.e. when reading ')',']','}'
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        for i in s:
            if i == '(':
                stack.append(1)
            elif i == '[':
                stack.append(2)
            elif i == '{':
                stack.append(3)
            elif i == ')':
                if not stack or stack.pop() != 1:
                    return False
            elif i == ']':
                if not stack or stack.pop() != 2:
                    return False
            elif i == '}':
                if not stack or stack.pop() != 3:
                    return False
        if stack:
            return False
        else:
            return True
