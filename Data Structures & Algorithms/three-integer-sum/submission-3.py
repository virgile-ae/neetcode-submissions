class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triples = set()
        counts = Counter(nums)

        for i in range(len(nums) - 2):
            num_i = nums[i]

            if counts[num_i] == 1:
                del counts[num_i]
            else:
                counts[num_i] -= 1
                
            remaining = dict(counts)
            for j in range(i + 1, len(nums) - 1):
                num_j = nums[j]
                target = -(num_i + num_j)

                if remaining[num_j] == 1:
                    del remaining[num_j]
                else:
                    remaining[num_j] -= 1

                if target in remaining:
                    triples.add(tuple(sorted([num_i, num_j, target])))
            


        return list(triples)