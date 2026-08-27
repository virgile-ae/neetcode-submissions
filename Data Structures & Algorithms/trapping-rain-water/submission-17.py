from itertools import pairwise
import heapq

class Solution:
    def trap(self, height: List[int]) -> int:
        filtered = []
        stack = []

        for i in range(len(height)):
            if not stack:
                stack.append(i)
                continue

            while len(stack) > 1 and height[stack[-1]] < height[i]:
                stack.pop()

            if height[stack[-1]] < height[i]:
                filtered.append(stack.pop())

            stack.append(i)

        total_area = 0
        for l, r in pairwise(filtered + stack):
            total_area += min(height[l], height[r]) * (r - l - 1)
            for h in height[l + 1:r]:
                total_area -= h
    
        return total_area

