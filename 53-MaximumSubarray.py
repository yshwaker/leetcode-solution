__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/maximum-subarray/
date: 03-01-2016
----------------
problem:
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
----------------
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) dynamic programming
        #
        # max_sum = nums[0]
        # cur_sum = nums[0]
        # for i in range(1, len(nums)):
        #     cur_sum = max(cur_sum + nums[i], nums[i])
        #     max_sum = max(max_sum, cur_sum)
        # return max_sum
