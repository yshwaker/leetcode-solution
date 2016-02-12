__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/missing-number/
date: 02-11-2016
----------------
problem:
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
----------------
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        n = len(nums)
        return n * (n + 1) / 2 - sum

    # add append the array with [0,1,2,3,4,5,..,n], then the problem is just
    # like #136. find the only number that occurs once in the array while other
    # numbers occur twice.
    # use the property of XOR
    def missingNumber2(self, nums):
        miss = 0
        for num in nums:
            miss = miss ^ num
        for i in range(len(nums) + 1):
            miss = miss ^ i
        return miss
