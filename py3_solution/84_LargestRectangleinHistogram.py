class Solution:
    def largestRectangleArea(self, H) -> int:
        maxRec = 0
        stc = []
        H.append(0)

        for i in range(len(H)):
            if stc == []:
                stc.append([i, H[i]])
                continue

            Vi, Vstc = H[i], stc[-1][1]
            if Vi > Vstc:
                stc.append([i, H[i]])
            elif Vi < Vstc:
                ind = None
                for j in range(len(stc) - 1, -1, -1):
                    if stc[j][1] > Vi:
                        tmp = (i - stc[j][0]) * stc[j][1]
                        ind = stc[j][0]
                        if tmp > maxRec:
                            maxRec = tmp
                        stc.pop(j)
                    elif stc[j][1] == Vi:
                        break
                    else:
                        stc.append([ind, Vi])
                if stc == []:
                    stc.append([ind, Vi])

        return maxRec
