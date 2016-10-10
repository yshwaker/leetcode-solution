# Code

## Description
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Python Solution
```
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        carry = 0
        res = ""

        while len1 > 0 or len2 > 0 or carry :
            digit1 = int(num1[len1 - 1]) if len1 > 0 else 0
            digit2 = int(num2[len2 - 1]) if len2 > 0 else 0

            add_sum = digit1 + digit2 + carry
            carry = (add_sum) / 10
            res = str((add_sum) % 10) + res

            len1 -= 1
            len2 -= 1
        return res

```

## Some thinking

same way as adding two numbers by hand.
