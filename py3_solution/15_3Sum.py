class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return list(res)
                    
