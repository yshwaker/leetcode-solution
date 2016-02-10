__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/single-number/
date: 2016-02-09
----------------
problem:
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
----------------

XOR:
since a ^ (b ^ c) = (a ^ b) ^ c,
and   a ^ b = b ^ a
and   b ^ b = 0 (a ^ b ^ b = a)

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for num in nums:
            x = x ^ num
        return x
