__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/excel-sheet-column-number/
date: 10-18-2015
----------------
problem:
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
----------------
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            sum += 26**i * (ord(s[len(s) - 1 - i]) - ord('A') + 1)
        return sum
