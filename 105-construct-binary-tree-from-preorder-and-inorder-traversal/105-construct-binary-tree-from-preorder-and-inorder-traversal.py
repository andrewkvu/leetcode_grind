# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # root is always first of preorder
        mid = inorder.index(preorder[0]) # find the root in the inorder
        # also tells us how many nodes will be in the left subtree
        
        # create left subtree 
        # subarray from 1 to mid in the preorder and from 0 to mid in the inorder
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid]) 
        
        # create right subtree
        # subarray from mid to the end in preorder and from mid to the end in inorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root