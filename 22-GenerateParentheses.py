__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/generate-parentheses/
date: 03-01-2016
----------------
problem:
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
----------------
searching
"""


class Solution(object):
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     list = self.generate(0, 0, n)
    #     return list

    # def generate(self, left, right, n):
    #     list1 = []
    #     list2 = []
    #     if left < n:
    #         list1 = self.generate(left + 1, right, n)
    #     if left > right:
    #         list2 = self.generate(left, right + 1, n)
    #     if left == n:
    #         return [")" * (left - right)]
    #     for i in range(len(list1)):
    #         list1[i] = "(" + list1[i]
    #     for j in range(len(list2)):
    #         list2[j] = ")" + list2[j]
    #     return list1 + list2

    # optimized version
    def generateParenthesis(self, n):
        list = []
        self.generate(n, n, "", list)
        return list

    def generate(self, left, right, str, list):
        if left == 0:
            list.append(str + ")" * right)
            return
        if left > 0:
            self.generate(left - 1, right, str + "(", list)
        if right > left:
            self.generate(left, right - 1, str + ")", list)
