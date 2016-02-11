__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
date: 02-09-2016
----------------
problem:
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
----------------

only buy at local minimum, sell at local maximum.
  
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        is_buy = False
        buy_price = 0
        for i in range(len(prices) - 1):
            if is_buy is False:
                if prices[i] < prices[i + 1]:
                    buy_price = prices[i]
                    is_buy = True
            else:
                if prices[i] > prices[i + 1]:
                    profit += (prices[i] - buy_price)
                    is_buy = False
        if is_buy is True:
            profit += (prices[-1] - buy_price)
        return profit
