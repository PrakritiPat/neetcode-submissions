class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(index,path):
            #base case
            if index == len(nums):
                result.append(path[:]) 
                return 
            
            #choice 1 keeping the nums[index]:
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            #choice 2 not keeping nums[index]:
            backtrack(index+1, path)

        backtrack(0,[])
        return result













        