__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/number-of-1-bits/
date: 10-18-2015
----------------
problem:
Write a function that takes an unsigned integer and returns
the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.
----------------

"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n == 0:
            return 0
        while n / 2 > 0:
            if n % 2 == 1:
                count += 1
            n /= 2
        return count + 1
