__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/happy-number/
date: 10-19-2015
----------------
problem:
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
----------------
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        path = [n]
        sum = 0
        while sum != 1:
            sum = 0
            numbers = []
            while n > 0:
                numbers.append(n % 10)
                n /= 10
            for num in numbers:
                sum += num**2
            if sum in path:
                return False
            path.append(sum)
            n = sum
        return True
