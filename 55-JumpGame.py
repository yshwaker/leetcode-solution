#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DFS Time Limit Exceeded(naive idea)
        # -----
        # frontier = deque()
        # frontier.appendleft(0)
        # explored = set()
        # end = len(nums) - 1
        # if 0 == end:
        #         return True
        # while len(frontier) != 0:
        #     state = frontier.popleft()
        #     if state not in explored:
        #         explored.add(state)
        #         if nums[state] + state < len(nums) - 1:
        #             max = nums[state] + state + 1
        #         else:
        #             return True
        #         for i in range(state, max):
        #             if i == end:
        #                 return True
        #             frontier.appendleft(i)
        # return False
        # 
        # -----
        # Time Complexity: O(n)
        max_length = 0
        i = 0 
        while i <= max_length and i < len(nums):
            if nums[i] + i >= len(nums) - 1:
                return True
            else:
                max_length = max(max_length, nums[i] + i)
            i += 1
        return False



