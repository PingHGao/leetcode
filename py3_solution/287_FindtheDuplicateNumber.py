class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return -1
        
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        entry = nums[0]
        slow = nums[slow]
        while slow != entry:
            entry = nums[entry]
            slow = nums[slow]
            
        return entry
            
