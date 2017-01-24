# Code

## Description

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

## Python Solution
```
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        median = nums[len(nums) / 2]
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves
```

using QuickSelect:
```
from random import shuffle
def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(nums)
        # median = nums[len(nums) / 2]
        # moves = 0
        # for num in nums:
        #     moves += abs(num - median)
        # return moves

        shuffle(nums)
        median = self.findMedian(nums)
        print median
        return sum(abs(num - median) for num in nums)

    def findMedian(self, nums):
        n = len(nums)
        return self.getKth(nums, n/2+1, 0, n - 1)

    def getKth(self, nums, k, start, end):
        pivot = nums[end]
        left = start
        right = end
        while True:
            while nums[left] < pivot and left < right:
                left += 1
            while nums[right] >= pivot and left < right:  # nums[end](a.k.a pivot) will never be swapped
                right -= 1
            if left == right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        nums[end], nums[left] = nums[left], nums[end]  # put pivot into right pos
        if left + 1 == k:
            return nums[left]
        elif left + 1 < k:
            return self.getKth(nums, k, left + 1, end)
        else:
            return self.getKth(nums, k, start, left - 1)  # left-1 won't out-of-range since k>=1

    # another version
    def getKth(self, nums, k, start, end):
        pivot = nums[end]
        storeIndex = start
        for i in range(start, end):
            if nums[i] < pivot:
                nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
                storeIndex += 1
        nums[end], nums[storeIndex] = nums[storeIndex], nums[end]

        if storeIndex + 1 == k:
            return nums[storeIndex]
        elif storeIndex + 1 < k:
            return self.getKth(nums, k, storeIndex + 1, end)
        else:
            return self.getKth(nums, k, start, storeIndex - 1)
```

Other way to findMedian: Min-Heap

## Some thinking

1. When using QuickSelect, don't forget to shuffle array ahead of time. if not, the worst case will be O(N^2), which will exceed the time limit.

## Complexity

1. time: O(nlgn)
2. time: ~N  n + n/2 + n/4 + .. + 1 < 2n    
