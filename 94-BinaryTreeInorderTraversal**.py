from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/binary-tree-inorder-traversal/
date: 02-18-2016
----------------
problem:
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
----------------
go to it left child if it can and push itself to stack to remeber where it come
from when it can not go any further.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = deque()
        while stack or root:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
