class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minPs = [[0] * n for row in range(m)]
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    minPs[r][c] = grid[r][c]
                    continue
                
                valR = float("inf") if c + 1 >= n else minPs[r][c + 1]
                valD = float("inf") if r + 1 >= m else minPs[r + 1][c]
                
                minPs[r][c] = grid[r][c] + min(valR, valD)
        
        return minPs[0][0]
    
    
