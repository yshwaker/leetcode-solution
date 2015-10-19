__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/valid-anagram/
date: 10-18-2015
----------------
problem:
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
Note:
You may assume the string contains only lowercase alphabets.
----------------
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        for i in range(len(t)):
            if t[i] in d:
                d[t[i]] -= 1
            else:
                d[t[i]] = 1
        for item in d:
            if d[item] != 0:
                return False
        else:
            return True
