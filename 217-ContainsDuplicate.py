__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/contains-duplicate/
date: 10-12-2015
----------------
problem:
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
---------------
hash
"""


class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = dict()
        for num in nums:
            if num in counts:
                return True
            else:
                counts[num] = 1
        return False

# using set instead


class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = set()
        for num in nums:
            if num in counts:
                return True
            else:
                counts.add(num)
        return False
