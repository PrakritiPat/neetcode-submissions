from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        high = max(piles)
        while (lo < high):
            k = lo + (high-lo) // 2
            hour = 0
            for pile in piles: 
                hour += ceil(pile/k)
            if hour <= h: 
                high = k 

            else: 
                lo = k+1
        return lo 

        