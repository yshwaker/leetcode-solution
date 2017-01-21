# Code

## Description

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

## Python Solution
```
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = cur_num = 0
        for num in nums:
            if num == 0:
                max_num = max(max_num, cur_num)
                cur_num = 0
            else:
                cur_num += 1
        max_num = max(max_num, cur_num)
        return max_num
```
