class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            c = 0
            for j in range(0, i):
                c += dp[j] * dp[i - j - 1]
            dp[i] = c
            
        return dp[-1]
