# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
                return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            head = l1
        else:
            head, l1, l2.next, l2 = l2, l2, l1, l2.next
            
        l1p, l1 = l1, l1.next
        while 1:
            if l2 == None:
                break
            
            if l1 == None:
                l1p.next = l2
                break
            x1, x2 = l1.val, l2.val
            if x2 <= x1:
                l1p.next, l2.next, l2 = l2, l1, l2.next
                l1p = l1p.next
            else:
                l1p, l1 = l1, l1.next
                
        return head
                
        
