__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/bulb-switcher/
date: 02-11-2016
----------------
problem:
There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round,
you toggle every third bulb (turning on if it's off or turning off if it's on).
For the nth round, you only toggle the last bulb.
Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
----------------
find the pattern given a n.
nth bulbs =   1 2 3 4 5 ...
toggle times: 0 1 1 2 1 3 1 3 2 3 1 5 1 3 3 4 1 5 1 5 3 3 1 7 2
1:off 0:on    0 1 1 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 0
"on" numbers  1 1 1 2 2 2 2 2 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 5
              1     4         9             16                25
for a bulb i, no matter how many bulbs there are, its state is certain.
"""


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        i = 1
        while True:
            if i**2 <= n < (i + 1)**2:
                return i
            i += 1
