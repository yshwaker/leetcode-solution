# Code

## Python Solution
```
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        counts = [0] * (num + 1)
        counts[0] = 0

        for i in range(num + 1):
            counts[i] = counts[i >> 1] + i % 2
        return counts
```

## Some thinking

After some try through some examples, I realized it's a DP problem. If we have a number with n bits, we want to know what digit of each bit is. We can calculate the lowest bit number by modulus operation of 2. what's left is a number of n-1 bits and we want to count bits of this new number which is a the same problem on a smaller scale. That lead to a equation of DP.
