class Solution:
    def countSubstrings(self, s: str) -> int:
        lenS = len(s)
        ans = 0
        def getLongestPalindrome(s, l, r):
            nonlocal ans
            overfit = lambda v, l, r: v < l or v > r
            clamp = lambda v, l, r:min(max(v,l), r)
            if overfit(l, 0, lenS - 1) or overfit(r, 0, lenS - 1):
                l = clamp(l + 1, 0, lenS - 1)
                r = clamp(r - 1, 0, lenS - 1)
                return r + 1 - l, s[l:r+1]

            if s[l] == s[r]:
                ans += 1
                return getLongestPalindrome(s, l-1, r+1)
            else:
                l = clamp(l + 1, 0, lenS - 1)
                r = clamp(r - 1, 0, lenS - 1)
                return r + 1 - l, s[l:r + 1]

        maxlen, maxstr = 0, ''
        for i in range(lenS):
            strlen, strs = getLongestPalindrome(s, i, i)
            if maxlen < strlen:
                maxlen = strlen
                maxstr = strs

        for i in range(lenS - 1):
            strlen, strs = getLongestPalindrome(s, i, i+1)
            if maxlen < strlen:
                maxlen = strlen
                maxstr = strs

        return ans
