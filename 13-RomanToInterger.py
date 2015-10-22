__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/roman-to-integer/
date: 10-19-2015
----------------
problem:
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
----------------
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                if self.val(s[i]) < self.val(s[i + 1]):
                    sum += self.val(s[i + 1]) - self.val(s[i])
                    i += 2
                    continue
            sum += self.val(s[i])
            i += 1
        return sum

    def val(self, s):
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        elif s == 'M':
            return 1000
