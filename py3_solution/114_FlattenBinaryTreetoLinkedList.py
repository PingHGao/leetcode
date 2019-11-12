# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        n = root
        while n:
            nl, nr = n.left, n.right
            if nl:
                n.left, n.right = None, nl
                nlr = nl
                while nlr.right:
                    nlr = nlr.right
                nlr.right = nr
                
            n = n.right
            
                
