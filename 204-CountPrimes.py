__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/count-primes/
date: 11-12-2015
----------------
problem:
Count the number of prime numbers less than a non-negative number, n.
----------------
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * (n + 1)
        for i in range(2, int(math.floor(math.sqrt(n))) + 1):
            if nums[i] == 1:
                continue
            j = i
            while j * i <= n:
                nums[j * i] = 1
                j += 1
        sum = 0
        for i in range(2, n):
            if nums[i] == 0:
                sum += 1
        return sum
