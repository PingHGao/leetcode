class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [1] * ln
        
        sPre = 1
        for i, n in enumerate(nums):
            res[i] = sPre
            sPre *= n
        sPre = 1
        for i in range(ln - 1, -1, -1):
            res[i] *= sPre
            sPre *= nums[i]
            
        return res
