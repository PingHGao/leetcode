class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        
        from collections import Counter
        dictT = Counter(t)
        lenDT = len(dictT)
        
        filteredS = []
        for i, val in enumerate(s):
            if val in t:
                filteredS.append((i, val))
        
        l, r = 0, 0
        countN = 0
        windowC = {}
        
        ans = float('inf'), None, None
        
        while r < len(filteredS):
            ch = filteredS[r][1]
            windowC[ch] = windowC.get(ch, 0) + 1
            
            if windowC[ch] == dictT[ch]:
                countN += 1
                
            while l <= r and countN == lenDT:
                ch = filteredS[l][1]
                
                en = filteredS[r][0]
                st = filteredS[l][0]
                if en - st + 1 < ans[0]:
                    ans = (en - st + 1, st, en)
                    
                windowC[ch] -= 1
                if windowC[ch] < dictT[ch]:
                    countN -= 1
                    
                l += 1
                
            r += 1
            
        res = '' if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
        return res
                
