class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        import functools
        people.sort(key=functools.cmp_to_key(cmpPL))
        ans = [] * len(people)
        for p in people:
            ans.insert(p[1], p)
            
        return ans
        
        
def cmpPL(a, b):
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    elif a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        return 0
