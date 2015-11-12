__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/add-binary/
date: 11-11-2015
----------------
problem:
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
----------------
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        flag = 0
        res = ""
        for i in range(max(len(a), len(b)) + 1):
            indexA = len(a) - 1 - i
            indexB = len(b) - 1 - i
            if indexA < 0 and indexB < 0:
                if flag == 0:
                    return res
                else:
                    return "1" + res
            elif indexA < 0:
                bit = int(b[indexB]) + flag
            elif indexB < 0:
                bit = int(a[indexA]) + flag
            else:
                bit = int(a[indexA]) + int(b[indexB]) + flag
            if bit == 0:
                res = "0" + res
                flag = 0
            elif bit == 1:
                res = "1" + res
                flag = 0
            elif bit == 2:
                res = "0" + res
                flag = 1
            else:
                res = "1" + res
                flag = 1
