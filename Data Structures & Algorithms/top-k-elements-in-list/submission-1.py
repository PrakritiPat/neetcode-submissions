class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}

        for n in nums: 
            hashset[n] = hashset.get(n,0) +1
        
        return sorted(hashset, key = lambda n:hashset[n], reverse = True) [:k]
        


        
        
