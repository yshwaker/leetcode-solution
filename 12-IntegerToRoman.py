__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/integer-to-roman/
date: 02-15-2016
----------------
problem:
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
----------------
subtractive notation only includes I X C
such as IX, not VIV.

some test cases:
1   "I"
44  "XLIV"
9   "IX"
99  "XCIX"
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ""
        roman = ["M", "D", "C", "L", "X", "V", "I"]
        val = [1000, 500, 100, 50, 10, 5, 1]
        for i in range(len(roman) - 1):
            count = num / val[i]
            num = num % val[i]
            if i % 2 == 0 and num / val[i + 2] == 9:
                str = str + roman[i] * count + roman[i + 2] + roman[i]
                num = num % val[i + 2]
            elif i % 2 == 1 and num / val[i + 1] == 4:
                str = str + roman[i] * count + roman[i + 1] + roman[i]
                num = num % val[i + 1]
            else:
                str = str + roman[i] * count
        str = str + "I" * num
        return str
