class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        g = collections.defaultdict(list)
        idg, vst, q = [0] * n, [0] * n, []
        
        for i, j in prerequisites:
            g[i].append(j)
            idg[j] += 1
            
        for i in range(n):
            if idg[i] == 0:
                q.append(i)
                vst[i] = 1
                
        while q:
            ind = q.pop(0)
            n -= 1
            
            for i in g[ind]:
                idg[i] -= 1
                if idg[i] == 0 and vst[i] == 0:
                    q.append(i)
                    vst[i] = 1
                    
        return n == 0
