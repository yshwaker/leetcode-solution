from collections import deque

__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/symmetric-tree/
date: 10-20-2015
----------------
problem:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # iteratively
    def isSymmetric1(self, root):
        if not root:
            return True
        left = deque()
        right = deque()
        left.append(root.left)
        right.append(root.right)
        while left and right:
            left_cur = left.pop()
            right_cur = right.pop()
            if not left_cur and not right_cur:
                continue
            if not left_cur or not right_cur:
                return False
            if left_cur.val == right_cur.val:
                left.append(left_cur.left)
                left.append(left_cur.right)
                right.append(right_cur.right)
                right.append(right_cur.left)
            else:
                return False
        return True

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    # recursively
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False
        if left.val != right.val:
            return False
        if self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right):
            return True
        else:
            return False
