__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/reverse-string/
date: 05-24-2016
----------------
problem:
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
----------------
"""


class Solution(object):

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
