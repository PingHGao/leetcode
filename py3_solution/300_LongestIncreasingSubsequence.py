class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln < 1:
            return 0
        
        tmp = list()
        for n in nums:
            low, up = 0, len(tmp)
            while low < up:
                mid = (up - low) // 2 + low
                if n > tmp[mid]:
                    low = mid + 1
                else:
                    up = mid
            if up == len(tmp):
                tmp.append(n)
            else:
                tmp[up] = n
                
        return len(tmp)
            
                
                
            
