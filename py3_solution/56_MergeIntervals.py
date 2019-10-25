class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        indl = 0
        numITV = len(intervals)
        
        while indl < numITV:
            ll = intervals[indl]
            for indr in range(indl + 1, numITV):
                lr = intervals[indr]
                maxV = max(ll[0], ll[1], lr[0], lr[1])
                minV = min(ll[0], ll[1], lr[0], lr[1])
                if ll[1] - ll[0] + lr[1] - lr[0] >= maxV - minV:
                    intervals[indl] = [minV, maxV]
                    del intervals[indr]
                    numITV = len(intervals)
                    break
            else:
                indl += 1
                
        return intervals
