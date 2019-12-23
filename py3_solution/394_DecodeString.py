class Solution:
    def decodeString(self, s: str) -> str:
        slength = len(s)
        stack = []
        
        ind = 0
        while ind < slength:
            sc = s[ind]
            
            if sc.isdigit():
                numstc = []
                while sc.isdigit():
                    numstc.append(sc)
                    ind += 1
                    sc = s[ind] 
                n = int(''.join(numstc))
                stack.append(n)
            elif sc == ']':
                stmp = ''
                while 1:
                    st = stack.pop()
                    if st == '[':
                        break
                    stmp = ''.join([st, stmp])
                stmp = stmp * stack.pop()
                stack.append(stmp)
                ind += 1
            else:
                stack.append(sc)
                ind += 1
        return ''.join(stack)
