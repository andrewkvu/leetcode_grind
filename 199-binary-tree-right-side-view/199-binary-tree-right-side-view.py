# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # keep track of a depth and compare it to the length of res
        # prioritize taking the right nodes first, then the left nodes
        res = []
        
        def dfs(root, depth): 
            if root:
                if depth == len(res):
                    res.append(root.val)
                dfs(root.right, depth + 1)
                dfs(root.left, depth + 1)
            
        dfs(root, 0)
        return res