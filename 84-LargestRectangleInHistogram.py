#! /usr/bin/env python
# -*- coding:utf-8 -*-
from collections import deque


class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        procedure:
        maintain a stack and the value of the top element of stack(namely current).
        each element in the stack consists of the bar height and
        the max width of area it can form yet.
        for each value V in the array, compare it with the current.
        if it's smaller, pop the top element and calculate its area using height*width
        repeat until the top element is smaller than new element V.
        else push it to the stack.
        """
        stack = deque()
        current = -1
        max_area = 0
        for val in height:
            if current < val:
                stack.append((val, 1))
                # print "push: %d 1" % val
                current = val
            elif current == val:
                v, c = stack.pop()
                # print "pop: %d %d" % (v, c)
                stack.append((v, c + 1))
                # print "push: %d %d" % (v, c + 1)
            else:
                max_area = self.calcArea(stack, val, max_area)
                current = val
        max_area = self.calcArea(stack, -1, max_area)
        return max_area

    def calcArea(self, stack, new_val, max_area):
        count = 0
        while True:
            if not stack:
                stack.append((new_val, count + 1))
                # print "push: %d %d" % (new_val, count + 1)
                return max_area
            else:
                element = stack.pop()
                # print "pop: %d %d" % (element[0], element[1])
                value = element[0]
            if value >= new_val:
                count += element[1]
                area = value * count
                max_area = max(max_area, area)
            elif value == new_val:
                count += element[1]
            else:
                stack.append(element)
                stack.append((new_val, count + 1))
                # print "push: %d %d" % (new_val, count + 1)
                return max_area


def main():
    array = [4, 2, 0, 3, 2, 4, 3, 4]
    sol = Solution()
    print sol.largestRectangleArea(array)

if __name__ == "__main__":
    main()
