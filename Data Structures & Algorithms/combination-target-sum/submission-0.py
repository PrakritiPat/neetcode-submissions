class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(index,path,total):
            if sum(path) == target: 
                result.append(path[:])
                return

            if index >= len(nums) or total > target:
                return 
            
            path.append(nums[index])
            dfs(index,path,total + nums[index])
            path.pop()

            dfs(index+1, path, total)

        dfs(0,[],0)
        return result
            
            
            
                
               

                
            
        dfs(0,[])
        return result
                   
                    

                


                  
                
            


        