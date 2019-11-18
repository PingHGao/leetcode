class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        locMax = locMin = glbMax = nums[0]
        for n in nums[1:]:
            locMax, locMin = max(locMax * n, locMin * n, n), min(locMax * n, locMin * n, n)
            glbMax = max(locMax, glbMax)
            
        return glbMax
