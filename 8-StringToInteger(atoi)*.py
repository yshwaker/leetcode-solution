import string
__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/string-to-integer-atoi/
date: 11-13-2015
----------------
problem:
mplement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
----------------
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(string.whitespace)
        num = None
        sign = 1
        for i in str:
            if num is None:
                if i == "+":
                    sign = 1
                    num = 0
                elif i == "-":
                    sign = -1
                    num = 0
                elif "0" <= i <= "9":
                    num = ord(i) - ord("0")
                else:
                    return 0
            else:
                if "0" <= i <= "9":
                    val = ord(i) - ord("0")
                    if sign == 1:
                        if num > 214748364 or (num == 214748364 and val > 7):
                            return 2147483647
                    if sign == -1:
                        if num > 214748364 or (num == 214748364 and val > 8):
                            return -2147483648
                    num = num * 10 + val
                else:
                    break
        if num is not None:
            return num * sign
        else:
            return 0
