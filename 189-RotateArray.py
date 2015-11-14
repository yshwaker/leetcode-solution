__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/rotate-array/
date: 11-13-2015
----------------
problem:
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
----------------
"""

# something like this:
# [1,2,3,4,5,6,7]
# [1,2,3,1,5,6,7] temp = 4
# [1,2,3,1,5,6,4] temp = 7
# [1,2,7,1,5,6,4] temp = 3
# [1,2,7,1,5,3,4] temp = 6
# [1,6,7,1,5,3,4] temp = 2
# [1,6,7,1,2,3,4] temp = 5
# [5,6,7,1,2,3,4] temp = 1


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = nums[0]
        start = 0
        t = start
        for count in range(len(nums)):
            t = (t + k) % len(nums)
            temp, nums[t] = nums[t], temp
            # if there is a cycle, move forward one step
            if t == start:
                t = (t + 1) % len(nums)
                start = t
                temp = nums[t]
            print t
