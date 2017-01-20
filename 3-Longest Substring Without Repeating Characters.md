# Code

## Description

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Python Solution
```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charSet = set()
        left = right = 0
        maxLength = 0
        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
            else:
                maxLength = max(maxLength, right - left)
                while left < right:
                    if s[left] != s[right]:
                        charSet.remove(s[left])
                        left += 1
                    else:
                        left += 1
                        break
            right += 1
        maxLength = max(maxLength, right - left)
        return maxLength
```

improve:
```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charSet = {}
        maxLength = 0
        left = 0
        for i in range(len(s)):
            if s[i] in charSet and left <= charSet[s[i]]:
                maxLength = max(maxLength, i - left)
                left = charSet[s[i]] + 1
            charSet[s[i]] = i
        maxLength = max(maxLength, len(s) - left)
        return maxLength

```


## Some thinking

set/hash to detect duplication

## Complexity

time: o(N)
space: O(N)
