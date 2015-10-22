from collections import deque
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/binary-tree-level-order-traversal/
date: 10-22-2015
----------------
problem:
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
----------------
Similar to #107
"""


class Solution(object):
    def levelOrder(self, root):
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
        return levels
