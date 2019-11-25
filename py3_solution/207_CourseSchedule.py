class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        from collections import Counter
        import numpy as np
        Preq = np.array(prerequisites)
        
        ns = list(set(Preq[:,0]))
        
        while ns:
            idg = Counter(Preq[:, 1])
            for i, n in enumerate(ns):
                if n not in idg:
                    del ns[i]
                    Preq = np.delete(Preq, np.where(Preq[:, 0] == n), axis=0)
                    break
            else:
                break
                
        return not ns
