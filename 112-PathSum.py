__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/path-sum/
date: 10-22-2015
----------------
problem:
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                return True
        if root.left:
            if self.hasPathSum(root.left, sum - root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, sum - root.val):
                return True
        return False
