# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        
        def maxDiameter(n):
            nonlocal res
            
            if not n:
                return 0
            l = maxDiameter(n.left)
            r = maxDiameter(n.right)
            res = max(res, l + r)
            
            return max(l, r) + 1
        
        maxDiameter(root)
        return res
