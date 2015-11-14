__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/excel-sheet-column-title/
date: 11-13-2015
----------------
problem:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
----------------
how to compute character by offset?
chr(ord('A') + i)

(n - 1) % 26 + 1 can make mutiple of 26 mod 26 equals 26
*  n -= (n - 1) % 26
*  n /= 26
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = ""
        while n > 0:
            c = chr(ord('A') + (n - 1) % 26)
            str = c + str
            n -= (n - 1) % 26
            n /= 26
        return str
