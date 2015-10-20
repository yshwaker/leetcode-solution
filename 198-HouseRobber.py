__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/house-robber/
date: 10-20-2015
----------------
problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
----------------
Dynamic Programming
money[i] = max(money[i - 2] + w(i), money[i - 1])
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        money = [0] * (length + 1)
        money[1] = nums[0]
        for i in range(2, length + 1):
            money[i] = max(money[i - 2] + nums[i - 1], money[i - 1])
        return money[length]
