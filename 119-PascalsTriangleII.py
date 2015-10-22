__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/pascals-triangle-ii/
date: 10-22-2015
----------------
problem:
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
----------------
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        last = [1, 1]
        for i in range(2, rowIndex + 1):
            level = [1]
            for j in range(1, i):
                level.append(last[j - 1] + last[j])
            level.append(1)
            last = level
        return last
