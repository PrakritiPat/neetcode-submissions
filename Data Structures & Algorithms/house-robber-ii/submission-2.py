class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==1: 
            return nums[0]
      
        def rob_line(houses):

            m = len(houses)
            if m == 1: 
                return houses[0]
            
            dp = [0] * m
            dp[0] = houses[0]
            dp[1] = max(houses[0],houses[1])

            for i in range(2,m):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1]) 
            return dp[m-1]


        return max(rob_line(nums[:-1]),rob_line(nums[1:]))

   



        