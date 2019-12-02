# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or root == None:
            return root
        
        nl = self.lowestCommonAncestor(root.left, p, q)
        nr = self.lowestCommonAncestor(root.right, p, q)
        
        if nl and nr:
            return root
        else:
            return nl if nl else nr
