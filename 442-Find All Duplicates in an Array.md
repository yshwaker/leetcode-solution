# Code

## Description

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

## Python Solution
```
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # to differentiate between those disappeared and those appeared.
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        # to differentiate between those twice and the other.
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -nums[index]

        result = []
        for i in range(len(nums)):
            if nums[i] < 0:
                result.append(i + 1)
        return result
```

improved(one pass):
```
res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res
```
## Some thinking

1. store information in index
