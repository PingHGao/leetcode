# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None or root == []:
            return []
        
        ans = []
        layer = [root]
        while layer != []:
            vals = [n.val for n in layer]
            ans.append(vals)
            
            layerN = []
            for n in layer:
                nl, nr = n.left, n.right
                if nl:
                    layerN.append(nl)
                if nr:
                    layerN.append(nr)
                
            layer = layerN
            
        return ans
