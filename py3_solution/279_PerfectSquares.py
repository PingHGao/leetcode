class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        
        powers = set([i*i for i in range(int(n**0.5) + 1)])
        
        def bfs(nums):
            if powers & nums:
                return 1
            newnums = set()
            newnums.update({num - p for num in nums for p in powers if num > p})
            return bfs(newnums) + 1
        
        return bfs(set([n]))
