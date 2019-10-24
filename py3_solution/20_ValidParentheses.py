class Solution:
    def isValid(self, s: str) -> bool:
        from queue import LifoQueue
        braOp = LifoQueue()
        
        OpenBras = ['(', '{', '[']
        CloseBras = [')', '}', ']']
        
        isSametype = lambda x, y: (x == '(' and y == ')') or (x == '{' and y == '}') or (x == '[' and y == ']')
        
        for bra in s:
            if bra in OpenBras:
                braOp.put(bra)
            elif bra in CloseBras:
                if braOp.empty():
                    return False
                val = braOp.get()
                if not isSametype(val, bra):
                    return False
            else:
                return False
            
        return braOp.empty()
