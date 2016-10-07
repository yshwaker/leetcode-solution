# Code

## Description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

## Python Solution
```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lowerLetters = [0] * 26
        upperLetters = [0] * 26
        hasOdd = False
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                index = ord(s[i]) - ord('a')
                lowerLetters[index] += 1
            elif 'A' <= s[i] <= 'Z':
                index = ord(s[i]) - ord('A')
                upperLetters[index] += 1
        length = 0
        for i in range(26):
            if lowerLetters[i] % 2:
                hasOdd = True
                length += lowerLetters[i] / 2 * 2
            else:
                length += lowerLetters[i]
            if upperLetters[i] % 2:
                hasOdd = True
                length += upperLetters[i] / 2 * 2
            else:
                length += upperLetters[i]
        return length + 1 if hasOdd else length

```

using `collections` datatypes
```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        hasOdd = 0
        counter = collections.Counter(s)
        for c in counter:
            if counter[c] % 2:
                hasOdd += 1
                length += counter[c] - 1
            else:
                length += counter[c]
        return length + (hasOdd > 0)
```

## Some thinking
create a hash table.
special case: "ccc"
