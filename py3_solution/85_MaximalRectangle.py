class Solution:
    def maximalRectangle(self, M: List[List[str]]) -> int:
        if not M:
            return 0
        
        m, n = len(M), len(M[0])
        lay = M[0]
        lay = [int(v) for v in lay]
        maxRec = self.largestRectangleArea(lay)
        for i in range(1, m):
            lay = [lay[j] + 1 if M[i][j] == '1' else 0 for j in range(n)]
            maxRec = max(maxRec, self.largestRectangleArea(lay))
        
        return maxRec
         
    def largestRectangleArea(self, H):
        stc = [-1]
        maxRec = 0
        H.append(-1)
        
        for i, val in enumerate(H):
            while H[stc[-1]] > val:
                h = H[stc.pop()]
                maxRec = max(maxRec, (i - stc[-1] - 1) * h)
                
            stc.append(i)
            
        return maxRec
