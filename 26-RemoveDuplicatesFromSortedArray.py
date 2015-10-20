__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
date: 10-20-2015
----------------
problem:
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
----------------
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        near = 0
        rear = 0
        while rear < len(nums):
            if nums[rear] == nums[near]:
                rear += 1
            else:
                near += 1
                nums[near] = nums[rear]
                rear += 1
        return near + 1
