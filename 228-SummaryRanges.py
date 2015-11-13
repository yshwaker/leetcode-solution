__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/summary-ranges/
date: 11-12-2015
----------------
problem:
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
----------------
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums:
            return []
        if len(nums) == 1:
            ranges.append(str(nums[0]))
            return ranges
        head = nums[0]
        last = nums[0]
        for i in range(1, len(nums)):
            if last + 1 == nums[i]:
                last = nums[i]
            else:
                if head == last:
                    ranges.append(str(head))
                else:
                    ranges.append(str(head) + "->" + str(last))
                head = nums[i]
                last = nums[i]
        if head == last:
            ranges.append(str(head))
        else:
            ranges.append(str(head) + "->" + str(last))
        return ranges
