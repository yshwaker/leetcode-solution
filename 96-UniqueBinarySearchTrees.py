__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/unique-binary-search-trees/
date: 02-20-2016
----------------
problem:
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
----------------
Dynamic Programming:
As a BST,
for a give root i, its left child tree contains [1...i-1], right child tree
contains [i+1... n], so the number of unique BST then stores 1...n depends on
the number of unique BST than stores 1...i-1 and i+1...n, for any i in [1...n].

And we can see storing [i+1, n] is the same as strong [1, n-i], with respect to
the number of unique BSTs. So what really matters is the size of the tree.

Counts[i] = sum(Counts[0...k] * counts([ k+1....i]))     0<=k<i-1
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = []
        counts.append(0)
        counts.append(1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        for j in range(2, n + 1):
            count = 0
            for i in range(j):
                count += max(counts[i], 1) * max(counts[j - 1 - i], 1)
            counts.append(count)
        return counts[n]
