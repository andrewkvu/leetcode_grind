# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # if subRoot null, it can be a tree of S
        if not root: return False # if root null AFTER subRoot not null, subtree can't exist
        if self.isSameTree(root, subRoot): # go through each potential subtree to compare
            return True
        # since the subtree can be of the left OR right of the root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # case where the root == subtree are the same
    # and in general to check at each part of the root compared to the subroot
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False