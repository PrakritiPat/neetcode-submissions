class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   # important to handle duplicates
        result = []

        def dfs(index, path):
            result.append(path[:])   # add current subset

            for i in range(index, len(nums)):
                # skip duplicates
                if i > index and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return result
            
            
                

        