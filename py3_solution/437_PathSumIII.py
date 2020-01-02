# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        result = 0
        if not root:
            return result
        
        result += self.hasPath(root, s)
        result += self.pathSum(root.left, s)
        result += self.pathSum(root.right, s)
        
        return result
        
        
    def hasPath(self, root, s):
        result = 0
        if not root:
            return result
        
        if root.val == s:
            result += 1
            
        result += self.hasPath(root.left, s - root.val)
        result += self.hasPath(root.right, s - root.val)
        
        return result
