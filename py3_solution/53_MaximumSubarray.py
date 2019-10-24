class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lenN = len(nums)
        maxN= max(nums)
        if maxN < 0:
            return maxN
        
        maxSum = 0
        
        i = 0
        while 1:
            if i >= lenN:
                break
                
            if nums[i] <= 0:
                i += 1
                continue
            
            sTmp = 0
            for j in range(i, lenN):
                sTmp += nums[j]
                if sTmp > maxSum:
                    maxSum = sTmp

                if sTmp <= 0:
                    break
            i = j + 1
        
        return maxSum
