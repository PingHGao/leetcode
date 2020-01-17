class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        lenT = len(tasks)
        tasks = collections.Counter(tasks)
        
        maxC = max(tasks.values())
        maxT = [k for k, v in tasks.items() if v == maxC]
        ans = (maxC - 1) * (n + 1) + len(maxT)
        
        if lenT < ans:
            return ans
        else:
            return lenT
