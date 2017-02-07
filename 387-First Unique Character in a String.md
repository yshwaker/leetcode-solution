# Code

## Description

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

## Python Solution
```
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            letters[index] += 1

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if letters[index] == 1:
                return i
        return -1
```
