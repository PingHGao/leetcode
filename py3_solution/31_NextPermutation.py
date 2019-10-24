class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l <= 1:
            return
        
        ind = l - 2
        flag_dicendent = False
        while ind >= 0:
            if nums[ind] < nums[ind + 1]:
                flag_dicendent = True
                break
            ind -= 1
        lind = ind
        
        if flag_dicendent:
            ind = l - 1
            while 1:
                if nums[ind] > nums[lind]:
                    break
                ind -= 1
            rind = ind
            
            nums[lind], nums[rind] = nums[rind], nums[lind]
            i = lind + 1
            j = l - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return
        else:
            nums.sort()
            return
        
        
