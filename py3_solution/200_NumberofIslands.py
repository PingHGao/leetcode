class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        from itertools import product
        
        h, w = len(grid), len(grid[0])
        
        flag = [[0 for j in range(w)] for i in range(h)]
        
        def grouping(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return
            
            if flag[i][j] == 1 or grid[i][j] == '0':
                return
            
            flag[i][j] = 1
            grouping(i - 1, j)
            grouping(i + 1, j)
            grouping(i, j - 1)
            grouping(i, j + 1)

        num = 0
        for i, j in product(range(h), range(w)):
            if grid[i][j] == "0" or flag[i][j] == 1:
                continue
            
            grouping(i, j)
            num += 1
                
        return num
                        
                
