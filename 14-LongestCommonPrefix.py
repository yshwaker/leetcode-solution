__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/longest-common-prefix/
date: 11-3-2015
----------------
problem:
Write a function to find the longest common prefix string amongst an array of strings.
----------------
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        for i in range(len(strs[0])):
            if self.check(strs, i, strs[0][i]):
                prefix += strs[0][i]
            else:
                return prefix
        return prefix

    def check(self, strs, i, char):
        for string in strs:
            if i >= len(string) or string[i] != char:
                return False
        return True
