class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        
        dp = [[-1] * n for i in range(m)]
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        for i in range(1, m):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i - 1][0] + 1

        for j in range(1, n):
            if word1[0] == word2[j]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j - 1] + 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] != -1:
                    continue

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m - 1][n - 1]
