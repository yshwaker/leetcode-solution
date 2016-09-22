__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/house-robber-iii/
date: date
----------------
problem:
The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called the "root." Besides the root, each house has
one and only one parent house. After a tour, the smart thief realized that "all
houses in this place forms a binary tree". It will automatically contact the
police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without
alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
----------------
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.findMax(root, False), self.findMax(root, True))

    # flag = true if the parent of root is stolen, false otherwise.
    def findMax(self, root, flag):
        if not root:
            return 0
        if flag is False:
            max_value = max(root.val + self.findMax(self.left, True) + self.findMax(self.right, True),
                            self.findMax(self.left, False), self.findMax(self.right, False))
        else:
            max_value = self.findMax(self.left, False) + self.findMax(self.right, False)
        return max_value
