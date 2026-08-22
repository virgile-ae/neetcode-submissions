from math import prod
import operator
from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        prefix = list(accumulate(nums, operator.mul))
        suffix = list(accumulate(reversed(nums), operator.mul))

        results = []

        results.append(suffix[-2])

        for i in range(1, len(nums) - 1):
            results.append(prefix[i - 1] * suffix[l - i - 2])

        results.append(prefix[-2])

        return results
