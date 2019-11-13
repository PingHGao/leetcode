class Solution:
    def maxProfit(self, P: List[int]) -> int:
        if not P:
            return 0
        
        minBef, maxPro = P[0], 0
        for v in P:
            pro = v - minBef
            maxPro = pro if pro > maxPro else maxPro
            
            minBef = min(minBef, v)
            
        return maxPro
