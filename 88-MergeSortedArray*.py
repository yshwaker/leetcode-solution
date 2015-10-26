__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/merge-sorted-array/
date: 10-26-2015
----------------
problem:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
----------------
merge from back to front
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        last1 = m - 1
        last2 = n - 1
        total = m + n - 1
        while last2 >= 0:
            if last1 < 0:
                nums1[total] = nums2[last2]
                last2 -= 1
            elif nums1[last1] > nums2[last2]:
                nums1[total] = nums1[last1]
                last1 -= 1
            else:
                nums1[total] = nums2[last2]
                last2 -= 1
            total -= 1
