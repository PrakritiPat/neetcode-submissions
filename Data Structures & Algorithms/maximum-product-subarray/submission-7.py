class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [1] * n
        min_dp = [1] * n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        

        for i in range(1,n): 
            prev_min = min_dp[i-1]
            prev_max = max_dp[i-1]
            max_dp[i] = max(nums[i],prev_min *nums[i], prev_max*nums[i])
            min_dp[i] = min(nums[i],prev_min *nums[i], prev_max*nums[i])




        return max(max_dp)
            

     

