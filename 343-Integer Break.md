# Code

## Description

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Hint:

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

## Python Solution
```
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [1,2,4,6,9]
        for i in range(7, n + 1):
            opt.append(3 * opt[i - 3 - 2])
        return opt[n - 2]
```
## Some thinking

regularities from 7 to n: opt(n) = 3 * opt(n-3)


Explanation from discussion:

Given a number n lets say we have a possible product P = p1 * p2 * ... pk. Then we notice what would happen if we could break pi up into two more terms lets say one of the terms is 2 we would get the terms pi-2 and 2 so if 2(pi-2) > pi we would get a bigger product and this happens if pi > 4. since there is one other possible number less then 4 that is not 2 aka 3. Likewise for 3 if we instead breakup the one of the terms into pi-3 and 3 we would get a bigger product if 3*(pi-3) > pi which happens if pi > 4.5.

Hence we see that all of the terms in the product must be 2's and 3's. So we now just need to write n = a3 + b2 such that P = (3^a) * (2^b) is maximized. Hence we should favor more 3's then 2's in the product then 2's if possible.

So if n = a*3 then the answer will just be 3^a.

if n = a3 + 2 then the answer will be 2(3^a).

and if n = a3 + 22 then the answer will be 2 * 2 * 3^a

The above three cover all cases that n can be written as and the Math.pow() function takes O(log n) time to preform hence that is the running time.
```
public class Solution {
    public int integerBreak(int n) {
        if(n == 2)
            return 1;
        else if(n == 3)
            return 2;
        else if(n%3 == 0)
            return (int)Math.pow(3, n/3);
        else if(n%3 == 1)
            return 2 * 2 * (int) Math.pow(3, (n - 4) / 3);
        else
            return 2 * (int) Math.pow(3, n/3);
    }

}
```
