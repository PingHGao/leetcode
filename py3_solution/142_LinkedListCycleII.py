# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        from collections import defaultdict
        ht = defaultdict(int)
        
        n = head
        ans = None
        while n:
            if ht[n]:
                ans = n
                break
            
            ht[n] = 1
            n = n.next
            
        return ans
