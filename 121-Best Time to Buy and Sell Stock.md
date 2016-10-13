# Code

## Description
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

## Python Solution
```
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profitMax = 0

        minPrice = float("Inf")
        for price in prices:
            profitMax = max(profitMax, price - minPrice)
            minPrice = min(minPrice, price)
        return profitMax

```

## Some thinking

max difference: find max(prices[j] – prices[i]) ，i < j.

on each day, we maintain a minimum price and maxProfit so far.

we iterate price from day 0 to day n, since we must buy and then sell.
MaxProfit on day i can only be done by buying stocking with minimum price between day 0 to day i-1.
