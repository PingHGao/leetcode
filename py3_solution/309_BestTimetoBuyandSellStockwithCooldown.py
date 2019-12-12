class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        cdp, buyp, sellp = 0, -prices[0], 0
        for i in range(1, len(prices)):
            cd = sellp
            sell = max(sellp, buyp + prices[i])
            buy = max(buyp, cdp - prices[i])
            
            cdp, buyp, sellp = cd, buy, sell
            
        return max(cdp, sellp)
