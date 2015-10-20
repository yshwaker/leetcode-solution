from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
date: 10-20-2015
----------------
problem:
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        level = 0
        levels = []
        cur = []
        while queue:
            node = queue.popleft()
            if node[1] == level:
                cur.append(node[0].val)
            else:
                level = node[1]
                levels.append(cur)
                cur = []
                cur.append(node[0].val)
            if node[0].left:
                queue.append((node[0].left, level + 1))
            if node[0].right:
                queue.append((node[0].right, level + 1))
        levels.append(cur)
        return levels[::-1]
