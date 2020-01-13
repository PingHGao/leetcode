class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsS = nums.copy()
        numsS.sort()
        
        lind, rind = 0, len(nums) - 1
        lwrong, rwrong = False, False
        while lind < rind:
            if nums[lind] == numsS[lind]:
                lind += 1
            else:
                lwrong = True
                
            if nums[rind] == numsS[rind]:
                rind -= 1
            else:
                rwrong = True
                
            if rwrong and lwrong:
                break
        
        ans = rind - lind
        ans = ans + 1 if ans > 0 else 0
        return ans
