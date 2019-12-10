# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow, fast = head, head.next
        while slow != fast:
            slow = slow.next if slow else None
            fast = fast.next.next if fast and fast.next else None
            
        if not slow:
            return None
            
        entry = head
        slow = slow.next
        while entry != slow:
            entry = entry.next
            slow = slow.next
            
        return entry
        
