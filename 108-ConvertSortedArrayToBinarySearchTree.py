__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
date: 02-27-2016
----------------
problem:
Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.
----------------]
hint: divide and conquer
the property of BST:
each value of node in left subtree of a node is smaller than its value while
the value in right subtree is larger.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.formBST(nums, 0, len(nums) - 1)
        return root

    def formBST(self, nums, left, right):
        if left <= right:
            mid = left + (right - left) / 2
            node = TreeNode(nums[mid])
            node.left = self.formBST(nums, left, mid - 1)
            node.right = self.formBST(nums, mid + 1, right)
            return node
        else:
            return None
