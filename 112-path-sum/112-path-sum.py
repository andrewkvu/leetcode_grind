# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # have a sum in your dfs function that you compute over time
        # if the total is = targetSum, return True
        # if the total is >= targetSum, return False
        # if not tree, return False
        # if not tree and sum < targetSum, return False
        
        if not root:
            return False
        if (not root.left and not root.right) and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)