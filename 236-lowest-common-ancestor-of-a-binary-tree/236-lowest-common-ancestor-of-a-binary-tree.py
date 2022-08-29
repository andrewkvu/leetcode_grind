# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False
            # recurse dfs traversal
            currLeft = dfs(node.left)
            currRight = dfs(node.right)
            
            # basically check if the current node is one of the ancestors
            mid = node == p or node == q
            # we need 2 of these to be true
            if currLeft + currRight + mid >= 2:
                self.ans = node
            return mid or currLeft or currRight
        
        dfs(root)
        return self.ans