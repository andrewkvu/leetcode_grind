# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.inorder(root)
        # swap the first and second values that you eventually get from inorder traversal
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        
        # inorder L ROOT R
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        # do some stuff
        # if first (left sided) element has not been found and
        # prev not initialized or prev doesn't follow bst structure 
        # cause left >= root when it shouldn't, assign it to prev
        if not self.first and (not self.prev or self.prev.val >= node.val):
            self.first = self.prev
        
        # if first element is found, assign second element to the root node
        if self.first and self.prev.val >= node.val:
            self.second = node
        self.prev = node
        self.inorder(node.right)