# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop()) # need to get rid of the roots
        mid = inorder.index(root.val) # have to use root.val since the root itself may potentially not be there anymore
        
        # have to do right first because of postorder traversal recursion?
        root.right = self.buildTree(inorder[mid + 1:], postorder) # right side of the subtree
        root.left = self.buildTree(inorder[:mid], postorder) # left side of the subtree 
        
        return root
        
        