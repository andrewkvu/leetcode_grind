# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def dfs(node):
            if not node:
                return False
            # dfs down the tree
            left = dfs(node.left)
            right = dfs(node.right)
            # check if this current node is one of the ancestors
            cur = (node == p) or (node == q)
            # check if two of the three nodes are ancestors, then set the answer to this node
            # should find answer here so no need to go further
            if (left and right) or (left and cur) or (right and cur):
                self.ans = node
                return
            # return if one of these has an ancestor from this root of the tree
            return left or right or cur
        
        dfs(root)
        return self.ans