from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/binary-tree-preorder-traversal/
date: 02-14-2016
----------------
problem:
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        frontier = deque()
        frontier.append(root)
        while(frontier):
            node = frontier.pop()
            res.append(node.val)
            if node.right:
                frontier.append(node.right)
            if node.left:
                frontier.append(node.left)
        return res

    # simplified
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        frontier = deque()
        frontier.append(root)
        while(frontier):
            node = frontier.pop()
            if node:
                res.append(node.val)
                frontier.append(node.right)
                frontier.append(node.left)
        return res
