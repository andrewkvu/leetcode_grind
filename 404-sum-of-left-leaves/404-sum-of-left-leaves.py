# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, isLeft):
            if not root:
                return 0
            if not root.left and not root.right: # if the node is a leaf
                if isLeft: # isLeft is only true when it's called with dfs(root.left, True)
                    return root.val
                else: # doesn't matter
                    return 0
            return dfs(root.left, True) + dfs(root.right, False)
            
        return dfs(root, False) # isLeft starts out as False
            