__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/pascals-triangle/
date: 10-22-2015
----------------
problem:
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
----------------
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        levels = [[]] * numRows
        levels[0] = [1]
        if numRows == 1:
            return levels
        levels[1] = [1, 1]
        if numRows == 2:
            return levels
        for i in range(2, numRows):
            level = [1]
            for j in range(1, i):
                level.append(levels[i - 1][j - 1] + levels[i - 1][j])
            level.append(1)
            levels[i] = level
        return levels
