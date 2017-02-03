# Code

## Description

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

## Python Solution
```
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        res = []
        for num in nums1:
            dict[num] = 1

        for num in nums2:
            if num in dict and dict[num] == 1:
                res.append(num)
                dict[num] += 1
        return res
```

sort
```
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(res) == 0 or res[-1] < nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
```
## Some thinking

thinking

## Complexity

Complexity
