# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        stack = [(0, root)]
        result = {None: (0, 0)}
        
        while stack:
            robbed, node = stack.pop()
            if not node:
                continue
            
            if not robbed:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                result[node] = (result[node.left][1] + result[node.right][1] + node.val,
                               max(result[node.left]) + max(result[node.right]))
                
        return max(result[root])
