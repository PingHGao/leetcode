class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        stack, ans = list(), list()
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                stack.pop()
                
            stack.append(i)
            if i - stack[0] >= k:
                stack.pop(0)
            
            if i >= k - 1:
                ans.append(nums[stack[0]])
                
        return ans
