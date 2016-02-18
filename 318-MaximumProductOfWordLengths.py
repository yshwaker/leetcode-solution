__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/maximum-product-of-word-lengths/
date: 02-17-2016
----------------
problem:
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
----------------
Transform the word into a binary number of 26 bits,
each bit stands for occurrence of the order of character.
If two words have common character,
then their binary numbers must have at least one bit on which the values are 1.
we can find them using & bit operation.

"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) <= 1:
            return 0
        val_list = []
        for word in words:
            val = 0
            for c in word:
                val |= 1 << (ord(c) - ord('a'))
            val_list.append(val)
        max_product = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if (val_list[i] & val_list[j]) == 0:
                    if max_product < len(words[i]) * len(words[j]):
                        max_product = len(words[i]) * len(words[j])
        return max_product
