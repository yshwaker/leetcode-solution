# Code

## Description
Find the sum of all left leaves in a given binary tree.

Example:
```
<!--
    3
   / \
  9  20
    /  \
   15   7
 -->
```
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

## Python Solution
```
class Solution(object):
    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root is not None:
            if root.left is not None:
                if self.isLeaf(root.left):
                    sum += root.left.val
                else:
                    sum += self.sumOfLeftLeaves(root.left)
            if root.right is not None:
                sum += self.sumOfLeftLeaves(root.right)
        return sum

```

## Some thinking
tree traverse
