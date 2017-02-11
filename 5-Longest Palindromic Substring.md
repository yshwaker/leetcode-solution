# Code

## Description

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

## Python Solution

first attemption
```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 1
        start_pos = 0
        for i in range(len(s)):
            for j in reversed(range(len(s))):
                if i > j or j - i + 1 < max_length:
                    break
                if s[i] == s[j] and self.checkPalindromic(s, i, j):
                    if max_length < j - i + 1:
                        max_length = j - i + 1
                        start_pos = i
        return s[start_pos:start_pos + max_length]


    def checkPalindromic(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

another way (extend palindrome):
```
class Solution(object):

    def __init__(self):
        self.max_length = 1
        self.start_pos = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in xrange(len(s) - 1):
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i + 1)
        return s[self.start_pos:self.start_pos + self.max_length]


    def extendPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if self.max_length < right - left - 1:
            self.max_length = right - left - 1
            self.start_pos = left + 1

```

improved:
```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 1
        start_pos = 0
        i = 0
        while i < len(s):
            left = i
            right = i
            # skip duplicate chars (improve performance)
            while right < len(s) - 1 and s[right] == s[right+1]:
                right += 1
            i = right + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if max_length < right - left - 1:
                max_length = right - left - 1
                start_pos = left + 1
        return s[start_pos:start_pos + max_length]
```

## Complexity

time: O(n^2)
