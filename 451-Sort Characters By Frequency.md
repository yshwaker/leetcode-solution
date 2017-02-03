# Code

## Description

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

## Python Solution
```
import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqDict = {}
        for c in s:
            if c in freqDict:
                freqDict[c] += 1
            else:
                freqDict[c] = 1
        freqHeap = []
        for c, freq in freqDict.iteritems():
            heapq.heappush(freqHeap, (-freq, c))
        res = ""
        while freqHeap:
            item = heapq.heappop(freqHeap)
            res = res + item[1] * (-item[0])
        return res
```

bucket-sort method:
```
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqDict = {}
        maxFreq = 0
        for c in s:
            if c in freqDict:
                freqDict[c] += 1
            else:
                freqDict[c] = 1
            maxFreq = max(maxFreq, freqDict[c])
        buckets = [""] * (maxFreq + 1)
        for c, freq in freqDict.iteritems():
            buckets[freq] += (c * freq)
        result = ""
        for substring in reversed(buckets):
            result += substring
        return result
```
## Some thinking

1. hashmap to calculate frequences.

2. heap to sort based on frequence.

3. similar to No.347.

## Complexity

1. time: O(nlgn) space: O(n)
2. time: O(n) space: O(n)
