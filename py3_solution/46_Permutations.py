class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        
        results = [list(res) for res in permutations(nums, len(nums))]
        
        return results
