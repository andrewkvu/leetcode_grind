# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # can insert when its a null value
            return TreeNode(val)
        if root.val < val: # right side insert recursion
            root.right = self.insertIntoBST(root.right, val)
        else: # left side insert recursion
            root.left = self.insertIntoBST(root.left, val)
        return root