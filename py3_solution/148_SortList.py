# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        mid, lst = head, head
        while lst.next != None and lst.next.next != None:
            lst = lst.next.next
            mid = mid.next
            
        lst, mid.next = mid.next, None
        
        return self._merge(self.sortList(head), self.sortList(lst))
        
    def _merge(self, h1, h2):
        h = ListNode(0)
        
        tmp = h
        while h1 and h2:
            if h1.val < h2.val:
                tmp.next, h1 = h1, h1.next
            else:
                tmp.next, h2 = h2, h2.next
            
            tmp = tmp.next
        
        tmp.next = h1 or h2
        
        return h.next               
        
