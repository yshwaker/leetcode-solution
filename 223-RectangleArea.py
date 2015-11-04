__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/rectangle-area/
date: 11-3-2015
----------------
problem:
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
  .------------.(C,D)
  |            |
  |       .----+-----.(G,H)
  |       |    |     |
  |_______|____|     |
 (A,B)    |          |
     (E,F)|__________|

Assume that the total area is never beyond the maximum possible value of int.
----------------
get the bottom left corner and top right corner of the overlapping rectangle
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        crossA = max(A, E)
        crossB = max(B, F)
        crossC = min(C, G)
        crossD = min(D, H)
        crossArea = 0
        if crossA < crossC and crossB < crossD:
            crossArea = (crossC - crossA) * (crossD - crossB)
        area = (C - A) * (D - B) + (G - E) * (H - F) - crossArea
        return area
