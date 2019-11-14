class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        
        for i in range(len(s)):
            si = s[:i + 1]
            inWD = False
            for w in wordDict:
                lw = len(w)
                if lw > i + 1:
                    continue
                if si[-lw:] == w:
                    lrem = i - lw
                    if lrem < 0 or dp[lrem]:
                        inWD = True
                        break
            dp[i] = inWD
        
        return dp[-1]
