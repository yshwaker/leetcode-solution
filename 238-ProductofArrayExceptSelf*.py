__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/product-of-array-except-self/
date: 02-10-2016
----------------
problem:
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
----------------
for an array [a, b, c, d]
our output is [bcd, acd, abd, abc]
we can regard it as the product of the following arrays
[1, a, ab, abc]
[bcd, cd, d, 1]
which can be generated in O(n)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[i - 1] * nums[i - 1])
        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp *= nums[i + 1]
            res[i] *= temp
        return res
