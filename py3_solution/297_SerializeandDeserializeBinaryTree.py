# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        strs = '#'
        layer = [root]
        while 1:
            flag = False
            for n in layer:
                if n:
                    flag = True
                    break
            
            if not flag:
                break
            
            vals = [str(n.val) if n else 'null' for n in layer]
            strs = ','.join([strs, ','.join(vals)])
            layerN = []
            [layerN.extend([n.left, n.right]) for n in layer if n]
            layer = layerN

        return strs[2:]
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        
        root = TreeNode(int(data[0]))
        layer = [root]
        nls = 1
        nll = 2
        
        while nls < len(data):
            layerN = [TreeNode(int(num)) if num != 'null' else None for num in data[nls:nls + nll]]
            tmpN = layerN.copy()
            for n in layer:
                if not n:
                    continue
                n.left = tmpN.pop(0)
                n.right = tmpN.pop(0)
            
            nls += nll
            layer = [n for n in layerN if n]
            nll = len(layer) * 2
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
