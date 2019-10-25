class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
            
        return list(dic.values())
