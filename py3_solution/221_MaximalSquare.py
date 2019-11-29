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
                    
