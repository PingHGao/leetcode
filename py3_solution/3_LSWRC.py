class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cursub = ''
        maxlen, curlen = 0, 0
        for val in s:
            if val not in cursub:
                cursub = ''.join((cursub, val))
            else:
                curlen = len(cursub)
                if maxlen < curlen:
                    maxlen = curlen
                cursub = cursub.split(val)[-1]
                cursub = ''.join((cursub, val))
        curlen = len(cursub)
        if maxlen < curlen:
            maxlen = curlen

        return maxlen
