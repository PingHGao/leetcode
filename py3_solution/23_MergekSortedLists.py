# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        indNode = head
        
        while 1:
            vals = [n.val for n in lists if n]
            if vals == []:
                break
                
            minval = min(vals)
            for i, node in enumerate(lists):
                if node and node.val == minval:
                    indNode.next, lists[i], indNode = node, node.next, node
                    
        return head.next
