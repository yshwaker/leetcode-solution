# Code

## Description

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

## Python Solution
```
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        nums = self.origin[:]
        length = len(nums)
        for i in range(length - 1):
            rand_index = random.randint(i, length - 1)
            nums[i], nums[rand_index] = nums[rand_index], nums[i]
        return nums
```
## Some thinking

pick a number from [i, end](including i itself)

## Complexity

time: O(n)
