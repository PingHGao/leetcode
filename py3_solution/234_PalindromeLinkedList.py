# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slw, fst = head, head.next
        
        pre, cur = None, head
        while fst and fst.next:
            slw, fst = slw.next, fst.next.next
            cur.next, pre, cur = pre, cur, cur.next
        
        sub2Head = slw.next
        cur.next = pre
        sub1Head = cur if fst else pre
        n1, n2 = sub1Head, sub2Head
        ans = True
        while n1 or n2:
            if n1.val != n2.val:
                ans = False
                break
            n1, n2 = n1.next, n2.next
        
        return ans
        
