# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left root right
        # all the way down to the left, then root, then right
        # 1,4,2,3,5,6,7 --> 3,4,5,1,6,2,7
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)