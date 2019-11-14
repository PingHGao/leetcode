# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        n = head
        ans = False
        while n:
            if d[n]:
                ans = True
                break
            d[n] = 1
            n = n.next
            
        return ans
