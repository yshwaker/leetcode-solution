# Code

## Description
Given  an arbitrary  ransom  note  string and another string containing letters from  all the magazines,  write a function that will return true if the ransom  note can be constructed from the magazines ; otherwise, it will return false.  

Each letter  in  the  magazine string can  only be  used once  in  your ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

## Python Solution
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lowerLetters = [0] * 26;
        for i in range(len(magazine)):
            index = ord(magazine[i]) - ord('a')
            lowerLetters[index] += 1
        for i in range(len(ransomNote)):
            index = ord(ransomNote[i]) - ord('a')
            lowerLetters[index] -= 1
        for i in range(len(lowerLetters)):
            if lowerLetters[i] < 0:
                return False
        return True

```

## Some thinking
Refer to 389.find The Difference
