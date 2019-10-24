class Solution:
    def trap(self, height: List[int]) -> int:
        lenH = len(height)
        lb = 0
        cont = 0
        while lb < lenH:
            rb = lb + 1
            vlb = height[lb]
            while rb < lenH:
                vrb = height[rb]
                if vrb > vlb:
                    break
                rb += 1
                
            rb = lenH - 1 if rb >= lenH else rb
            
            if vlb < height[rb]:
                c = (rb - lb - 1) * vlb
                for i in range(lb + 1, rb):
                    c -= height[i]
                cont += c
                lb = rb
            else:
                break
        
        rbn = lenH - 1
        while rbn >= lb:
            lbn = rbn - 1
            vrb = height[rbn]
            while lbn >= lb:
                vlb = height[lbn]
                if vlb >= vrb:
                    break
                lbn -= 1
                
            if vlb >= vrb:
                c = (rbn - lbn - 1) * vrb
                for i in range(lbn + 1, rbn):
                    c -= height[i]
                cont += c
                rbn = lbn
                
        return cont
