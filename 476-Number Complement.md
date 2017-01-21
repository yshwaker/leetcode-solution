# Code

## Description

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

## Python Solution
```
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_bit = 0
        temp = num
        while temp:
            num_bit += 1
            temp /= 2
        return num ^ (2**(num_bit) - 1)
```

```
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        while i <= num:
            i = i << 1
        return num ^ (i - 1)
```
## Some thinking

find which bits to flip

use XOR to flip bits
