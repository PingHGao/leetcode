class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cnt = 0
        for n in nums:
            if cnt == 0:
                res, cnt = n, 1
            elif res == n:
                cnt += 1
            else:
                cnt -= 1
                
        return res
