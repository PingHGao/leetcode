class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp, css = collections.Counter(p), collections.Counter()
        lenp = len(p)
        ans = []
        for i, ch in enumerate(s):
            if ch in p:
                css[ch] += 1
            ind = i - lenp
            if ind >= 0 and s[ind] in p:
                css[s[ind]] -= 1
            
            if css == cp:
                ans.append(ind + 1)
        
        return ans
