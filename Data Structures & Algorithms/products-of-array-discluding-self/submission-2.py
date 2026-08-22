from math import prod
import operator
from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        prefix = list(accumulate(nums, operator.mul))
        suffix = list(accumulate(reversed(nums), operator.mul))

        results = []

        # print(prefix)
        # print(suffix)
        results.append(suffix[-2])

        for i in range(1, len(nums) - 1):
            # print(f'{i=} {prefix[i-1]=} {suffix[l-i-2]=}')
            results.append(prefix[i - 1] * suffix[l - i - 2])

        results.append(prefix[-2])

        # 2 4 6
        # prefix
        # 2  8  48
        # suffix
        # 6  24 48

        # prefix[i - 1] * suffix[len - i - 1]


        return results
