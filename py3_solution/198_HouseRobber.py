class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                dp[0] = n
                continue
            if i == 1:
                dp[1] = max(nums[:2])
                continue
                
            dp[i] = max(n + dp[i - 2], dp[i - 1])
            
        return dp[-1]
