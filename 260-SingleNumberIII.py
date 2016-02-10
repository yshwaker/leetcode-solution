__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/single-number-iii/
date: 02-09-2016
----------------
problem:
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
----------------

just like #136, we use XOR.
First we xor all the numbers in the array, what remains is the xor of two elements that appear only once.
Then we look at each bit of this number we get. if the value on one bit is 1, then we can say the two elements we are looking for are different on this bit.
then we can split the array into two array according to the value on that bit.
we are sure numbers that occured twice will be put into the same array.
so when we xor all numbers in each array respectively, we can get those two numbers we need.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor = num ^ xor
        tester = 1
        while xor != 0:
            if xor & tester != 0:
                break
            tester *= 2
        num1 = 0
        num2 = 0
        for num in nums:
            if num & tester == 0:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num
        return [num1, num2]
