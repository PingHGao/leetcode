class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        res = []
        candidates.sort()
        
        def comb(candidates, target, index, res, results):
            if target == 0:
                results.append(res)
                return
            
            if res and res[-1] > target:
                return
            
            for i in range(index, len(candidates)):
                comb(candidates, target - candidates[i], i, res + [candidates[i]], results)
                
        comb(candidates, target, 0, res, results)
        
        return results
