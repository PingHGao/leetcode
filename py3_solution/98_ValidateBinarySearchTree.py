# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stc = []
        pre = None
        while root or stc:
            if root:
                stc.append(root)
                root = root.left
            else:
                root = stc.pop()
                if pre and root.val <= pre.val:
                    return False
                
                pre = root
                root = root.right
        
        return True
