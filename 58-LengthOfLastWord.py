__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/length-of-last-word/
date: 11-02-2015
----------------
problem:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
----------------
"""


class Solution(object):
    # solution using API
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.rstrip(" ").split(" ")
        if len(words):
            return len(words[-1])

    # general solution
    def lengthOfLastWord1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in reversed(s):
            if i != ' ':
                length += 1
            elif i == ' ' and length != 0:
                return length
        return length
