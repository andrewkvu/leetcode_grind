# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive dfs? and then check if the p == q
        
        # if both are null that means the tree is over?
        if not p and not q:
            return True
        # if one is null, means tree structure isnt good
        if not p or not q:
            return False
        # checking for same value
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        