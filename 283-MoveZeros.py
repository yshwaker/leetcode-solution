__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/move-zeroes/
date: 10-7-2015
----------------
problem:
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
---------------
"""


class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        cur_pt = 0
        zero_pt = 0
        zero_count = 0
        while cur_pt < len(nums):
            if nums[cur_pt] == 0:
                if zero_count == 0:
                    zero_pt = cur_pt
                zero_count += 1
            else:
                if zero_count > 0:
                    nums[cur_pt], nums[zero_pt] = nums[zero_pt], nums[cur_pt]
                    zero_pt += 1
            cur_pt += 1
