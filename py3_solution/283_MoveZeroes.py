class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, n in enumerate(nums):
            if n != 0:
                if k != i:
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1
            
