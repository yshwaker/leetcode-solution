__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/reverse-integer/
date: 11-11-2015
----------------
problem:
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
----------------
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x < 0:
            sign = -1
            x = -x
            maxInt = 2**31
        else:
            sign = 1
            maxInt = 2**31 - 1
        while x:
            t = x % 10
            print rev, maxInt / 10
            if rev > maxInt / 10:
                return 0
            rev = rev * 10 + t
            x /= 10
        return rev * sign
