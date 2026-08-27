from itertools import pairwise

class Solution:
    def trap(self, height: List[int]) -> int:
        filtered_peaks = []
        peak_stack = []

        for peak in range(len(height)):
            if not peak_stack:
                peak_stack.append(peak)
                continue

            while len(peak_stack) > 1 and height[peak_stack[-1]] < height[peak]:
                peak_stack.pop()

            if height[peak_stack[-1]] < height[peak]:
                filtered_peaks.append(peak_stack.pop())

            peak_stack.append(peak)
            
        total_area = 0
        for l, r in pairwise(sorted(filtered_peaks + peak_stack)):
            total_area += min(height[l], height[r]) * (r - l - 1)
            for h in height[l + 1:r]:
                total_area -= h
    
        return total_area

