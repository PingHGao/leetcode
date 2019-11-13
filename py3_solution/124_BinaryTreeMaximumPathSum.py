# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def maxPath(node):
            nonlocal ans
            if not node:
                return 0
            
            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))
            
            ans = max(ans, left + right + node.val)
            return max(left, right) + node.val
            
        maxPath(root)
        return ans
