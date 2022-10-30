# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs function, have left and right boundaries
        # if node is null, technically valid for bst
        # check if the node is valid (within the left and right boundaries)
            # if its not, return false
        # recurse down the whole tree, adjusting the boundaries with left and right
        
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val and right > node.val):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, float('-inf'), float('inf'))