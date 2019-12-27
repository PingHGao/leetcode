class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        return self._canPartition(nums, len(nums) - 1, s / 2)
        
    def _canPartition(self, nums, index, s):
        if s == 0:
            return True
        if index < 0 or s < 0 or nums[index] > s:
            return False
        
        return self._canPartition(nums, index - 1, s - nums[index]) or self._canPartition(nums, index - 1, s)
