class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        if nums[-1] == target:
            return len(nums)-1
        
        pivot = -1
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            if nums[i] > nums[i + 1]:
                pivot = i
                break
        
        if pivot == -1:
            return -1
        
        if nums[pivot + 1] > target:
            return -1
        else:
            sind = pivot+1
            while sind < len(nums):
                if nums[sind] == target:
                    return sind
                if nums[sind]>target:
                    break
                sind +=1
        return -1
