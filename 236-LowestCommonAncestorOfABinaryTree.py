__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
date: 10-12-2015
----------------
problem:
Given a binary search tree (BST), find the lowest common ancestor (LCA)
of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2, since a node can be a
descendant of itself according to the LCA definition.
-----------------

it's a more general version of problem #235
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # found at least one node in subtree
        if root == p or root == q:
                return root
        # found one node in both subtrees
        elif left and right:
            return root
        # found node in left tree
        elif left:
            return left
        # found node in right tree
        elif right:
            return right
        # not found
        else:
            return None
