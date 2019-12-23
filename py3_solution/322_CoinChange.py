class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if amount is 0:
            return 0
        
        money = set(coins)
        num = 1
        while 1:
            if amount in money:
                return num
            if min(money) > amount:
                return -1
            
            money = {m + c for m in money for c in coins}
            num += 1
        
