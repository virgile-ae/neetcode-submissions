def area(index1: int, index2: int, heights: list[int]) -> int:
    return abs(index1 - index2) * min(heights[index1], heights[index2])


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            a = area(l, r, heights)

            if a > max_area:
                max_area = a

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
