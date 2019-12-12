class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stc = [s]
        while stc:
            ans = [d for d in stc if self.isvalid(d)]
            if ans:
                return ans

            stcN = []
            [stcN.extend(self.delete(subs)) for subs in stc]
            stc = list(set(stcN))
            

    def delete(self, s):
        ans = [''.join([s[0:i], s[i+1:]]) for i in range(len(s)) if s[i] == ')' or s[i] == '(']
        ans = list(set(ans))

        return ans
        
        
    def isvalid(self, s):
        stc = list()
        for ch in s:
            if ch == '(':
                stc.append(ch)
            elif ch == ')':
                if len(stc) == 0:
                    return False
                stc.pop()
                continue
            else:
                continue
        if stc == []:
            return True
        else:
            return False
