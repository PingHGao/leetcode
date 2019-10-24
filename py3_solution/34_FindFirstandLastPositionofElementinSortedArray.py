class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        flag_find = False
        for i, n in enumerate(nums):
            if n == target:
                flag_find = True
                break
            elif n > target:
                return [-1, -1]
        if not flag_find:
            return [-1, -1]
        
        lind = rind = i
        while rind < len(nums):
            if nums[rind] != target:
                break
            
            rind += 1
            
        return [lind, rind - 1]
            
