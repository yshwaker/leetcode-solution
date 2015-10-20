__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/power-of-two/
date: 10-20-2015
----------------
problem:
Given an integer, write a function to determine if it is a power of two.
----------------
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        if n == 1:
            return True
        if n <= 0:
            return False
