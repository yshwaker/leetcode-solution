__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/word-pattern/
date: 11-3-2015
----------------
problem:
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
----------------
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        d = {}
        dd = {}
        # projection: pattern -> words
        for i in range(len(pattern)):
            if i >= len(words):
                return False
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                d[pattern[i]] = words[i]
        # projection: words -> pattern
        for i in range(len(words)):
            if i >= len(pattern):
                return False
            if words[i] in dd:
                if dd[words[i]] != pattern[i]:
                    return False
            else:
                dd[words[i]] = pattern[i]
        return True
