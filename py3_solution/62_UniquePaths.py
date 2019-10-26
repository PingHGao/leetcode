class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m
            
        steps = m + n - 2
        paths = 1
        for i in range(m - 1):
            paths = (steps - i) * paths / (i + 1)
            
        return int(paths)
            
