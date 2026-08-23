class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start,sums):

            if sums == target:
                res.append(path[:])
                return 
            if sums > target:
                return 

            for i in range(start,len(nums)):

                path.append(nums[i])
                backtrack(i, sums + nums[i])
                path.pop()

        backtrack(0,0)
        return res
      
            
                
               

                
            
        
            


        