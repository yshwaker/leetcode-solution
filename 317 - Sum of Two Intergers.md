# Code

## Python Solution
```
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) & MOD
            a = (a ^ b) & MOD
            b = (carry << 1) & MOD
        return a if a <= MAX_INT else ~(a ^ MOD)
```

## Some thinking

when we add two Intergers, we basiclly add two numbers in each bit (binary) with maybe a carry added to next bit.

We can first take some examples by hand, and soon we find there are only 4 situations in each bit, which is:

0 + 0 = 0 no carry<br>
1 + 0 = 1 no carry<br>
0 + 1 = 1 no carry<br>
1 + 1 = 0 with carry<br>

Without carry, we find the operation is just the same as `^` bit operation.

As for carry, the pattern is the same as & bit operation. the obly problem is it need to be added to the next bit, which can be solved by `<<` (left shift 1 bit).

So the problem of add two Int a and b can be transformed to a problem of adding `(a ^ b)` and `(a & b) << 1`. Although it is still a sum, but if we keep doing this, the carry will eventually become 0(it makes sence when we do sum by hand).

In other languages, when the result go beyond 32-bit, the extra part will be dropped. However in Python, when we add two int beyond the max 32-bit int, python can treat this number as a signed 64-bit int.

for example:
 0x00000001  -> 0x0000000000000001
 0xFFFFFF00  -> 0xFFFFFFFFFFFFFF00 (bits higher than sign bit are all 1)

after `&` and `^` operations, we take the lower 32bit since we don't care higher bits.

When final result comes, it may be larger than maximum `MAX_INT`. the carry will overwrite the sign bit to 1. if treated as int, it is a negative number. So we need to change it so that it becomes the same negative number as 64bit int.
somthing like:

0000..00001xxx...xxx  ->  1111...11111xxx.xxx

It's done by first inverting lower 32bits and then inverting all 64bits.
