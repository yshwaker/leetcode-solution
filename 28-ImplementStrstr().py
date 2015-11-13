__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/implement-strstr/
date: 11-12-2015
----------------
problem:
Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
----------------
TESTCASE:
"as2asd"
"asd"
"asdasd"
"aa"
""
""
"a"
""
""
"a"
"aaa"
"aaaa"
** "mississippi"
** "issip"
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        iter = 0
        first = -1
        if not needle:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[iter]:
                if first == -1:
                    first = i
                iter += 1
            else:
                iter = 0
                if first != -1:
                    i = first
                    first = -1
            if iter == len(needle):
                return first
            i += 1
        if iter != len(needle):
                return -1
