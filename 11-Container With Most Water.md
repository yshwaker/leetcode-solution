# Code

## Description

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

## Python Solution
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volumn = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                volumn = max(volumn, height[i] * (j - i))
                i += 1
            else:
                volumn = max(volumn, height[j] * (j - i))
                j -= 1
        return volumn
```
## Some thinking

essentially，we want to maximize min(height[i], height[j]) * (j-i), while i < j.

And for certain pair (i j), if height[i] <= height[j], then we can say the result is great than any pair (i k) that i < k < j. vice versa.

We choose to traverse the array from two side so that we can ingore the most number of pairs and have a better performance.

## Complexity

Time: O(n)
Space: O(1)
