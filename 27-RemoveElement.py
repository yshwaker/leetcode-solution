__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/remove-element/
date: 10-20-2015
----------------
problem:
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
----------------
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        near = 0
        rear = len(nums) - 1
        length = len(nums)
        while near <= rear:
            if nums[near] != val:
                near += 1
                continue
            if nums[rear] == val:
                rear -= 1
                length -= 1
                continue
            nums[near], nums[rear] = nums[rear], nums[near]
        return length
