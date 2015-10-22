__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/factorial-trailing-zeroes/
date: 10-22-2015
----------------
problem:
Given an integer n, return the number of trailing zeroes in n!.
----------------
To see how many 5 factors there are. the number of 5s is more than the number of 2s
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 0:
            num += n / 5
            n /= 5
        return num
