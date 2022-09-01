# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node if current node is the max in the path
        def dfs(node, currMax):
            if not node:
                return 0
            
            res = 0
            if node.val >= currMax: # if this node is a good node
                res = 1 # add to good node count
            currMax = max(currMax, node.val) # get the new highest good val
            # preorder
            res += dfs(node.left, currMax) 
            res += dfs(node.right, currMax)
            
            return res
        
        return dfs(root, root.val)