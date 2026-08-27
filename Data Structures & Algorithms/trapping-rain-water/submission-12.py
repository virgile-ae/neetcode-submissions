from itertools import pairwise

class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0
        # start, area
        # continue until area >= otherwise pick next max
        # peaks = []

        # for i, h in enumerate(height):
        #     left = i == 0 or height[i-1] < h
        #     right = i == len(height) - 1 or height[i+1] < h

        #     if left and right:
        #         peaks.append(i)

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
            
        print(peak_stack)
        print(filtered_peaks)



        total_area = 0
        for l, r in pairwise(sorted(filtered_peaks + peak_stack)):
            total_area += min(height[l], height[r]) * (r - l - 1)
            # area = (i - last_peak_idx - 1) * last_peak
            for h in height[l + 1:r]:
                total_area -= h

        # if last_peak_idx is not None:
        #     total_area += self.trap(height[last_peak_idx + 1:])
    
        return total_area

