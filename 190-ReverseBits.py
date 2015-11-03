__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/reverse-bits/
date: 11-2-2015
----------------
problem:
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
----------------
"""


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit = n % 2
            if bit == 1:
                res += 2**(31 - i)
            n /= 2
        return res
