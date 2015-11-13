__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/valid-palindrome/
date: 11-12-2015
----------------
problem:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
----------------
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        near = 0
        rear = len(s) - 1
        while near <= rear:
            if not self.isAlphanumeric(s[near]):
                near += 1
                continue
            if not self.isAlphanumeric(s[rear]):
                rear -= 1
                continue
            if s[near] != s[rear]:
                return False
            else:
                near += 1
                rear -= 1
        return True

    def isAlphanumeric(self, c):
        if "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9":
            return True
        else:
            return False
