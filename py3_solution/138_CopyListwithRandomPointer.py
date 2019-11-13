"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        headN = Node(head.val, None, None)
        O2N = {head: headN}
        
        nnPre = headN
        no = head.next
        while no != None:
            nn = Node(no.val, None, None)
            nnPre.next, nnPre = nn, nn
            O2N[no] = nn
            
            no = no.next
            
        nn = headN
        no = head
        while nn:
            if no.random:
                nn.random = O2N[no.random]
            else:
                nn.random = None
            nn, no = nn.next, no.next
            
        return headN
            
