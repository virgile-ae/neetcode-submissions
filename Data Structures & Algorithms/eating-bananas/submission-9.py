def isValid(piles: List[int], h: int, k: int) -> bool:
    return sum(math.ceil(pile / k) for pile in piles) <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = sum(piles)
        optimal = upper // h
        
        l = max(optimal, 1)
        r = upper

        while l < r:
            k = (l + r) // 2
            if isValid(piles, h, k):
                r = k;
            else:
                l = k + 1;

        return l