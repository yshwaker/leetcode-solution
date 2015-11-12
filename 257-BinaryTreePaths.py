__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/binary-tree-paths/
date: 11-11-2015
----------------
problem:
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            self.dfs(root, "")
        return self.paths

    def dfs(self, root, path):
        if root:
            if not path:
                path = str(root.val)
            else:
                path += ("->" + str(root.val))
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)
        if not root.left and not root.right:
            self.paths.append(path)
