# Code

## Description
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

## Python Solution
```
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = -1
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] == target:
                return [i + 1, i + 2]
            elif numbers[i] + numbers[i + 1] > target:
                mid = i
                break
        left = mid
        right = mid + 1
        while left >= 0 and right < len(numbers):
            print numbers[left] + numbers[right]
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                left -= 1
            else:
                right += 1
```

## Some thinking

When meet a sorted array, the first thing comes to my mind is splitting array into two part.

First get a example and try to solve it by hand.

for example [1, 3, 5, 7, 10] and target 11.
after some attempts, we find a group [1,3,5] that can never find two numbers that fit the target, since the largest two number's sum is still smaller than target. On the other hand, cannot find out the correct number only in the remaining numbers. So there is must be one number in [1,3,5] and one number in [7,10].

In a more general case, we can alse draw a line to split the array. What's more interesting is that we search the first part from right to left, search the second part from left to right and finally find the result.

Assume we are look at two particular numbers, num[left] , num[right].

if num[left] + num[right] > target, then we can make sure num[left] is not the one we need. because if num[left] is the correct one, then plus another number larger than num[right] will definitely larger than target.

Similar situation when num[left] + num[right] < target.

finally we'll find the correct two numbers, since Description has guaranteed that each input would have exactly one solution.
