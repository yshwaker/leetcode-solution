__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/single-number-ii/
date: 02-22-2016
----------------
problem:
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
----------------
accumulate the value of each bit of each number and mod it by 3, the numbers
left are the values of each bit of the specal number

NOTE:
for python, if the value of int overflows, the number will automatically
converted to long. So we need to consider the negative numbers as special case.

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        result = 0
        negative = 0
        for j in range(len(nums)):
            num = nums[j]
            if num < 0:
                negative += 1
                num = -num
            for i in range(32):
                if (num >> i) & 1:
                    bits[i] += 1
        for i in range(32):
            result |= (bits[i] % 3) << i
        if negative % 3:
            return -result
        else:
            return result
