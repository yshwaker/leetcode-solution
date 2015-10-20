__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/balanced-binary-tree/
date: 10-20-2015
----------------
problem:
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            if -1 <= self.height(root.left) - self.height(root.right) <= 1:
                return True
        return False

    def height(self, root):
        if not root:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
