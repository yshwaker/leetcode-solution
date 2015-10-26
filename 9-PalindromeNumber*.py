__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/palindrome-number/
date: 10-26-2015
----------------
problem:
Determine whether an integer is a palindrome. Do this without extra space.
----------------
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        a = x
        b = x
        bit_num = 0
        while x > 0:
            x /= 10
            bit_num += 1
        i = 1
        while i <= bit_num:
            left = a / 10**(bit_num - i)
            right = b % 10
            if left != right:
                return False
            a -= left * 10**(bit_num - i)
            b /= 10
            i += 1
        return True
