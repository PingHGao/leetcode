class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea, indl, indr = 0, 0, len(height) - 1
        while indl < indr:
            vl = height[indl]
            vr = height[indr]
            
            area = min(vl, vr) * (indr - indl)
            maxarea = max(maxarea, area)
            
            if vl < vr:
                indl += 1
            else:
                indr -= 1
                
        return maxarea
