class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlon = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                tmplon = 1
                numcur = num + 1
                while numcur in nums_set:
                    tmplon += 1
                    numcur += 1
                    
                maxlon = max(maxlon, tmplon)
                
        return maxlon
