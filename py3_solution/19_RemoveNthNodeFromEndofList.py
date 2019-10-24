# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not n:
            return head
        
        nNode, tailNode, i = head, head, 0
        ibigger = False
        while 1:
            tailNode = tailNode.next
            if not tailNode:
                break
            i += 1
            if i > n:
                nNode = nNode.next
        l = i + 1
        if n == l:
            head = head.next
        else:
            nNode.next = nNode.next.next
        
        return head
