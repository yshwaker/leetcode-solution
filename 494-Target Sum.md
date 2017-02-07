# Code

## Description

https://leetcode.com/problems/target-sum/?tab=Description

## Python Solution

1. dfs with memorization
```
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        cache = {}

        return self.dfs(nums, 0, S, cache)

    def dfs(self, nums, index, S, cache):
        if (index, S) in cache:
            return cache[(index, S)]
        if index >= len(nums):
            if S == 0:
                return 1
            else:
                return 0
        res = self.dfs(nums, index + 1, S - nums[index], cache) + self.dfs(nums, index + 1, S + nums[index], cache)
        cache[(index, S)] = res
        return res
```
## Some thinking

thinking

## Complexity

Complexity
