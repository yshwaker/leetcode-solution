# Code

## Description

https://leetcode.com/problems/hamming-distance/

## Python Solution
```
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num = x ^ y
        count = 0
        while num:
            if num % 2:
                count += 1
            num = num >> 1
        return count
```
## Some thinking

bit difference: XOR operation

one way to count the number of positions at which the bit is 1:
count = 0
while (num):
    count += 1
    num = num & (num - 1)
