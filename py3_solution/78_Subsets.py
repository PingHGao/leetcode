class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        
        ans = []
        ans.append(nums)
        ans.append([])
        
        for i in range(1, len(nums)):
            for r in combinations(nums, i):
                ans.append(list(r))
                
        return ans
