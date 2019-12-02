class Solution:
    def searchMatrix(self, M, T):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not M:
            return False
        
        if not M[0]:
            return False
        
        h, w = len(M), len(M[0])
        
        i, j = h - 1, 0
        while 1:
            if M[i][j] == T:
                return True
            
            if M[i][j] > T:
                i -= 1
                if i < 0:
                    return False
            
            if M[i][j] < T:
                j += 1
                if j >= w:
                    return False
