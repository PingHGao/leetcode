class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 0:
            mod = 'e'
            ind = (m + n ) // 2
        else:
            mod = 'o'
            ind = (m + n) // 2 + 1
            
        indm, indn = 0, 0
        curnum = 0
        for i in range(ind):
            numm = nums1[indm] if indm < m else float('inf')
            numn = nums2[indn] if indn < n else float('inf')
            if numm < numn:
                curnum = numm
                indm += 1
            else:
                curnum = numn
                indn += 1
                
        if mod == 'e':
            numm = nums1[indm] if indm < m else float('inf')
            numn = nums2[indn] if indn < n else float('inf')
            if numm < numn:
                curnum += numm
                indm += 1
            else:
                curnum += numn
                indn += 1
            curnum /= 2
            
        return curnum
