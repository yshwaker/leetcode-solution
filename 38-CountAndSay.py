__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/count-and-say/
date: 11-3-2015
----------------
problem:
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
----------------
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            oldStr = self.countAndSay(n - 1)
            last = 0
            count = 0
            newStr = ""
            for i in oldStr:
                if last == 0:
                    last = i
                    count += 1
                else:
                    if last == i:
                        count += 1
                    else:
                        newStr += (str(count) + str(last))
                        last = i
                        count = 1
            newStr += (str(count) + str(last))
            return newStr
