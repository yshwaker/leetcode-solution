__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/climbing-stairs/
date: 10-19-2015
----------------
problem:
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
----------------
dynamic programming:
s[i] = s[i - 1] + s[i - 2]
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        s = [0] * (n + 1)
        s[1] = 1
        s[2] = 2
        for i in range(3, n + 1):
            s[i] = s[i - 1] + s[i - 2]
        return s[n]
