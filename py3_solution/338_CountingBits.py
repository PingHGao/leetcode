class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        
        ans = [0] * (num + 1)
        ans[1] = 1
        maxfac = 2
        for i in range(2, num + 1):
            if maxfac * 2 < i:
                maxfac *= 2
            ans[i] = ans[i % maxfac] + 1
            
        return ans
