class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = '('
        
        if n == 0:
            return [""]
        
        def generator(Parens):            
            lpN = len([d for d in Parens if d == '('])
            apN = len(Parens)
            rpN = apN - lpN
            if lpN >= rpN and lpN <= n:
                if lpN + rpN >= n*2:
                    res.append(Parens)
                    while 1:
                        s = Parens[-1]
                        Parens = Parens[:-1]
                        if s == '(':
                            break
                    if not Parens:
                        return
                    else:
                        generator(Parens + ')')
                else:
                    generator(Parens + '(')
            else:
                while 1:
                    s = Parens[-1]
                    Parens = Parens[:-1]
                    if s == '(':
                        break
                if not Parens:
                    return
                else:
                    generator(Parens + ')')
        generator(s)
        return res
