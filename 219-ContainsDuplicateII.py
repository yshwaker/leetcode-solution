__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/contains-duplicate-ii/
date: 11-3-2015
----------------
problem:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
----------------
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                if i - numDict[nums[i]] <= k:
                    return True
            numDict[nums[i]] = i
            i += 1
        return False
