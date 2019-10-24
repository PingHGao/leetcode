class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lenS = len(s)
        if lenS == 0:
            return 0
        
        dp = [0] * lenS
        
        for i in range(lenS - 1):
            if s[i] == '(' and s[i + 1] == ')':
                if i - 1 >= 0:
                    dp[i + 1] = dp[i - 1] + 2
                else:
                    dp[i + 1] = 2
                    
            elif s[i] == ')' and s[i + 1] == ')':
                ind = i - dp[i]
                if ind >= 0 and s[ind] == '(':
                    dp[i + 1] = dp[i] + 2
                    if ind - 1 >= 0:
                        dp[i + 1] = dp[i + 1] + dp[ind - 1]
                        
        return max(dp)
