# Code

## Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## Python Solution

Brute Force
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in xrange(len(nums) - 1):
            for j in xrange (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

Hash
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_hash = {}

        for i in xrange(len(nums)):
            if ((target - nums[i]) in num_hash):
                return [num_hash[target - nums[i]], i]
            num_hash[nums[i]] = i
```

## Complexity

brute-force: O(n^2)  
hash: time -> O(n) space -> O(n)
