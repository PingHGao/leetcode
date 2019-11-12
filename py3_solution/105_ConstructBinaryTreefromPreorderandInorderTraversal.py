# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, P: List[int], I: List[int]) -> TreeNode:
        if not P:
            return None
        
        root = self.divideList(P, 0, len(P) - 1, I, 0, len(I) - 1)
        
        return root
        
    def divideList(self, P, pl, pr, I, il, ir):
        if pr - pl < 0:
            return None
        elif pr == pl and pr >= 0 and pr < len(P):
            root = TreeNode(P[pl])
            return root
        
        root = TreeNode(P[pl])
        for i in range(il, ir + 1):
            if P[pl] == I[i]:
                break
                
        root.left = self.divideList(P, pl + 1, i - il + pl, I, il, i-1)
        root.right = self.divideList(P, pl + i - il + 1, pr, I, i + 1, ir)
        
        return root
