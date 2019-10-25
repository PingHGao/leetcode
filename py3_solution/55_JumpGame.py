class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = True
        lenN = len(nums)
        
        if lenN == 1:
            return True
        
        ind = 0
        res = True
        while ind < lenN - 1:
            if nums[ind] > 0:
                ind += nums[ind]
                continue
                
            for i in range(ind):
                if i + nums[i] > ind:
                    ind = i + nums[i]
                    break
            else:
                res = False
                break
            
        return res
                
