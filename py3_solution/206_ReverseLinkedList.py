# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        n, pre = head, None
        while n:
            nxt = n.next
            n.next = pre
            
            n, pre = nxt, n
            
            
        return pre
