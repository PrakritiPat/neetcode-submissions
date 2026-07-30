class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) # make nums into set because then its more efficent to check if something is in a set
        longest = 0
        for n in nums: 
            if (n-1) not in numset:
                length = 0
                while (length+n) in numset: 
                    length+=1
                longest = max(length,longest)
        return longest


            
                
                


        

        