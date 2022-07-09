# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right): # left and right boundaries
            if not node: # technically valid
                return True
            if not (left < node.val and node.val < right): # checking if the left and right nodes are not BST valid
                return False
            
            # for left call, left bound stays same - right bound is now the parent val to make sure left is less than parent
            return (dfs(node.left, left, node.val) and \
            # fpr right call, left bound changes to the parent, right bound stays same
            dfs(node.right, node.val, right))    
        
        return dfs(root, float('-inf'), float('inf'))
            