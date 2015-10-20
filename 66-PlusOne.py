__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/plus-one/
date: 10-20-2015
----------------
problem:
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
----------------
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        for i in reversed(range(len(digits))):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] += flag
                flag = 0
        if flag == 1:
            return [1] + digits
        else:
            return digits
