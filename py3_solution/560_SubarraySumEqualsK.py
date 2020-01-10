class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lenN = len(nums)
        
        s, ans, sums = 0, 0, [0]
        for n in nums:
            s += n
            res = s - k
            ans += sums.count(res)
            
            sums.append(s)
                
        return ans
