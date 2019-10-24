class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        R = n // 2
        
        for r in range(R):
            for i in range(r, n - 1 - r):
                matrix[0 + r][0 + i], matrix[0 + i][n - r - 1], matrix[n - r - 1][n - 1 - i], matrix[n - 1 - i][0 + r] = \
                matrix[n - 1 - i][0 + r], matrix[0 + r][0 + i], matrix[0 + i][n - r - 1], matrix[n - r - 1][n - 1 - i]
