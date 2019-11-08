# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root or root.val == None:
            return []
        
        stc = [root]
        ans = []
        poped = False
        while stc != []:
            n = stc[-1]
            lson = n.left
            if lson and not poped:
                stc.append(lson)
                continue
            rson = n.right
            ans.append(n.val)
            stc.pop()
            poped = True
            if rson:
                stc.append(rson)
                poped = False
        
        return ans
