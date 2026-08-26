class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nums = set(numbers)

        for i, num in enumerate(numbers):
            if target - num in nums:
                return [i + 1, numbers[i + 1:].index(target - num) + i + 2]

        raise RuntimeError('no valid combination')
        
        