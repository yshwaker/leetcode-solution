"""
source: https://leetcode.com/problems/majority-element/
date: 10-18-2015
----------------
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
----------------
what a good idea with O(n)
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        majority = None
        for i in nums:
            if count == 0:
                majority = i
                count += 1
            else:
                count = count + 1 if i == majority else count - 1
                if count > len(nums) / 2:
                    return majority
        return majority
