class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenN = len(nums)
        indl, indr = 0, lenN - 1
        
        while indl < lenN:
            if nums[indl] == 0:
                indl += 1
            else:
                break
                
        while indr > -1:
            if nums[indr] == 2:
                indr -= 1
            else:
                break
        
        ind = indl
        while ind <= indr:
            flag_s = False
            
            if nums[ind] == 1:
                ind += 1
            elif nums[ind] == 0:
                nums[indl], nums[ind] = nums[ind], nums[indl]
                indl += 1
                flag_s = True
            else:
                nums[indr], nums[ind] = nums[ind], nums[indr]
                indr -= 1
                flag_s = True
            
            if flag_s:
                while indl < lenN:
                    if nums[indl] == 0:
                        indl += 1
                    else:
                        break

                while indr > -1:
                    if nums[indr] == 2:
                        indr -= 1
                    else:
                        break
                if ind < indl:
                    ind = indl
