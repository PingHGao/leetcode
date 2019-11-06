# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        layerCur = [root]
        
        isEqual = lambda nl, nr : (nl == nr == None) or (nl and nr and nl.val == nr.val)
        
        while 1:
            l, r = 0, len(layerCur) - 1
            
            while l < r:
                if not isEqual(layerCur[l], layerCur[r]):
                    return False
                l += 1
                r -= 1
            
            allNone = True
            layerNext = []
            for n in layerCur:
                if not n:
                    ln, rn = None, None
                else:
                    ln, rn = n.left, n.right
                if ln or rn:
                    allNone = False
                
                layerNext.append(ln)
                layerNext.append(rn)
            layerCur = layerNext
            if allNone:
                return True
