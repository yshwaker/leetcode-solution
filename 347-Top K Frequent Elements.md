# Code

## Description

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Python Solution
```
import heapq
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = defaultdict(int)
        freq_heap = []
        result = []
        for num in nums:
            freq_dict[num] += 1
        for num in freq_dict:
            heapq.heappush(freq_heap, (-freq_dict[num], num))
        for i in range(k):
            pop_item = heapq.heappop(freq_heap)
            result.append(pop_item[1])
        return result
```

bucket:
```
freq_dict = defaultdict(int)
        result = []
        max_freq = 0
        for num in nums:
            freq_dict[num] += 1
            max_freq = max(max_freq, freq_dict[num])
        freq_buckets = [None] * (max_freq + 1)
        for num in freq_dict:
            if freq_buckets[freq_dict[num]]:
                freq_buckets[freq_dict[num]].append(num)
            else:
                freq_buckets[freq_dict[num]] = [num]
        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            if freq_buckets[i]:
                for num in freq_buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
```
## Some thinking

1. negate frequency to implement a max heap.

2. defaultdict(int) is useful for counting. (don't forget the argument!)

3. similar to No.451

4. can not initialize 2d array using [[]] * 10, use [None] * 10 instead.

## Complexity

time: O(nlgn) hash and heapsort
space: O(n)
