# 方法一：暴力搜索
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        h, w = len(matrix), len(matrix[0])
        dp = [[1] * w for i in range(h)]
        
        maxS = 0
        for i,j in itertools.product(range(h), range(w)):
            if matrix[i][j] == '0':
                continue
            
            # find max Square with (i, j) being top-left Corner
            l = dp[i][j]
            while i + l < h and j + l < w:
                isSqr = True
                for n in range(j, j + l + 1):
                    if matrix[i + l][n] == '0':
                        isSqr = False
                        break
                
                if isSqr:
                    for m in range(i, i + l):
                        if matrix[m][j + l] == '0':
                            isSqr = False
                            break
                
                if isSqr:
                    l += 1
                else:
                    break

            maxS = max(maxS, l * l)
            for m, n in itertools.product(range(i, i + l), range(j, j + l)):
                dp[m][n] = min(i + l - m, j + l - n)
                
        return maxS
                    
# 方法2：动态规划
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        h, w = len(matrix), len(matrix[0])
        dp = [[0] * w for i in range(h)]
        
        maxl = 0
        for i in range(h):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] > 0:
                maxl = 1
        
        for j in range(w):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] > 0:
                maxl = 1
        
        for i,j in itertools.product(range(1, h), range(1, w)):
            if matrix[i][j] == '0':
                continue
                
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            
            maxl = max(maxl, dp[i][j])
        
        return maxl**2
