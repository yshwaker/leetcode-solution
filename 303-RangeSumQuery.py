__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/range-sum-query-immutable/
date: 11-11-2015
----------------
problem:
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
*There are many calls to sumRange function.
----------------
"""


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            self.sum = []
        else:
            self.sum = [0] * len(nums)
            self.sum[0] = nums[0]
            for i in range(1, len(nums)):
                self.sum[i] = self.sum[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.sum[j] - self.sum[i - 1]
        else:
            return self.sum[j]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
