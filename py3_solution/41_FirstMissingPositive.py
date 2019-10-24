class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lenN = len(nums)
        if lenN == 0:
            return 1
        
        ind = 0
        while ind < lenN:
            val = nums[ind]
            
            if val > 0 and val < lenN and val != ind + 1 and nums[val - 1] != val:
                nums[ind], nums[val - 1] = nums[val - 1], val
                continue
            
            ind += 1
            
        for i, val in enumerate(nums):
            if i + 1 != val:
                return i + 1
            
        return i + 2
