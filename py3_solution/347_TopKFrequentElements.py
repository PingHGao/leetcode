class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        ans = c.most_common(k)
        ans = [n for n, _ in ans]
        
        return ans
