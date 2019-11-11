# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        layer = [root]
        d = 0
        while layer:
            d += 1
            layerN = []
            for n in layer:
                nl, nr = n.left, n.right
                
                if nl:
                    layerN.append(nl)
                if nr:
                    layerN.append(nr)
            layer = layerN
            
        return d
